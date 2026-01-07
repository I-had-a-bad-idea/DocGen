# **Documentation for `main.py`**
> _Generated on 2026-01-07 15:39:33_

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
This script is a tool for generating documentation from code files. It supports various programming languages and ignores certain file types or folders.			
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
To use this script, run the following command in your terminal:

python main.py path_to_folder

This will generate documentation for all supported files in the specified folder and its subfolders.

---


# Symbols


## queue ![set](https://img.shields.io/badge/set-gray?style=flat)

- **Defined on line:** 1
- **Symbol kind:** set

### Definition
```Python
queue = set()
```
### Purpose
A set to store file paths that need documentation generated.

### Details
This set is used to keep track of all files that are eligible for documentation generation. It ensures that each file is processed only once.

### Usage
The queue is populated by the `get_files_for_folder` function and then used in the `generate_docs` function to process each file.

### Limitations
- Files added to the queue may not be processed if they are ignored or unsupported.

---

## LANGUAGES ![dict](https://img.shields.io/badge/dict-gray?style=flat)

- **Defined on lines:** 3–54
- **Symbol kind:** dict

### Definition
```Python
LANGUAGES = {
```
### Purpose
A dictionary that maps file extensions to their corresponding programming languages.

### Details
This dictionary is used to determine the language of a given file based on its extension. It helps in identifying which functions or classes are available for documentation generation.

### Usage
The `is_supported_language` function uses this dictionary to check if a file should be processed.

### Limitations
- The dictionary may not cover all possible programming languages, and additional entries can be added as needed.

---

## ignored_languages ![list](https://img.shields.io/badge/list-gray?style=flat)

- **Defined on lines:** 56–57
- **Symbol kind:** list

### Definition
```Python
ignored_languages = []
```
### Purpose
A list to store file extensions that should be ignored during documentation generation.

### Details
This list is used to exclude certain files or folders from being processed. It helps in maintaining a clean and organized project structure.

### Usage
The `is_supported_language` function checks if a file extension is in the `ignored_languages` list before processing it.

### Limitations
- Files added to the `ignored_languages` list may still be processed if they are not ignored by other means.

---

## ignored_folders ![list](https://img.shields.io/badge/list-gray?style=flat)

- **Defined on lines:** 59–60
- **Symbol kind:** list

### Definition
```Python
ignored_folders = []
```
### Purpose
A list to store folder names that should be ignored during documentation generation.

### Details
This list is used to exclude certain folders from being processed. It helps in maintaining a clean and organized project structure.

### Usage
The `is_allowed_folder` function checks if a folder name is in the `ignored_folders` list before processing it.

### Limitations
- Folders added to the `ignored_folders` list may still be processed if they are not ignored by other means.

---

## is_supported_language ![function](https://img.shields.io/badge/function-green?style=flat)

- **Defined on lines:** 62–75
- **Symbol kind:** function

### Definition
```Python
def is_supported_language(file_path: str) -> bool:
```
### Purpose
A function to check if a file is supported for documentation generation.

### Details
This function checks if the file extension of a given file path is in the `ignored_languages` list or not. If it is, the function returns False, indicating that the file should be ignored. Otherwise, it checks if the file extension exists in the `LANGUAGES` dictionary and returns True if it does.

### Usage
The function is used to determine if a file should be processed by the `get_files_for_folder` function.

### Limitations
- The function may not cover all possible programming languages, and additional entries can be added as needed.

---

## is_allowed_folder ![function](https://img.shields.io/badge/function-green?style=flat)

- **Defined on lines:** 77–90
- **Symbol kind:** function

### Definition
```Python
def is_allowed_folder(folder_path: str) -> bool:
```
### Purpose
A function to check if a folder is allowed for documentation generation.

### Details
This function checks if the name of a given folder path is in the `ignored_folders` list. If it is, the function returns False, indicating that the folder should be ignored. Otherwise, it checks if any parent directory of the folder matches an entry in the `ignored_folders` list and returns True if it does.

### Usage
The function is used to determine if a folder should be processed by the `get_files_for_folder` function.

### Limitations
- The function may not cover all possible folder names, and additional entries can be added as needed.

---

## get_code_from_file ![function](https://img.shields.io/badge/function-green?style=flat)

- **Defined on lines:** 92–105
- **Symbol kind:** function

### Definition
```Python
def get_code_from_file(file_path: str) -> str:
```
### Purpose
A function to read the content of a file.

### Details
This function attempts to open and read the content of a file specified by its path. If successful, it returns the content as a string. If an error occurs during the reading process, it prints an error message and returns an empty string.

### Usage
The function is used by the `generate_docs_for_file` function to get the code from a file before generating documentation for it.

