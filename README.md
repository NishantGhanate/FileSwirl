# File sort

Now sort your media files with just one command.

### System requriments.
- `Python3.10`
- `ExifTool`


### Project setup
```
- git clone <project_url>
- cd <folder_name>
- pip install -r requriments.txt

- Download & Install https://exiftool.org/
- For Windows Installer https://oliverbetz.de/pages/Artikel/ExifTool-for-Windows
```

## To build project locally
```

- pip install .

```

### Run project 
```
> python -m file_sort -h
    --input_paths can take multiple file paths 
    --out_path takes only one path

> python -m file_sort --input_paths "E:\temp" --output_path "E:\Memories"

> python -m file_sort --input_paths "E:\temp" "E:\GoogleDrive" "E:\DCIM" --output_path "E:\Memories"

> python -m file_sort --input_paths "E:\temp" --output_path "E:\Memories" --shift_type "move"

- shift_type options : 
    + move
    + copy 

```

### To test out file meta data
```

Open Cmd and check if tool is installed correctly 

> exiftool -h

meta data via Command prompt:
> exiftool -json E:\Memories\2022\09\25\IMG_1911.HEIC

meta data via python:
> python media_metadata.py --input_path "E:\IMG_1911.HEIC"
> python media_metadata.py --input_path "E:\IMG_1825.MOV" 
> python media_metadata.py --input_path "E:\temp_.jpg"
> python media_metadata.py --input_path "E:\20\VID_24921005_231526_366.mp4"
```


### For android on windwos (wip)

> adb devices
> adb shell
> cd sdcard/dcim
> exit

adb pull /sdcard/dcim E:\temp

adb shell ln -s /mnt/runtime/default/emulated/0 /sdcard