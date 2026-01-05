# **Documentation for `main.py`**
> _Generated on 2026-01-05 12:16:07_

> _Generated with [DocGen](https://github.com/I-had-a-bad-idea/DocGen), may include wrong information!_



# Table of Contents

- [queue (set)](#queue-set)
- [LANGUAGES (dict)](#languages-dict)
- [ignored_languages (list)](#ignored_languages-list)
- [ignored_folders (list)](#ignored_folders-list)
- [is_supported_language (function)](#is_supported_language-function)
- [is_allowed_folder (function)](#is_allowed_folder-function)
- [get_code_from_file (function)](#get_code_from_file-function)
- [generate_docs_for_file (function)](#generate_docs_for_file-function)
- [get_files_for_folder (function)](#get_files_for_folder-function)
- [get_files_for_path (function)](#get_files_for_path-function)
- [generate_docs (function)](#generate_docs-function)
- [load_docgen_ignore (function)](#load_docgen_ignore-function)
- [main (function)](#main-function)

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
Python installed,
markdown_generator module installed,
tqdm and tqdm_asyncio modules installed,
asyncio library installed
## Usage
Run the script with a folder path as an argument to generate documentation for all supported files in that folder and its subfolders.

---


# Symbols


## queue (set)

- **Defined on lines:** 1–2
- **Symbol kind:** set

### Purpose
A set to store file paths for processing.

### Details
Not specified.

### Usage
Add file paths to the queue using `queue.add(element_path)`.




## LANGUAGES (dict)

- **Defined on lines:** 4–50
- **Symbol kind:** dict

### Purpose
A dictionary mapping file extensions to their corresponding programming languages.

### Details
Contains mappings for various programming languages and their respective file extensions.

### Usage
Use `LANGUAGES.get(suffix)` to get the language of a file based on its extension.




## ignored_languages (list)

- **Defined on lines:** 52–53
- **Symbol kind:** list

### Purpose
A list to store ignored programming languages.

### Details
Not specified.

### Usage
Add language extensions to the `ignored_languages` list using `ignored_languages.append(extension)`.




## ignored_folders (list)

- **Defined on lines:** 55–56
- **Symbol kind:** list

### Purpose
A list to store ignored folders.

### Details
Not specified.

### Usage
Add folder paths to the `ignored_folders` list using `ignored_folders.append(folder)`.




## is_supported_language (function)

- **Defined on lines:** 58–71
- **Symbol kind:** function

### Purpose
Check if a file is supported based on its extension and language.

### Details
Returns `True` if the file is supported, otherwise `False`.

### Usage
Use `is_supported_language(file_path)` to determine if a file should be processed.




## is_allowed_folder (function)

- **Defined on lines:** 73–86
- **Symbol kind:** function

### Purpose
Check if a folder is allowed based on its name and parent directories.

### Details
Returns `True` if the folder is allowed, otherwise `False`.

### Usage
Use `is_allowed_folder(folder_path)` to determine if a folder should be processed.




## get_code_from_file (function)

- **Defined on lines:** 88–105
- **Symbol kind:** function

### Purpose
Read the content of a file and return it as a string.

### Details
Returns the code from the specified file path or an empty string if an error occurs.

### Usage
Use `get_code_from_file(file_path)` to read the contents of a file.




## generate_docs_for_file (function)

- **Defined on lines:** 107–124
- **Symbol kind:** function

### Purpose
Generate documentation for a single file.

### Details
Reads the code from the file and calls `generate_markdown` to generate documentation.

### Usage
Use `generate_docs_for_file(file_path)` to generate documentation for a specific file.




## get_files_for_folder (function)

- **Defined on lines:** 126–153
- **Symbol kind:** function

### Purpose
Recursively get all files in a folder and its subfolders.

### Details
Lists all files in the specified folder and its subfolders, filtering based on supported languages and allowed folders.

### Usage
Use `get_files_for_folder(folder_path)` to recursively find all files in a folder.




## get_files_for_path (function)

- **Defined on lines:** 155–172
- **Symbol kind:** function

### Purpose
Get all files for a given path, which can be a folder or a file.

### Details
Checks if the path is a file or a directory and processes it accordingly.

### Usage
Use `get_files_for_path(path)` to get all files in a specified location.




## generate_docs (function)

- **Defined on lines:** 174–203
- **Symbol kind:** function

### Purpose
Generate documentation for all files in the queue.

### Details
Runs `generate_docs_for_file` for each file in the queue and processes them asynchronously.

### Usage
Use `generate_docs()` to generate documentation for all files in the queue.




## load_docgen_ignore (function)

- **Defined on lines:** 205–234
- **Symbol kind:** function

### Purpose
Load ignored languages and folders from a .docgen_ignore file.

### Details
Reads the .docgen_ignore file in the specified folder and adds any ignored languages or folders to their respective lists.

### Usage
Use `load_docgen_ignore(folder)` to load ignored files and folders from a specific directory.




## main (function)

- **Defined on lines:** 236–258
- **Symbol kind:** function

### Purpose
The main function to run the script.

### Details
Checks if a path is provided as an argument, loads ignored files and folders, processes all files in the specified folder, and generates documentation for them.

### Usage
Run `main()` to execute the script.


