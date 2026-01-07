# **Documentation for `main.py`**
> _Generated on 2026-01-06 14:43:45_

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
This script is a tool for generating documentation from code files. It supports various programming languages and ignores certain files or folders.			
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
Python 3.7 or later,
markdown_generator library,
tqdm library,
asyncio library,
pathlib library
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
queue = set()
### Purpose
A set to store file paths that need documentation generated.

### Details
This set is used to keep track of all files that are eligible for documentation generation. It ensures that each file is processed only once.

### Usage
The queue is populated by the `get_files_for_path` function and then used in the `generate_docs` function to process each file.

### Limitations
- Files added to the queue may not be processed if they are ignored due to language or folder settings.

---

## LANGUAGES ![dict](https://img.shields.io/badge/dict-gray?style=flat)

- **Defined on lines:** 3–54
- **Symbol kind:** dict

### Definition
LANGUAGES = {
    ".py": "Python",
    ".pyw": "Python",
    ".pyi": "Python (type hints)",

    # Rust
    ".rs": "Rust",

    # JavaScript
    ".js": "JavaScript",
    ".mjs": "JavaScript (ES modules)",
    ".cjs": "JavaScript (CommonJS)",

    # TypeScript
    ".ts": "TypeScript",
    ".tsx": "TypeScript (React)",
    ".d.ts": "TypeScript (declarations)",

    # Go
    ".go": "Go",

    # Java
    ".java": "Java",
    ".jar": "Java (archive)",
    ".class": "Java (bytecode)",

    # C
    ".c": "C",
    ".h": "C/C++ header",

    # C++
    ".cpp": "C++",
    ".cc": "C++",
    ".cxx": "C++",
    ".hpp": "C++ header",
    ".hh": "C++ header",
    ".hxx": "C++ header",

    # C#
    ".cs": "C#",
    ".csproj": "C# project",

    # PHP
    ".php": "PHP",
    ".phtml": "PHP",

    # Ruby
    ".rb": "Ruby",
    ".erb": "Ruby (ERB templates)",
    ".rake": "Ruby (Rake)",

    # Web
    ".html": "HTML",
    ".htm": "HTML",
    ".css": "CSS",
    ".scss": "CSS (Sass)",
    ".sass": "CSS (Sass)",
    ".less": "CSS (Less)",

    # Shell
    ".sh": "Shell",
    ".bash": "Bash",
    ".zsh": "Zsh",

    # Other common languages
    ".kt": "Kotlin",
    ".kts": "Kotlin (script)",
    ".swift": "Swift",
    ".lua": "Lua",
    ".pl": "Perl",
    ".pm": "Perl module",
    ".dart": "Dart",
    ".r": "R",
    ".m": "Objective-C / MATLAB",
    ".mm": "Objective-C++",

    # Data / config / markup
    ".json": "JSON",
    ".yaml": "YAML",
    ".yml": "YAML",
    ".xml": "XML",
    ".toml": "TOML",
    ".ini": "INI",
    ".cfg": "Config",
    ".md": "Markdown",
    ".sql": "SQL"
}

### Purpose
A dictionary that maps file extensions to their corresponding programming languages.

### Details
This dictionary is used to determine the language of a given file based on its extension. It helps in identifying which functions or classes are available for documentation generation.

### Usage
The `is_supported_language` function uses this dictionary to check if a file should be processed.

### Limitations
- The dictionary may not cover all possible programming languages, and additional entries may need to be added as new languages are supported.

---

## ignored_languages ![list](https://img.shields.io/badge/list-gray?style=flat)

- **Defined on lines:** 56–57
- **Symbol kind:** list

### Definition
ignored_languages = []
### Purpose
A list to store file extensions that should be ignored during documentation generation.

### Details
This list is used to exclude certain files from being processed. It helps in maintaining a clean and organized project structure.

### Usage
The `is_supported_language` function uses this list to check if a file should be processed.

### Limitations
- Files added to the ignored_languages list may still be processed if they are not supported by any other language or folder settings.

---

## ignored_folders ![list](https://img.shields.io/badge/list-gray?style=flat)

- **Defined on lines:** 59–60
- **Symbol kind:** list

### Definition
ignored_folders = []
### Purpose
A list to store folder names that should be ignored during documentation generation.

### Details
This list is used to exclude certain folders from being processed. It helps in maintaining a clean and organized project structure.

### Usage
The `is_allowed_folder` function uses this list to check if a folder should be processed.

