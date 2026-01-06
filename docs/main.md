# **Documentation for `main.py`**
> _Generated on 2026-01-06 14:37:44_

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
Python installed,
markdown_generator module installed,
tqdm and tqdm_asyncio modules installed,
asyncio library installed
## Usage
To use this script, run it from the command line with a folder path as an argument. For example:

python main.py /path/to/folder

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
Not specified.

### Usage
Used in the `generate_docs` function to keep track of files to process.

---

## LANGUAGES ![dict](https://img.shields.io/badge/dict-gray?style=flat)

- **Defined on lines:** 3–45
- **Symbol kind:** dict

### Definition
LANGUAGES = {
    # Python
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
A dictionary mapping file extensions to their corresponding programming languages.

### Details
Not specified.

### Usage
Used in the `is_supported_language` function to determine if a file is supported.

---

## ignored_languages ![list](https://img.shields.io/badge/list-gray?style=flat)

- **Defined on lines:** 47–48
- **Symbol kind:** list

### Definition
ignored_languages = []
### Purpose
A list of file extensions to ignore.

### Details
Not specified.

### Usage
Used in the `is_supported_language` function to determine if a file is supported.

---

## ignored_folders ![list](https://img.shields.io/badge/list-gray?style=flat)

- **Defined on lines:** 49–50
- **Symbol kind:** list

### Definition
ignored_folders = []
### Purpose
A list of folder names to ignore.

### Details
Not specified.

### Usage
Used in the `is_allowed_folder` function to determine if a folder is allowed.

---

## is_supported_language ![function](https://img.shields.io/badge/function-green?style=flat)

- **Defined on lines:** 52–61
- **Symbol kind:** function

### Definition
def is_supported_language(file_path: str) -> bool:
    path = Path(file_path)
    suffix = path.suffix
    if suffix in ignored_languages:
        return False
    
    return LANGUAGES.get(suffix) != None
### Purpose
Checks if a file is supported based on its extension.

### Details
Not specified.

### Usage
Used in the `get_files_for_folder` function to filter files by language.

---

## is_allowed_folder ![function](https://img.shields.io/badge/function-green?style=flat)

- **Defined on lines:** 63–72
- **Symbol kind:** function

### Definition
def is_allowed_folder(folder_path: str) -> bool:
    folder = Path(folder_path)
    for ignored_folder in ignored_folders:
        if ignored_folder in folder.parents or folder.name == ignored_folder.name:
            return False
    return True
### Purpose
Checks if a folder is allowed based on its name and parent folders.

### Details
Not specified.

### Usage
Used in the `get_files_for_folder` function to filter folders by name and location.

---

## get_code_from_file ![function](https://img.shields.io/badge/function-green?style=flat)

- **Defined on lines:** 74–85
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
Reads the content of a file.

### Details
Not specified.

### Usage
Used in the `generate_docs_for_file` function to get the code from a file.

---

## generate_docs_for_file ![function](https://img.shields.io/badge/function-green?style=flat)

- **Defined on lines:** 87–102
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
Generates documentation for a single file.

### Details
Not specified.

### Usage
Used in the `generate_docs` function to process each file in the queue.

---

## get_files_for_folder ![function](https://img.shields.io/badge/function-green?style=flat)

- **Defined on lines:** 104–132
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
Recursively retrieves files from a folder and its subfolders.

### Details
Not specified.

### Usage
Used in the `get_files_for_path` function to find all supported files in a directory.

---

## get_files_for_path ![function](https://img.shields.io/badge/function-green?style=flat)

- **Defined on lines:** 134–150
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
Recursively retrieves files from a path, including subdirectories.

### Details
Not specified.

### Usage
Used in the `main` function to start processing files.

---

## generate_docs ![function](https://img.shields.io/badge/function-green?style=flat)

- **Defined on lines:** 152–160
- **Symbol kind:** function

### Definition
async def generate_docs():
    tasks = [generate_docs_for_file(path) for path in queue]

    for task in tqdm_asyncio.as_completed(tasks, total=len(tasks), desc="Processing files", unit="file"):
        await task
### Purpose
Asynchronously processes all files in the queue.

### Details
Not specified.

### Usage
Used in the `main` function to start generating documentation.

---

## load_docgen_ignore ![function](https://img.shields.io/badge/function-green?style=flat)

- **Defined on lines:** 162–180
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
Loads the .docgen_ignore file to add additional folders and languages to ignore.

### Details
Not specified.

### Usage
Used in the `get_files_for_folder` function to load custom ignore rules.

---

## main ![function](https://img.shields.io/badge/function-green?style=flat)

- **Defined on lines:** 182–204
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
The entry point of the script, which processes a folder and generates documentation.

### Details
Not specified.

### Usage
To use this script, run it from the command line with a folder path as an argument.

---