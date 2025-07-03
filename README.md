# File sort

Now sort your files with just one command.

## Sorting Features
- Sort by Alphabet
- Sort by Date (format YYYY/MM/DD)
- Sort by File Extension
- Sort by File Extension by Group
- Sort by Make
- Sort by Model

Also supports to arranges file in nested folder structure like `Output/Data/Make/Model` for all the options mentioned above.

This scripts lets you filter out specific file extensions while sorting.
e.g Sort only `.mp4` files from `source` dir into `des` dir

### System requriments.
- `Python3.10+`
- `ExifTool`

### Tested platform
```
- Windows 11 x64
```

### Project setup
```
- git clone https://github.com/NishantGhanate/FileSort.git
- cd FileSort
- python -m venv venv
- [Win] > venv\Scripts\activate
- [Linux] $ venv/bin/activate
- pip install -r requriments.txt
```

### Download this tool
```
- Download & Install: https://exiftool.org/
- For Windows Installer: https://oliverbetz.de/pages/Artikel/ExifTool-for-Windows
```

## To install project locally
```
For development
> pip install -e .

For final build testing
> python -m pip install .
```


## To build project locally
```
> python -m build
> pip install dist/file_sort-0.0.10-py3-none-any.whl
```

### HELP
```
> python -m file_sort.cli -h
```

### Run cli: Default command
```
> python -m file_sort.cli --input_paths "E:\\src" --output_path "E:\\dest"
```

### Defaults Args for cli
```
--shift_type copy
--nested_order date
--process_type linear
--file_extensions "{pre-defined inside constants}"
```

#### Args and its values
```
--shift_type : copy | move
--nested_order : alphabet date file_extension file_extension_group make model
--process_type : linear | parallel
--file_extensions "{pre-defined inside constants all basic formats}"
```



### With Extra Arguments:
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
