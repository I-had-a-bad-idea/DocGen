# **Documentation for `main.py`**
> _Generated on 2026-01-01 15:38:30_

> _Generated with [DocGen](https://github.com/I-had-a-bad-idea/DocGen), may include wrong information!_



# Overview
**Language**: Python

This Python script is a tool for generating documentation from source code files. It supports various programming languages and ignores certain folders or file types.
## Key components
queue,
LANGUAGES,
ignored_languages,
ignored_folders,
get_code_from_file,
generate_docs_for_file,
get_files_for_folder,
get_files_for_path,
generate_docs,
load_docgen_ignore,
main

---

# Symbols

<a id='queue'></a>
<details style='margin-bottom: 10px;'>
  <summary> **queue** <span style='background-color:blue; color:white; padding:2px 6px; border-radius:4px;'>variable</span></summary>

  - **Defined on line:** 1

  <h4>Purpose</h4>
  <p>A set to store file paths that need documentation generation.</p>
  <h4>Details</h4>
  <p>This variable is used to keep track of all files that are eligible for generating documentation. It is initialized as an empty set.</p>
  <h4>Usage</h4>
  <p>queue.add(element_path)</p>
</details>
<hr>
<a id='languages'></a>
<details style='margin-bottom: 10px;'>
  <summary> **LANGUAGES** <span style='background-color:gray; color:white; padding:2px 6px; border-radius:4px;'>dictionary</span></summary>

  - **Defined on lines:** 3-45

  <h4>Purpose</h4>
  <p>A dictionary mapping file extensions to their corresponding programming languages.</p>
  <h4>Details</h4>
  <p>This dictionary contains mappings for various file extensions to the programming language they represent. It is used to determine if a file should be processed by the script.</p>
  <h4>Usage</h4>
  <p>LANGUAGES.get(suffix)</p>
</details>
<hr>
<a id='ignored_languages'></a>
<details style='margin-bottom: 10px;'>
  <summary> **ignored_languages** <span style='background-color:gray; color:white; padding:2px 6px; border-radius:4px;'>list</span></summary>

  - **Defined on lines:** 47-48

  <h4>Purpose</h4>
  <p>A list of file extensions to be ignored during processing.</p>
  <h4>Details</h4>
  <p>This list contains file extensions that should not be processed by the script. It is used to filter out files based on their extension.</p>
  <h4>Usage</h4>
  <p>if suffix in ignored_languages</p>
</details>
<hr>
<a id='ignored_folders'></a>
<details style='margin-bottom: 10px;'>
  <summary> **ignored_folders** <span style='background-color:gray; color:white; padding:2px 6px; border-radius:4px;'>list</span></summary>

  - **Defined on lines:** 49-50

  <h4>Purpose</h4>
  <p>A list of folder names to be ignored during processing.</p>
  <h4>Details</h4>
  <p>This list contains folder names that should not be processed by the script. It is used to filter out folders based on their name or location.</p>
  <h4>Usage</h4>
  <p>if ignored_folder in folder.parents or folder.name == ignored_folder.name</p>
</details>
<hr>
<a id='get_code_from_file'></a>
<details style='margin-bottom: 10px;'>
  <summary> **get_code_from_file** <span style='background-color:green; color:white; padding:2px 6px; border-radius:4px;'>function</span></summary>

  - **Defined on lines:** 52-63

  <h4>Purpose</h4>
  <p>Reads the content of a file and returns it as a string.</p>
  <h4>Details</h4>
  <p>This function takes a file path as input, opens the file in read mode, reads its contents, and returns them as a string. It handles exceptions to print an error message if the file cannot be read.</p>
  <h4>Usage</h4>
  <p>code = get_code_from_file(file_path)</p>
</details>
<hr>
<a id='generate_docs_for_file'></a>
<details style='margin-bottom: 10px;'>
  <summary> **generate_docs_for_file** <span style='background-color:green; color:white; padding:2px 6px; border-radius:4px;'>function</span></summary>

  - **Defined on lines:** 65-80

  <h4>Purpose</h4>
  <p>Generates documentation for a single file.</p>
  <h4>Details</h4>
  <p>This function checks if the input file is valid and supported. If so, it reads the code from the file using `get_code_from_file` and then calls `generate_markdown` to generate documentation.</p>
  <h4>Usage</h4>
  <p>await generate_docs_for_file(file_path)</p>
</details>
<hr>
<a id='get_files_for_folder'></a>
<details style='margin-bottom: 10px;'>
  <summary> **get_files_for_folder** <span style='background-color:green; color:white; padding:2px 6px; border-radius:4px;'>function</span></summary>

  - **Defined on lines:** 82-107

  <h4>Purpose</h4>
  <p>Recursively retrieves all files in a folder and its subfolders.</p>
  <h4>Details</h4>
  <p>This function takes a folder path as input, lists all elements within the folder, and processes each element. It uses `tqdm` to display progress during the file retrieval process. If an element is a file, it checks if it is supported using `is_supported_language`. If it is a directory, it checks if it is allowed using `is_allowed_folder` and recursively calls itself for subdirectories.</p>
  <h4>Usage</h4>
  <p>await get_files_for_folder(folder_path)</p>
</details>
<hr>
<a id='get_files_for_path'></a>
<details style='margin-bottom: 10px;'>
  <summary> **get_files_for_path** <span style='background-color:green; color:white; padding:2px 6px; border-radius:4px;'>function</span></summary>

  - **Defined on lines:** 109-124

  <h4>Purpose</h4>
  <p>Recursively retrieves all files in a path, including subfolders.</p>
  <h4>Details</h4>
  <p>This function takes a path as input. If the path is a directory, it calls `load_docgen_ignore` to load any ignore rules and then calls `get_files_for_folder`. If the path is a file, it checks if it is supported using `is_supported_language` and adds it to the queue.</p>
  <h4>Usage</h4>
  <p>await get_files_for_path(path)</p>
</details>
<hr>
<a id='generate_docs'></a>
<details style='margin-bottom: 10px;'>
  <summary> **generate_docs** <span style='background-color:green; color:white; padding:2px 6px; border-radius:4px;'>function</span></summary>

  - **Defined on lines:** 126-138

  <h4>Purpose</h4>
  <p>Asynchronously generates documentation for all files in the queue.</p>
  <h4>Details</h4>
  <p>This function creates a list of tasks to generate documentation for each file in the queue. It uses `tqdm_asyncio.as_completed` to process these tasks concurrently and display progress during the generation process.</p>
  <h4>Usage</h4>
  <p>await generate_docs()</p>
</details>
<hr>
<a id='load_docgen_ignore'></a>
<details style='margin-bottom: 10px;'>
  <summary> **load_docgen_ignore** <span style='background-color:green; color:white; padding:2px 6px; border-radius:4px;'>function</span></summary>

  - **Defined on lines:** 140-159

  <h4>Purpose</h4>
  <p>Loads ignore rules from a file named `.docgen_ignore` in the specified folder.</p>
  <h4>Details</h4>
  <p>This function takes a folder path as input, constructs the path to the `.docgen_ignore` file, and checks if it exists. If it does, it reads the file line by line, ignoring any lines that are empty or start with a dot (`.`). It adds any ignored folders or languages to their respective lists.</p>
  <h4>Usage</h4>
  <p>load_docgen_ignore(folder)</p>
</details>
<hr>
<a id='main'></a>
<details style='margin-bottom: 10px;'>
  <summary> **main** <span style='background-color:green; color:white; padding:2px 6px; border-radius:4px;'>function</span></summary>

  - **Defined on lines:** 161-203

  <h4>Purpose</h4>
  <p>The main entry point of the script.</p>
  <h4>Details</h4>
  <p>This function checks if a command-line argument is provided. If so, it calls `get_files_for_path` and `generate_docs` to process the specified folder and generate documentation for its files. If no argument is provided, it prints usage instructions.</p>
  <h4>Usage</h4>
  <p>if len(sys.argv) >= 2:
    path = sys.argv[1]
    asyncio.run(get_files_for_path(path))
    asyncio.run(generate_docs())</p>
</details>
<hr>