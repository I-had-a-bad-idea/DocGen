# **Documentation for `main.py`**
> _Generated on 2026-01-06 14:19:59_

> _Generated with [DocGen](https://github.com/I-had-a-bad-idea/DocGen), may include wrong information!_



# Table of Contents

- [queue ![set](https://img.shields.io/badge/set-gray?style=flat)](#queue-set)
- [LANGUAGES ![dict](https://img.shields.io/badge/dict-gray?style=flat)](#languages-dict)
- [ignored_languages ![list](https://img.shields.io/badge/list-gray?style=flat)](#ignored_languages-list)
- [ignored_folders ![list](https://img.shields.io/badge/list-gray?style=flat)](#ignored_folders-list)
- [is_supported_language ![function](https://img.shields.io/badge/function-green?style=flat)](#is_supported_language-function)
- [is_allowed_folder ![function](https://img.shields.io/badge/function-green?style=flat)](#is_allowed_folder-function)
- [get_code_from_file ![function](https://img.shields.io/badge/function-green?style=flat)](#get_code_from_file-function)
- [generate_docs_for_file ![function](https://img.shields.io/badge/function-green?style=flat)](#generate_docs_for_file-function)
- [get_files_for_folder ![function](https://img.shields.io/badge/function-green?style=flat)](#get_files_for_folder-function)
- [get_files_for_path ![function](https://img.shields.io/badge/function-green?style=flat)](#get_files_for_path-function)
- [generate_docs ![function](https://img.shields.io/badge/function-green?style=flat)](#generate_docs-function)
- [load_docgen_ignore ![function](https://img.shields.io/badge/function-green?style=flat)](#load_docgen_ignore-function)
- [main ![function](https://img.shields.io/badge/function-green?style=flat)](#main-function)

---

# Overview
This script is a tool for generating documentation from source code files. It supports various programming languages and ignores certain files or directories.			
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
Python 3.7+
## Usage
To use this script, run the following command in your terminal:

python main.py path_to_folder

---


# Symbols


## queue ![set](https://img.shields.io/badge/set-gray?style=flat)

- **Defined on lines:** 1–2
- **Symbol kind:** set

### Purpose
A set to store file paths that need documentation generation.

### Details
Not specified.

### Usage
Add file paths to the queue using `queue.add(element_path)` when a supported language file is found.

---

## LANGUAGES ![dict](https://img.shields.io/badge/dict-gray?style=flat)

- **Defined on lines:** 4–60
- **Symbol kind:** dict

### Purpose
A dictionary mapping file extensions to their corresponding programming languages.

### Details
The keys are file extensions (e.g., ".py", ".js") and the values are language names (e.g., "Python").

### Usage
Check if a file is supported by calling `is_supported_language(file_path)` with the file path as an argument.

---

## ignored_languages ![list](https://img.shields.io/badge/list-gray?style=flat)

- **Defined on lines:** 62–63
- **Symbol kind:** list

### Purpose
A list of file extensions to ignore during documentation generation.

### Details
Not specified.

### Usage
Add file extensions to the ignored_languages list using `ignored_languages.append(extension)` when a language is not supported or should be ignored.

---

## ignored_folders ![list](https://img.shields.io/badge/list-gray?style=flat)

- **Defined on lines:** 65–67
- **Symbol kind:** list

### Purpose
A list of folder names to ignore during documentation generation.

### Details
Not specified.

### Usage
Add folder names to the ignored_folders list using `ignored_folders.append(folder)` when a folder should be ignored.

---

## is_supported_language ![function](https://img.shields.io/badge/function-green?style=flat)

- **Defined on lines:** 70–82
- **Symbol kind:** function

### Purpose
Check if a file is supported by the script based on its extension.

### Details
The function takes a file path as an argument and returns `True` if the language is supported, otherwise `False`.

### Usage
Use this function to determine if a file should be processed by calling `is_supported_language(file_path)` before processing it.

---

## is_allowed_folder ![function](https://img.shields.io/badge/function-green?style=flat)

- **Defined on lines:** 85–97
- **Symbol kind:** function

### Purpose
Check if a folder is allowed for documentation generation based on its name and parent directories.

### Details
The function takes a folder path as an argument and returns `True` if the folder is allowed, otherwise `False`.

### Usage
Use this function to determine if a folder should be processed by calling `is_allowed_folder(folder_path)` before processing it.

---

## get_code_from_file ![function](https://img.shields.io/badge/function-green?style=flat)

- **Defined on lines:** 100–123
- **Symbol kind:** function

### Purpose
Read the content of a file and return it as a string.

### Details
The function takes a file path as an argument and returns the file's contents. It handles exceptions to print error messages if reading fails.

### Usage
Use this function to read the code from a file by calling `get_code_from_file(file_path)` before processing it.

---

## generate_docs_for_file ![function](https://img.shields.io/badge/function-green?style=flat)

- **Defined on lines:** 126–148
- **Symbol kind:** function

### Purpose
Generate documentation for a single file by calling `generate_markdown`.

### Details
The function takes a file path as an argument, reads the code using `get_code_from_file`, and then calls `generate_markdown` to generate documentation.

### Usage
Use this function to process a single file by calling `generate_docs_for_file(file_path)` when processing files in a queue.

---

## get_files_for_folder ![function](https://img.shields.io/badge/function-green?style=flat)

- **Defined on lines:** 151–204
- **Symbol kind:** function

### Purpose
Recursively search for files in a folder and add them to the queue if they are supported.

### Details
The function takes a folder path as an argument, lists all elements in the folder using `os.listdir`, and processes each element. It uses `tqdm` for progress tracking.

### Usage
Use this function to process files in a folder by calling `get_files_for_folder(folder_path)` when processing folders in a queue.

---

## get_files_for_path ![function](https://img.shields.io/badge/function-green?style=flat)

- **Defined on lines:** 207–235
- **Symbol kind:** function

### Purpose
Recursively search for files in a path and add them to the queue if they are supported.

### Details
The function takes a path as an argument, checks if it is a directory or file using `os.path.isdir` and `os.path.isfile`, and processes it accordingly. It uses `tqdm` for progress tracking.

### Usage
Use this function to process files in a path by calling `get_files_for_path(path)` when processing paths in a queue.

---

## generate_docs ![function](https://img.shields.io/badge/function-green?style=flat)

- **Defined on lines:** 238–259
- **Symbol kind:** function

### Purpose
Generate documentation for all files in the queue using `tqdm_asyncio.as_completed`.

### Details
The function creates a list of tasks to process each file in the queue and uses `asyncio.run` to execute them. It uses `tqdm_asyncio` for progress tracking.

### Usage
Use this function to generate documentation by calling `generate_docs()` after processing files in a queue.

---

## load_docgen_ignore ![function](https://img.shields.io/badge/function-green?style=flat)

- **Defined on lines:** 262–287
- **Symbol kind:** function

### Purpose
Load the .docgen_ignore file from a folder and add ignored languages and folders to the respective lists.

### Details
The function takes a folder path as an argument, checks for the existence of `.docgen_ignore`, reads it line by line, and adds ignored languages and folders to their respective lists.

### Usage
Use this function to load ignore settings from a file by calling `load_docgen_ignore(folder)` before processing files in a queue.

---

## main ![function](https://img.shields.io/badge/function-green?style=flat)

- **Defined on lines:** 290–315
- **Symbol kind:** function

### Purpose
The main function to run the script. It checks if a path is provided as an argument, processes files in the folder using `get_files_for_path`, generates documentation using `generate_docs`, and prints a success message.

### Details
The function takes command-line arguments, calls `load_docgen_ignore` if a path is provided, processes files in the folder, generates documentation, and prints a success message.

### Usage
Run the script by calling `python main.py path_to_folder` to generate documentation for all supported files in the specified folder.

---