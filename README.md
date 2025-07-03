# File sort

Now sort your files with just one command.

## Sorting Features
- Sort by Alphabet
- Sort by Date (format YYYY/MM/DD)
- Sort by File Extension
- Sort by File Extension by Group
- Sory by Location by given radius
- Sort by Make
- Sort by Model

Also supports to arranges file in nested folder structure like `Output/Data/Make/Model` for all the options mentioned above.

This scripts lets you filter out specific file extensions while sorting.
e.g Sort only `.mp4` files from `source` dir into `des` dir

### System requriments.
- `Python3.10+`
- `ExifTool`

### Project setup
```
- git clone <project_url>
- cd <folder_name>
- python -m venv venv
- [Win] > venv\Scripts\activate | [Linux] $ venv/bin/activate
- pip install -r requriments.txt

- Download & Install https://exiftool.org/
- For Windows Installer https://oliverbetz.de/pages/Artikel/ExifTool-for-Windows
```

## To install project locally
```
For development
> pip install -e .

For final build testing
> python -m pip install .
```


# To build project locally
```
> python -m build
> pip install dist/file_sort-0.0.10-py3-none-any.whl
```

## HELP
```
> python -m file_sort.cli -h
```

### Run project
Default:
```
> python -m file_sort.cli --input_paths "E:\\src" --output_path "E:\\dest"

> python -m file_sort.cli --input_paths "E:\\src" --output_path "E:\\dest" --nested_order model
```

Extra Arguments:
```
python -m file_sort.cli --input_paths "E:\\src" --output_path "E:\\dest" --shift_type "move"

python -m file_sort.cli --input_paths "E:\\src" --output_path "E:\\dest" --shift_type "move" --nested_order date file_extension

python -m file_sort.cli --input_paths "E:\\src" --output_path "E:\\dest" --nested_order make

python -m file_sort.cli --input_paths "E:\\src" --output_path "E:\\dest" --shift_type "copy" --process_type "parallel"

```

Multiple input folder example:
> python -m file_sort.cli --input_paths "E:\temp" "E:\GoogleDrive" "E:\DCIM" --output_path "E:\Memories"

> python -m file_sort.get_meta_data --input_paths "E:\\src\\IMG_4267.HEIC"


### Set to test code locally
```
Linux : export PYTHONPATH=.
WIN: set PYTHONPATH=.
```


```
python -m file_sort.app.py
```
