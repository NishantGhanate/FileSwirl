
import os
import re
import time
import json
import shutil
import exifread
import argparse
from glob import glob
from pathlib import Path
from datetime import datetime
from dataclasses import dataclass

@dataclass
class FileDate:
    year: str
    month: str
    day: str

class FileSort:

    def __init__(self) -> None:
        self.total_counter = 0
        self.files_tracked = {}

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
            r"(IMG[_-]|IMG|PXL_)?(\d{4})(\d{2})(\d{2}).*?\.(jpg|jpeg|png|gif|heic)" : (2,3,4),
            r"(VIDEO_|VID_)?(\d{4})(\d{2})(\d{2}).*?\.(mp4|mov)" : (2,3,4),
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
                date_taken = tags.get('EXIF DateTimeOriginal')
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


    def sort_images(self, input_folder, output_folder, file_extensions):
        processed = 0
        duplicate = 0
        
        print(f'\n\nCurently processing : {input_folder}\n')
        for file_path in input_folder.rglob("*"):
            if file_path.is_file() and file_path.suffix.lower() in file_extensions:
                creation_date = self.get_date_taken(file_path)
                if creation_date is None:
                    creation_date = self.get_file_name_date(file_path)
                    if creation_date is None:
                        creation_date = self.get_file_creation_date(file_path)
                
                sub_path = "{year}{sep}{month}{sep}{day}".format(
                    year=creation_date.year,
                    month=creation_date.month,
                    day=creation_date.day,
                    sep=os.sep
                )
                
                output_subfolder = output_folder/sub_path
                output_subfolder.mkdir(parents=True, exist_ok=True)

                new_file_path = f"{output_subfolder}{os.sep}{file_path.parts[-1]}"
                
                if not os.path.exists(new_file_path):
                    shutil.copy2(str(file_path), str(output_subfolder))
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

    def process_files(self, input_folders, output_folder):
        output_path = Path(output_folder)
        file_extensions = ('.jpg', '.jpeg', '.png', '.gif', '.heic', '.mp4', '.mov')
        
        for input_folder in input_folders:
            input_path = Path(input_folder)
            self.sort_images(
                input_folder= input_path,
                output_folder= output_path,
                file_extensions= file_extensions
            )
        
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

    # Parse the command-line arguments
    args = parser.parse_args()
    output_path_check = Path(args.output_path)
    output_path_check.mkdir(parents=True, exist_ok=True)

    start_time = time.time()

    # Call the process_file function with the provided paths
    file_sort = FileSort()
    file_sort.process_files(args.input_paths, args.output_path)

    end_time = time.time()
    runtime = end_time - start_time
    print("\n\nRuntime: {:.2f} seconds".format(runtime))