### Limitations
- The function may not handle all possible errors, such as permission issues or invalid file paths.

---

## generate_docs_for_file ![function](https://img.shields.io/badge/function-green?style=flat)

- **Defined on lines:** 107–128
- **Symbol kind:** function

### Definition
```Python
async def generate_docs_for_file(file_path):
```
### Purpose
An asynchronous function to generate documentation for a single file.

### Details
This function checks if the given file path is a valid file. If it is, it reads the content of the file using the `get_code_from_file` function and then generates documentation for the code using the `generate_markdown` function. The `generate_markdown` function is an asynchronous function that handles the actual generation of documentation.

### Usage
The function is called by the `generate_docs` function to process each file in the queue.

### Limitations
- The function may not handle all possible errors, such as permission issues or invalid file paths.

---

## get_files_for_folder ![function](https://img.shields.io/badge/function-green?style=flat)

- **Defined on lines:** 130–164
- **Symbol kind:** function

### Definition
```Python
async def get_files_for_folder(folder_path):
```
### Purpose
An asynchronous function to recursively search for files in a folder and its subfolders.

### Details
This function checks if the given folder path is a valid directory. If it is, it lists all elements in the directory using `os.listdir`. It then iterates over each element, checking if it is a file or a directory. If it is a file, it checks if the file extension is supported by calling the `is_supported_language` function. If it is supported, the file path is added to the queue. If it is a directory, it checks if the folder name is allowed by calling the `is_allowed_folder` function. If it is allowed, the function recursively calls itself to search for files in the subdirectory.

### Usage
The function is called by the `get_files_for_path` function to process each folder in the queue.

### Limitations
- The function may not handle all possible errors, such as permission issues or invalid file paths.

---

## get_files_for_path ![function](https://img.shields.io/badge/function-green?style=flat)

- **Defined on lines:** 166–203
- **Symbol kind:** function

### Definition
```Python
async def get_files_for_path(path):
```
### Purpose
An asynchronous function to recursively search for files in a path.

### Details
This function checks if the given path is a valid directory or file. If it is a directory, it calls the `load_docgen_ignore` function to load any `.docgen_ignore` file and then calls the `get_files_for_folder` function to process all files in the directory and its subdirectories. If it is a file, it checks if the file extension is supported by calling the `is_supported_language` function. If it is supported, the file path is added to the queue.

### Usage
The function is called by the `main` function to process all files in the specified folder and its subfolders.

### Limitations
- The function may not handle all possible errors, such as permission issues or invalid file paths.

---

## generate_docs ![function](https://img.shields.io/badge/function-green?style=flat)

- **Defined on lines:** 205–218
- **Symbol kind:** function

### Definition
```Python
async def generate_docs():
```
### Purpose
An asynchronous function to generate documentation for all files in the queue.

### Details
This function creates a list of tasks by calling the `generate_docs_for_file` function for each file path in the queue. It then uses `tqdm_asyncio.as_completed` to asynchronously wait for all tasks to complete and print progress information as they are completed.

### Usage
The function is called by the `main` function to generate documentation for all files in the specified folder and its subfolders.

### Limitations
- The function may not handle all possible errors, such as permission issues or invalid file paths.

---

## load_docgen_ignore ![function](https://img.shields.io/badge/function-green?style=flat)

- **Defined on lines:** 220–243
- **Symbol kind:** function

### Definition
```Python
def load_docgen_ignore(folder: str):
```
### Purpose
A function to load `.docgen_ignore` files and add entries to the `ignored_folders` and `ignored_languages` lists.

### Details
This function checks if a `.docgen_ignore` file exists in the specified folder. If it does, it reads the file line by line and processes each line. If the line ends with a slash (`/`), it adds the directory path to the `ignored_folders` list. If the line starts with a dot (`.`), it adds the language extension to the `ignored_languages` list.

### Usage
The function is called by the `get_files_for_path` function to load any `.docgen_ignore` files and update the `ignored_folders` and `ignored_languages` lists.

### Limitations
- The function may not handle all possible errors, such as permission issues or invalid file paths.

---

## main ![function](https://img.shields.io/badge/function-green?style=flat)

- **Defined on lines:** 245–270
- **Symbol kind:** function

### Definition
```Python
def main():
```
### Purpose
The entry point of the script.

### Details
This function checks if a command-line argument is provided. If it is, it calls the `get_files_for_path` and `generate_docs` functions asynchronously to process all files in the specified folder and its subfolders and generate documentation for them. If no command-line argument is provided, it prints usage information.

### Usage
To run the script, execute the following command in your terminal:

python main.py path_to_folder

### Limitations
- The function may not handle all possible errors, such as invalid command-line arguments or permission issues.

---