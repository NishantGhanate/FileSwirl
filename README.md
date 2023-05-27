# File sort

Now sort your media files with just one command.

### System requriments.
- `Python3.10`


### Project setup
```
- git clone <project_url>
- cd <folder_name>
- pip install exifread

for alias setup
- python310 -m pip install exifread
```

### Run project
```
> python main.py -h
    --input_paths can take multiple file paths 
    --out_path takes only one path

> python main.py --input_paths "E:/temp" --output_path "E:/NewSort"

> python main.py --input_paths "E:/temp" "E:/GoogleDrive" "E:/Memories" --output_path "E:/NewSort"
```