### Limitations
- Folders added to the ignored_folders list may still be processed if they are not supported by any other language or file settings.

---

## is_supported_language ![function](https://img.shields.io/badge/function-green?style=flat)

- **Defined on lines:** 62–75
- **Symbol kind:** function

### Definition
def is_supported_language(file_path: str) -> bool:
    path = Path(file_path)
    suffix = path.suffix
    if suffix in ignored_languages:
        return False
    
    return LANGUAGES.get(suffix) != None
### Purpose
A function to check if a file is supported for documentation generation.

### Details
This function checks if the file extension is in the `ignored_languages` list or not. If it is, the function returns False indicating that the file should be ignored. Otherwise, it checks if the file extension exists in the `LANGUAGES` dictionary and returns True if it does.

### Usage
The function is called by the `get_files_for_path` function to determine which files need documentation generation.

### Limitations
- The function may not handle all possible file extensions correctly, and additional entries may need to be added to the `LANGUAGES` dictionary as new languages are supported.

---

## is_allowed_folder ![function](https://img.shields.io/badge/function-green?style=flat)

- **Defined on lines:** 78–91
- **Symbol kind:** function

### Definition
def is_allowed_folder(folder_path: str) -> bool:
    folder = Path(folder_path)
    for ignored_folder in ignored_folders:
        if ignored_folder in folder.parents or folder.name == ignored_folder.name:
            return False
    return True
### Purpose
A function to check if a folder is allowed for documentation generation.

### Details
This function checks if the folder name exists in the `ignored_folders` list. If it does, the function returns False indicating that the folder should be ignored. Otherwise, it checks if any of the parent folders contain an entry from the `ignored_folders` list and returns True if they do not.

### Usage
The function is called by the `get_files_for_folder` function to determine which folders need documentation generation.

### Limitations
- The function may not handle all possible folder names correctly, and additional entries may need to be added to the `ignored_folders` list as new folders are supported.

---

## get_code_from_file ![function](https://img.shields.io/badge/function-green?style=flat)

- **Defined on lines:** 94–107
- **Symbol kind:** function

### Definition
def get_code_from_file(file_path: str) -> str:
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            code = f.read()
        return code
    except Exception as e:
        print(f"Error reading file {file_path}: {e}")
        return ""
### Purpose
A function to read the content of a file.

### Details
This function attempts to open and read the contents of a file specified by `file_path`. If successful, it returns the code as a string. If an error occurs during reading, it prints an error message and returns an empty string.

### Usage
The function is called by the `generate_docs_for_file` function to get the code for a given file.

### Limitations
- The function may not handle all possible errors correctly, such as permission issues or invalid file paths.

---

## generate_docs_for_file ![function](https://img.shields.io/badge/function-green?style=flat)

- **Defined on lines:** 109–124
- **Symbol kind:** function

### Definition
async def generate_docs_for_file(file_path):
    if not os.path.isfile(file_path):
        print("Not a file")
        return

    code = get_code_from_file(file_path)
    if code:
        await generate_markdown(file_path, code)
### Purpose
An asynchronous function to generate documentation for a given file.

### Details
This function first checks if the specified `file_path` is a valid file. If it is not, it prints an error message and returns. Otherwise, it reads the file content using the `get_code_from_file` function and generates documentation using the `generate_markdown` function if the code is available.

### Usage
The function is called by the `asyncio.run(get_files_for_path(path))` in the `main` function to process each file in the queue.

### Limitations
- The function may not handle all possible errors correctly, such as permission issues or invalid file paths.

---

## get_files_for_folder ![function](https://img.shields.io/badge/function-green?style=flat)

- **Defined on lines:** 126–153
- **Symbol kind:** function

### Definition
async def get_files_for_folder(folder_path):
    if not os.path.isdir(folder_path):
        print("Not a folder")
        return
    
    elements = os.listdir(folder_path)
    
    for element in tqdm(elements, desc=f"Getting files in {folder_path}", unit="item"):
        element_path = os.path.join(folder_path, element)

        if os.path.isfile(element_path):
            if is_supported_language(element_path):
                queue.add(element_path)
        elif os.path.isdir(element_path):
            if is_allowed_folder(element_path):
                await get_files_for_folder(element_path)
### Purpose
An asynchronous function to recursively search for files in a given folder.

