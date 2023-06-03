
import os
import re
import time
import json
import shutil
import exifread
import subprocess
import argparse
from enum import Enum
from pathlib import Path
from datetime import datetime
from dataclasses import dataclass

@dataclass
class FileDate:
    year: str
    month: str
    day: str

class ShiftType(Enum):
    COPY = 'copy'
    MOVE = 'move'
    

class FileSort:

    def __init__(self, output_folder, shift_type= ShiftType.COPY) -> None:
        self.total_counter = 0
        self.files_tracked = {}
        self.output_folder =  Path(output_folder)
        if shift_type == ShiftType.COPY.value:
            self.shift_type = shutil.copy2
        else:
            self.shift_type = shutil.move
        
        self.file_extensions = ('.jpg', '.jpeg', '.png', '.gif', '.heic', '.mp4', '.mov')


    def is_valid_date(self, year, month, day):
        try:
            datetime(int(year), int(month), int(day))
            return True
        except (ValueError, TypeError):
            return False
    

    def get_file_creation_date(self, file_path):
        timestamp = file_path.stat().st_ctime
        file_date_created= datetime.fromtimestamp(timestamp)
        return FileDate(
            year= str(file_date_created.year),
            month= str(file_date_created.month).zfill(2),
            day= str(file_date_created.day).zfill(2)
        )


    def get_file_name_date(self, file_path):
        filename = file_path.parts[-1]
        regex_file_name_patterns = {
            r"(IMG[_-]|IMG|PXL_)?(\d{4})(\d{2})(\d{2}).*?\.(jpg|jpeg|png|gif|heic|mov)" : (2,3,4),
            r"(VIDEO_|VID_|PXL_)?(\d{4})(\d{2})(\d{2}).*?\.(mp4|mov)" : (2,3,4),
        }

        for pattern, group_indexs in regex_file_name_patterns.items():
            match = re.match(pattern, filename, flags=re.IGNORECASE)
            if match and self.is_valid_date(
                    year= match.group(group_indexs[0]),
                    month=match.group(group_indexs[1]),
                    day=match.group(group_indexs[2])
                ):
                return FileDate(
                    year= match.group(group_indexs[0]),
                    month=match.group(group_indexs[1]),
                    day=match.group(group_indexs[2])
                )
        
        return None


    def get_date_taken(self, file_path):
        try:
            with open(file_path, 'rb') as f:
                tags = exifread.process_file(f)
                date_taken = tags.get('EXIF DateTimeOriginal') or tags.get('Image DateTime')
                if date_taken is not None:
                    date_taken = date_taken.values[0:10].split(':')
                    return FileDate(
                        year=date_taken[0],
                        month=date_taken[1].zfill(2),
                        day=date_taken[2].zfill(2),
                    )
                return None
        except Exception as e:
            print(f'Error {e} tried to read = {file_path}')
            return None

    def get_metadata(self, input_file_path):
        """
        Extract file meta data through exiftool
        """
        command = ['exiftool', '-json', input_file_path]
        result = subprocess.run(command, capture_output=True, text=True)

        if result.returncode == 0:
            # Parse the JSON output
            metadata = json.loads(result.stdout)

            # DateTimeOriginal-jpg, SubSecDateTimeOriginal-heic, MediaCreateDate - mp4
            taken_date = metadata[0].get('DateTimeOriginal') or \
                metadata[0].get('SubSecDateTimeOriginal') or \
                metadata[0].get('MediaCreateDate')
            
            if taken_date is not None:
                taken_date = taken_date[0:10].split(':')
                return FileDate(
                    year=taken_date[0],
                    month=taken_date[1],
                    day=taken_date[2]
                )
             

            # with open(output_file_path, mode='w') as f:
            #     json_data = json.dumps(metadata, indent=4)
            #     f.write(json_data)

        return None


    def sort_files(self, input_folder):
        processed = 0
        duplicate = 0
        
        print(f'\n\nCurently processing : {input_folder}\n')
        for file_path in input_folder.rglob("*"):
            if file_path.is_file() and file_path.suffix.lower() in self.file_extensions:
                creation_date = (
                    self.get_metadata(file_path) or
                    self.get_date_taken(file_path) or
                    self.get_file_name_date(file_path) or
                    self.get_file_creation_date(file_path)
                )
                
                sub_path = "{year}{sep}{month}{sep}{day}".format(
                    year=creation_date.year,
                    month=creation_date.month,
                    day=creation_date.day,
                    sep=os.sep
                )
                
                output_subfolder = self.output_folder/sub_path
                output_subfolder.mkdir(parents=True, exist_ok=True)

                new_file_path = f"{output_subfolder}{os.sep}{file_path.parts[-1]}"
                
                if not os.path.exists(new_file_path):
                    self.shift_type(str(file_path), str(output_subfolder))
                    processed += 1
                    self.total_counter += 1
                    print(f"""
                    \rFile name= {file_path.parts[-1]},
                    \rdate = {creation_date},
                    \rprocessed= {processed}
                    """,
                    end='\r')
                else:
                    duplicate += 1
                    print(f"""
                    \rFile name= {file_path.parts[-1]},
                    \rdate = {creation_date},
                    \rduplicate= {duplicate}
                    """, end="\r")
                
        
        self.files_tracked[str(input_folder)] = {
            'processed' : processed,
            'duplicate' : duplicate
        }
                

    def print_result(self):
        print(f"\n{'#'*15} Processing Completed {'#'*15}")
        print(self.files_tracked)


    def process_files(self, input_folders):
        for input_folder in input_folders:
            self.sort_files(input_folder= Path(input_folder))
        
        self.print_result()


if __name__ == "__main__":
    
    parser = argparse.ArgumentParser(description='Media file sorting')

    # Add the input & output path argument
    parser.add_argument(
        '--input_paths', nargs='+', required=True, type=str,
        help='Path to the input file'
    )
    parser.add_argument(
        '--output_path', type=str, required=True,
        help='Path to the output file'
    )
    parser.add_argument(
        '--shift_type', type=str, choices=[e.value for e in ShiftType],
        default=ShiftType.COPY.value, help='Path to the output file'
    )

    # Parse the command-line arguments
    args = parser.parse_args()
    output_path_check = Path(args.output_path)
    output_path_check.mkdir(parents=True, exist_ok=True)

    start_time = time.time()

    # Call the process_file function with the provided paths
    file_sort = FileSort(output_folder=args.output_path, shift_type= args.shift_type)
    file_sort.process_files(args.input_paths)

    end_time = time.time()
    runtime = end_time - start_time
    print("\n\nRuntime: {:.2f} seconds".format(runtime))
