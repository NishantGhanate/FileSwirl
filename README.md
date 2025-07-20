
![Python](https://img.shields.io/badge/python-3.10%2B-blue?logo=python&logoColor=white)
[![PyPI](https://img.shields.io/pypi/v/file-swirl?color=brightgreen&logo=pypi)](https://pypi.org/project/file-swirl/)
[![Downloads](https://img.shields.io/pypi/dm/file-swirl?label=Downloads&logo=pypi&color=blue)](https://pypi.org/project/file-swirl/)

# 📁 File swirl

Now Organizes files from chaos to order with just one command.
Organize photos, videos, documents, and more — cleanly and efficiently — using flexible sorting rules.
Can easily process 100 GB +

## ✨ Organize Features
- 📅 Sort by Date — Organize files into folders by creation or modified date.
- 🧩 Filter by File Extension — Group files like .jpg, .mp4, .pdf, etc
- 🏷️ Sort by Camera Make (EXIF.make) — Useful for photographers to group by device brand.
- 🔍 Sort by File Type (MIME) — Organize images, videos, documents, etc.
- 🗂️ Nested Sorting — Apply multi-level sort: e.g., Date → Extension → Make.
- ⚙️ Custom Sort Key Chains — Chain any supported keys in any order.
- 🎛️ Parallel Processing Support — Fast sorting using multi-threading.



Also supports to arranges file in nested folder structure like `Output/Data/Make/Model` for all the options mentioned above.

This scripts lets you filter out specific file extensions while sorting.
e.g Sort only `.mp4` files from `source` dir into `destination` dir



### System requriments.
- `Python3.10+`
- `ExifTool`

### ✅ Supports
- Windows 11 x64
- Linux Ubuntu
- Cli & Gui


### 📸 Screenshot

![FileSwirl UI](assets/Screenshot.png)

## Run Gui *
```
> python -m file_swirl.gui
```



### Project setup
```
- git clone https://github.com/NishantGhanate/FileSwirl.git
- cd FileSwirl
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
```bash
For development
> pip install -e .

For final build testing
> python -m pip install .
```
[Pypi Installer](https://pypi.org/project/file-swirl/):
> pip install file-swirl

## To build project locally
```bash
> python -m build
> pip install dist/file_swirl-0.0.10-py3-none-any.whl
```

### HELP
```bash
> python -m file_swirl.cli -h
```


### Run cli: default command
```bash
> python -m file_swirl.cli --input_paths "E:\\src" --output_path "E:\\dest"
```

### Defaults Args for cli
```bash
--shift_type copy
--nested_order date
--process_type linear
--file_extensions "{pre-defined inside constants}"
```

#### Args and its values
```bash
--shift_type : copy | move
--nested_order : alphabet date file_extension file_extension_group make model
--process_type : linear | parallel
--file_extensions "{pre-defined inside constants all basic formats}"
```

### Examples:

🔁 Move files from a source to a destination
```bash
python -m file_swirl.cli \
  --input_paths "E:\\src" \
  --output_path "E:\\dest" \
  --shift_type "move"
```

🗃️ Move files and organize by nested folders: date file_extension
```bash
python -m file_swirl.cli \
  --input_paths "E:\\src" \
  --output_path "E:\\dest" \
  --shift_type "move" \
  --nested_order date file_extension
```

🏷️ Organize files by camera make/brand
```bash
python -m file_swirl.cli \
  --input_paths "E:\\src" \
  --output_path "E:\\dest" \
  --nested_order make
```

⚡ Copy from multiple folders in parallel mode
```bash
python -m file_swirl.cli \
  --input_paths "E:\\src" "E:\\temp" \
  --output_path "E:\\dest" \
  --shift_type "copy" \
  --process_type "parallel
```




## 🧱 Architecture:
Currently its limited to 1 producer and 4 q each thread will consume from this q
```
+-----------------+       +------------------+
|   Producer(s)   | --->  |  Queue (Stream)  | ---> [Processor 1]
| (dir scanners)  |       |  file paths      | ---> [Processor 2]
+-----------------+       +------------------+ ---> [Processor N]
```

### Set to test code locally
```
Linux : export PYTHONPATH=.
WIN: set PYTHONPATH=.
```

📌 [Project Roadmap](RoadMap.md)
- See the full RoadMap for upcoming features and ideas.
