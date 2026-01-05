# **Documentation for `main.py`**
> _Generated on 2026-01-05 12:51:22_

> _Generated with [DocGen](https://github.com/I-had-a-bad-idea/DocGen), may include wrong information!_



# Table of Contents

- [queue ![set](https://img.shields.io/badge/set-gray?style=flat)](#queue)
- [LANGUAGES ![dict](https://img.shields.io/badge/dict-gray?style=flat)](#languages)
- [ignored_languages ![list](https://img.shields.io/badge/list-gray?style=flat)](#ignored_languages)
- [ignored_folders ![list](https://img.shields.io/badge/list-gray?style=flat)](#ignored_folders)
- [is_supported_language ![function](https://img.shields.io/badge/function-green?style=flat)](#is_supported_language)
- [is_allowed_folder ![function](https://img.shields.io/badge/function-green?style=flat)](#is_allowed_folder)
- [get_code_from_file ![function](https://img.shields.io/badge/function-green?style=flat)](#get_code_from_file)
- [generate_docs_for_file ![function](https://img.shields.io/badge/function-green?style=flat)](#generate_docs_for_file)
- [get_files_for_folder ![function](https://img.shields.io/badge/function-green?style=flat)](#get_files_for_folder)
- [get_files_for_path ![function](https://img.shields.io/badge/function-green?style=flat)](#get_files_for_path)
- [generate_docs ![function](https://img.shields.io/badge/function-green?style=flat)](#generate_docs)
- [load_docgen_ignore ![function](https://img.shields.io/badge/function-green?style=flat)](#load_docgen_ignore)
- [main ![function](https://img.shields.io/badge/function-green?style=flat)](#main)

---

# Overview
A script to generate documentation for various programming languages.			
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
Python 3.6+
## Usage
Run the script with a folder path as an argument to generate documentation for all supported files within that folder and its subfolders.

---


# Symbols


## queue ![set](https://img.shields.io/badge/set-gray?style=flat)

- **Defined on lines:** 1–2
- **Symbol kind:** set

### Purpose
A set to store file paths for processing.

### Details
Not specified.

### Usage
Add file paths to the queue using `queue.add(element_path)`.

---

## LANGUAGES ![dict](https://img.shields.io/badge/dict-gray?style=flat)

- **Defined on lines:** 4–57
- **Symbol kind:** dict

### Purpose
A dictionary mapping file extensions to their corresponding programming languages.

### Details
Not specified.

### Usage
Check if a file is supported by looking up its extension in `LANGUAGES`.

---

## ignored_languages ![list](https://img.shields.io/badge/list-gray?style=flat)

- **Defined on lines:** 59–60
- **Symbol kind:** list

### Purpose
A list of file extensions to ignore.

### Details
Not specified.

### Usage
Add file extensions to the `ignored_languages` list to exclude them from processing.

---

## ignored_folders ![list](https://img.shields.io/badge/list-gray?style=flat)

- **Defined on lines:** 62–63
- **Symbol kind:** list

### Purpose
A list of folder names to ignore.

### Details
Not specified.

### Usage
Add folder names to the `ignored_folders` list to exclude them from processing.

---

## is_supported_language ![function](https://img.shields.io/badge/function-green?style=flat)

- **Defined on lines:** 65–82
- **Symbol kind:** function

### Purpose
Check if a file is supported by its extension.

### Details
Returns `True` if the file extension is in `LANGUAGES`, otherwise returns `False`.

### Usage
Use this function to determine if a file should be processed.

---

## is_allowed_folder ![function](https://img.shields.io/badge/function-green?style=flat)

- **Defined on lines:** 84–102
- **Symbol kind:** function

### Purpose
Check if a folder is allowed to be processed based on its name and parent directories.

### Details
Returns `True` if the folder is not in `ignored_folders`, otherwise returns `False`.

### Usage
Use this function to determine if a folder should be processed.

---

## get_code_from_file ![function](https://img.shields.io/badge/function-green?style=flat)

- **Defined on lines:** 104–123
- **Symbol kind:** function

### Purpose
Read the content of a file and return it as a string.

### Details
Returns an empty string if the file cannot be read or if there is an error.

### Usage
Use this function to get the code from a file path.

---

## generate_docs_for_file ![function](https://img.shields.io/badge/function-green?style=flat)

- **Defined on lines:** 125–143
- **Symbol kind:** function

### Purpose
Generate documentation for a single file.

### Details
Reads the code from the file and calls `generate_markdown` to generate documentation.

### Usage
Use this function to process a single file.

---

## get_files_for_folder ![function](https://img.shields.io/badge/function-green?style=flat)

- **Defined on lines:** 145–203
- **Symbol kind:** function

### Purpose
Recursively get all files in a folder and its subfolders.

### Details
Uses `tqdm` to display progress and checks if each file is supported and allowed before adding it to the queue.

### Usage
Use this function to process all files in a folder.

---

## get_files_for_path ![function](https://img.shields.io/badge/function-green?style=flat)

- **Defined on lines:** 205–231
- **Symbol kind:** function

### Purpose
Get all files from a given path, which can be a folder or a file.

### Details
If the path is a directory, it calls `load_docgen_ignore` and then processes the folder. If the path is a file, it checks if the file is supported and adds it to the queue.

### Usage
Use this function to process all files in a given path.

---

## generate_docs ![function](https://img.shields.io/badge/function-green?style=flat)

- **Defined on lines:** 233–251
- **Symbol kind:** function

### Purpose
Generate documentation for all files in the queue.

### Details
Creates tasks to process each file and uses `tqdm_asyncio` to display progress.

### Usage
Use this function to generate documentation for all files.

---

## load_docgen_ignore ![function](https://img.shields.io/badge/function-green?style=flat)

- **Defined on lines:** 253–281
- **Symbol kind:** function

### Purpose
Load the `.docgen_ignore` file and add ignored languages and folders to their respective lists.

### Details
Reads the `.docgen_ignore` file line by line, adding each line to `ignored_folders` if it ends with a slash or to `ignored_languages` if it does not start with a dot.

### Usage
Use this function to load ignored files and folders from a configuration file.

---

## main ![function](https://img.shields.io/badge/function-green?style=flat)

- **Defined on lines:** 283–306
- **Symbol kind:** function

### Purpose
The main function to run the script.

### Details
Checks if a path is provided as an argument, loads the `.docgen_ignore` file, processes all files in the folder and its subfolders, and generates documentation for each file.

### Usage
Run this function to start processing files.

---