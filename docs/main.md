# **Documentation for `main.py`**
> _Generated on 2026-01-05 12:45:42_

> _Generated with [DocGen](https://github.com/I-had-a-bad-idea/DocGen), may include wrong information!_



# Table of Contents

- [queue ![set](https://img.shields.io/badge/set-gray&style=flat)](#queue)
- [LANGUAGES ![dict](https://img.shields.io/badge/dict-gray&style=flat)](#languages)
- [ignored_languages ![list](https://img.shields.io/badge/list-gray&style=flat)](#ignored_languages)
- [ignored_folders ![list](https://img.shields.io/badge/list-gray&style=flat)](#ignored_folders)
- [is_supported_language ![function](https://img.shields.io/badge/function-green&style=flat)](#is_supported_language)
- [is_allowed_folder ![function](https://img.shields.io/badge/function-green&style=flat)](#is_allowed_folder)
- [get_code_from_file ![function](https://img.shields.io/badge/function-green&style=flat)](#get_code_from_file)
- [generate_docs_for_file ![function](https://img.shields.io/badge/function-green&style=flat)](#generate_docs_for_file)
- [get_files_for_folder ![function](https://img.shields.io/badge/function-green&style=flat)](#get_files_for_folder)
- [get_files_for_path ![function](https://img.shields.io/badge/function-green&style=flat)](#get_files_for_path)
- [generate_docs ![function](https://img.shields.io/badge/function-green&style=flat)](#generate_docs)
- [load_docgen_ignore ![function](https://img.shields.io/badge/function-green&style=flat)](#load_docgen_ignore)
- [main ![function](https://img.shields.io/badge/function-green&style=flat)](#main)

---

# Overview
This script is a tool for generating documentation from source code files. It supports various programming languages and can be used to generate Markdown documentation.			
**Language**: Python

## Key components
queue,
LANGUAGES,
ignored_languages,
ignored_folders,
is_supported_language,
is_allowed_folder,
get_code_from_file,
generate_docs_for_file,
get_files_for_folder,
get_files_for_path,
generate_docs,
load_docgen_ignore,
main
## Requirements
Python 3.6 or later,
markdown_generator library,
tqdm library,
asyncio library,
pathlib library
## Usage
To use this script, run it from the command line with a path to a folder as an argument. The script will generate documentation for all supported files in the folder and its subfolders.

---


# Symbols


## queue ![set](https://img.shields.io/badge/set-gray&style=flat)

- **Defined on lines:** 1–2
- **Symbol kind:** set

### Purpose
A set to store file paths that need documentation generated.

### Details
Not specified.

### Usage
Add file paths to the queue using `queue.add(element_path)`.

---

## LANGUAGES ![dict](https://img.shields.io/badge/dict-gray&style=flat)

- **Defined on lines:** 4–52
- **Symbol kind:** dict

### Purpose
A dictionary mapping file extensions to their corresponding programming languages.

### Details
The dictionary includes mappings for various programming languages and their respective file extensions.

### Usage
Use `LANGUAGES.get(suffix)` to get the language of a file based on its extension.

---

## ignored_languages ![list](https://img.shields.io/badge/list-gray&style=flat)

- **Defined on lines:** 54–56
- **Symbol kind:** list

### Purpose
A list of file extensions to be ignored by the script.

### Details
The list includes common file extensions that are not supported or should not be processed.

### Usage
Add file extensions to the `ignored_languages` list using `ignored_languages.append(extension)`.

---

## ignored_folders ![list](https://img.shields.io/badge/list-gray&style=flat)

- **Defined on lines:** 58–60
- **Symbol kind:** list

### Purpose
A list of folder names to be ignored by the script.

### Details
The list includes common folder names that are not supported or should not be processed.

### Usage
Add folder names to the `ignored_folders` list using `ignored_folders.append(folder)`.

---

## is_supported_language ![function](https://img.shields.io/badge/function-green&style=flat)

- **Defined on lines:** 62–78
- **Symbol kind:** function

### Purpose
Check if a file is supported by the script based on its extension.

### Details
The function checks if the file's extension is in the `LANGUAGES` dictionary and not in the `ignored_languages` list.

### Usage
Use `is_supported_language(file_path)` to determine if a file should be processed.

---

## is_allowed_folder ![function](https://img.shields.io/badge/function-green&style=flat)

- **Defined on lines:** 80–96
- **Symbol kind:** function

### Purpose
Check if a folder is allowed by the script based on its name and parent directories.

### Details
The function checks if the folder's name is in the `ignored_folders` list or if any of its parents are in the `ignored_folders` list.

### Usage
Use `is_allowed_folder(folder_path)` to determine if a folder should be processed.

---

## get_code_from_file ![function](https://img.shields.io/badge/function-green&style=flat)

- **Defined on lines:** 98–124
- **Symbol kind:** function

### Purpose
Read the content of a file and return it as a string.

### Details
The function opens a file in read mode and reads its contents. It handles exceptions to print an error message if the file cannot be read.

### Usage
Use `get_code_from_file(file_path)` to get the code from a file.

---

## generate_docs_for_file ![function](https://img.shields.io/badge/function-green&style=flat)

- **Defined on lines:** 126–150
- **Symbol kind:** function

### Purpose
Generate documentation for a single file using the `generate_markdown` function.

### Details
The function checks if the file exists, reads its content, and then calls `generate_markdown` to generate documentation.

### Usage
Use `generate_docs_for_file(file_path)` to generate documentation for a specific file.

---

## get_files_for_folder ![function](https://img.shields.io/badge/function-green&style=flat)

- **Defined on lines:** 152–204
- **Symbol kind:** function

### Purpose
Recursively get all files in a folder and its subfolders, filtering by supported languages.

### Details
The function uses `os.listdir` to list the contents of the folder. It checks each element to see if it is a file or directory and processes them accordingly.

### Usage
Use `get_files_for_folder(folder_path)` to get all files in a folder and its subfolders.

---

## get_files_for_path ![function](https://img.shields.io/badge/function-green&style=flat)

- **Defined on lines:** 206–238
- **Symbol kind:** function

### Purpose
Get all files in a path, filtering by supported languages and ignoring certain folders.

### Details
The function checks if the input is a file or directory. If it's a file, it checks if it is supported and adds it to the queue. If it's a directory, it recursively calls `get_files_for_folder` to process its contents.

### Usage
Use `get_files_for_path(path)` to get all files in a path.

---

## generate_docs ![function](https://img.shields.io/badge/function-green&style=flat)

- **Defined on lines:** 240–268
- **Symbol kind:** function

### Purpose
Generate documentation for all files in the queue using `generate_docs_for_file`.

### Details
The function creates a list of tasks to generate documentation for each file in the queue. It uses `asyncio.run` to execute these tasks concurrently and prints progress using `tqdm_asyncio.as_completed`.

### Usage
Use `generate_docs()` to generate documentation for all files in the queue.

---

## load_docgen_ignore ![function](https://img.shields.io/badge/function-green&style=flat)

- **Defined on lines:** 270–314
- **Symbol kind:** function

### Purpose
Load a .docgen_ignore file and add ignored languages and folders to the respective lists.

### Details
The function checks for a `.docgen_ignore` file in the specified folder. If found, it reads each line and adds any non-empty lines that end with a slash or start with a dot to the `ignored_folders` list or `ignored_languages` list, respectively.

### Usage
Use `load_docgen_ignore(folder)` to load an .docgen_ignore file and update the ignored lists.

---

## main ![function](https://img.shields.io/badge/function-green&style=flat)

- **Defined on lines:** 316–352
- **Symbol kind:** function

### Purpose
The main function to execute the script. It checks if a path is provided as an argument and runs `get_files_for_path` and `generate_docs`.

### Details
The function checks if the script was run with at least one argument (the path). If so, it calls `load_docgen_ignore`, `get_files_for_path`, and `generate_docs`. It also handles command-line usage instructions if no path is provided.

### Usage
Run the script from the command line with a path to a folder as an argument.

---