### Details
This function first checks if the specified `folder_path` is a valid directory. If it is not, it prints an error message and returns. Otherwise, it lists all elements in the directory using `os.listdir`. It then iterates over each element, checking if it is a file or a folder. If it is a file, it checks if the file extension is supported by calling the `is_supported_language` function. If it is supported, the file path is added to the `queue`. If it is a folder, it checks if the folder name is allowed by calling the `is_allowed_folder` function. If the folder is allowed, the function calls itself recursively to process the subfolder.

### Usage
The function is called by the `asyncio.run(get_files_for_path(path))` in the `main` function to populate the queue with all eligible files and folders.

### Limitations
- The function may not handle all possible errors correctly, such as permission issues or invalid folder paths.

---

## get_files_for_path ![function](https://img.shields.io/badge/function-green?style=flat)

- **Defined on lines:** 155–172
- **Symbol kind:** function

### Definition
async def get_files_for_path(path):
    if os.path.isdir(path):
        load_docgen_ignore(path)
        await get_files_for_folder(path)
    elif os.path.isfile(path):
        if is_supported_language(path):
            queue.add(path)
### Purpose
An asynchronous function to recursively search for files in a given path.

### Details
This function first checks if the specified `path` is a valid directory. If it is, it loads any `.docgen_ignore` file and then calls the `get_files_for_folder` function to process all files and folders within the directory. If the path is a file, it checks if the file extension is supported by calling the `is_supported_language` function. If it is supported, the file path is added to the `queue`. This function is called by the `main` function to populate the queue with all eligible files.

### Usage
The function is called by the `main` function to initialize the queue with all eligible files and folders.

### Limitations
- The function may not handle all possible errors correctly, such as permission issues or invalid paths.

---

## generate_docs ![function](https://img.shields.io/badge/function-green?style=flat)

- **Defined on lines:** 174–189
- **Symbol kind:** function

### Definition
async def generate_docs():
    tasks = [generate_docs_for_file(path) for path in queue]

    for task in tqdm_asyncio.as_completed(tasks, total=len(tasks), desc="Processing files", unit="file"):
        await task
### Purpose
An asynchronous function to generate documentation for all files in the queue.

### Details
This function creates a list of tasks by calling `generate_docs_for_file` for each file path in the `queue`. It then uses `asyncio.as_completed` to process each task asynchronously. The progress is displayed using `tqdm_asyncio`, and the function waits for all tasks to complete before returning.

### Usage
The function is called by the `main` function to generate documentation for all files in the queue.

### Limitations
- The function may not handle all possible errors correctly, such as permission issues or invalid file paths.

---

## load_docgen_ignore ![function](https://img.shields.io/badge/function-green?style=flat)

- **Defined on lines:** 192–208
- **Symbol kind:** function

### Definition
def load_docgen_ignore(folder: str):
    folder_path = Path(folder)
    path = folder_path / ".docgen_ignore"
    if not os.path.isfile(path):
        return
    with open(path) as f:
        for line in f:
            line = line.strip()
            if line.endswith("/"):
                ignored_folders.append(Path(line.strip()))
            elif line.startswith("."):
                ignored_languages.append(line.strip())
### Purpose
A function to load `.docgen_ignore` files and update the `ignored_languages` and `ignored_folders` lists.

### Details
This function first constructs the path to the `.docgen_ignore` file in the specified `folder`. If the file does not exist, it returns. Otherwise, it opens the file and reads each line. For each line, it checks if the line ends with a slash (`/`). If it does, it adds the folder name (excluding the trailing slash) to the `ignored_folders` list. If the line starts with a dot (`.`), it adds the language extension (excluding the leading dot) to the `ignored_languages` list.

### Usage
The function is called by the `get_files_for_path` function to load any `.docgen_ignore` files and update the queue accordingly.

### Limitations
- The function may not handle all possible errors correctly, such as permission issues or invalid file paths.

---

## main ![function](https://img.shields.io/badge/function-green?style=flat)

- **Defined on lines:** 210–235
- **Symbol kind:** function

### Definition
def main():
    if len(sys.argv) >= 2:
        path = sys.argv[1]
        asyncio.run(get_files_for_path(path))
        asyncio.run(generate_docs())
        print("\n\nGenerated docs!")
    else:
        print("Usage: python main.py path_to_folder")
### Purpose
The entry point of the script.

### Details
This function checks if a command-line argument is provided. If it is, it calls `get_files_for_path` and `generate_docs` asynchronously to process all eligible files and generate documentation. If no argument is provided, it prints usage instructions.

### Usage
The script should be run from the terminal with the path to the folder containing the code as an argument.

### Limitations
- The function may not handle all possible errors correctly, such as invalid command-line arguments or permission issues.

---