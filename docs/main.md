# **Documentation for `main.py`**
> _Generated on 2026-01-02 16:43:13_

> _Generated with [DocGen](https://github.com/I-had-a-bad-idea/DocGen), may include wrong information!_



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
Python 3.6 or later,
markdown_generator library,
tqdm library,
asyncio library,
pathlib library
## Usage
Run the script with a folder path as an argument to generate documentation for all supported files in that folder and its subfolders.

---


# Symbols

<a id='queue'></a>
<details style='margin-bottom: 10px;'>
  <summary> **queue** <span style='background-color:gray; color:white; padding:2px 6px; border-radius:4px;'>set</span></summary>

  - **Defined on lines:** 1-2

  <h4>Purpose</h4>
  <p>A set to store file paths for processing.</p>
  <h4>Details</h4>
  <p></p>
  <h4>Usage</h4>
  <p>Add file paths to the queue using `queue.add(element_path)`.</p>
</details>
<hr>
<a id='languages'></a>
<details style='margin-bottom: 10px;'>
  <summary> **LANGUAGES** <span style='background-color:gray; color:white; padding:2px 6px; border-radius:4px;'>dict</span></summary>

  - **Defined on lines:** 4-56

  <h4>Purpose</h4>
  <p>A dictionary mapping file extensions to their corresponding programming languages.</p>
  <h4>Details</h4>
  <p></p>
  <h4>Usage</h4>
  <p>Check if a file is supported by looking up its extension in the `LANGUAGES` dictionary.</p>
</details>
<hr>
<a id='ignored_languages'></a>
<details style='margin-bottom: 10px;'>
  <summary> **ignored_languages** <span style='background-color:gray; color:white; padding:2px 6px; border-radius:4px;'>list</span></summary>

  - **Defined on lines:** 58-60

  <h4>Purpose</h4>
  <p>A list of file extensions to ignore.</p>
  <h4>Details</h4>
  <p></p>
  <h4>Usage</h4>
  <p>Add file extensions to the `ignored_languages` list to exclude them from processing.</p>
</details>
<hr>
<a id='ignored_folders'></a>
<details style='margin-bottom: 10px;'>
  <summary> **ignored_folders** <span style='background-color:gray; color:white; padding:2px 6px; border-radius:4px;'>list</span></summary>

  - **Defined on lines:** 62-64

  <h4>Purpose</h4>
  <p>A list of folder names to ignore.</p>
  <h4>Details</h4>
  <p></p>
  <h4>Usage</h4>
  <p>Add folder names to the `ignored_folders` list to exclude them from processing.</p>
</details>
<hr>
<a id='is_supported_language'></a>
<details style='margin-bottom: 10px;'>
  <summary> **is_supported_language** <span style='background-color:green; color:white; padding:2px 6px; border-radius:4px;'>function</span></summary>

  - **Defined on lines:** 66-78

  <h4>Purpose</h4>
  <p>Check if a file is supported by its extension.</p>
  <h4>Details</h4>
  <p>Returns `True` if the file extension is in the `LANGUAGES` dictionary, otherwise returns `False`.</p>
  <h4>Usage</h4>
  <p>Use this function to determine if a file should be processed.</p>
</details>
<hr>
<a id='is_allowed_folder'></a>
<details style='margin-bottom: 10px;'>
  <summary> **is_allowed_folder** <span style='background-color:green; color:white; padding:2px 6px; border-radius:4px;'>function</span></summary>

  - **Defined on lines:** 80-92

  <h4>Purpose</h4>
  <p>Check if a folder is allowed for processing.</p>
  <h4>Details</h4>
  <p>Returns `True` if the folder is not in the `ignored_folders` list and is not ignored by its name or parent folders, otherwise returns `False`.</p>
  <h4>Usage</h4>
  <p>Use this function to determine if a folder should be processed.</p>
</details>
<hr>
<a id='get_code_from_file'></a>
<details style='margin-bottom: 10px;'>
  <summary> **get_code_from_file** <span style='background-color:green; color:white; padding:2px 6px; border-radius:4px;'>function</span></summary>

  - **Defined on lines:** 94-108

  <h4>Purpose</h4>
  <p>Read the content of a file and return it as a string.</p>
  <h4>Details</h4>
  <p>Returns the contents of the file if successful, otherwise returns an empty string and prints an error message.</p>
  <h4>Usage</h4>
  <p>Use this function to read the code from a file.</p>
</details>
<hr>
<a id='generate_docs_for_file'></a>
<details style='margin-bottom: 10px;'>
  <summary> **generate_docs_for_file** <span style='background-color:green; color:white; padding:2px 6px; border-radius:4px;'>function</span></summary>

  - **Defined on lines:** 110-124

  <h4>Purpose</h4>
  <p>Generate documentation for a single file.</p>
  <h4>Details</h4>
  <p>Reads the code from the file and calls `generate_markdown` to generate documentation if the file is supported.</p>
  <h4>Usage</h4>
  <p>Use this function to generate documentation for a specific file.</p>
</details>
<hr>
<a id='get_files_for_folder'></a>
<details style='margin-bottom: 10px;'>
  <summary> **get_files_for_folder** <span style='background-color:green; color:white; padding:2px 6px; border-radius:4px;'>function</span></summary>

  - **Defined on lines:** 126-158

  <h4>Purpose</h4>
  <p>Recursively get all files in a folder and its subfolders.</p>
  <h4>Details</h4>
  <p>Iterates over the elements of the folder, checks if each element is a file or directory, and processes it accordingly. Uses `tqdm` to display progress.</p>
  <h4>Usage</h4>
  <p>Use this function to recursively process all files in a folder.</p>
</details>
<hr>
<a id='get_files_for_path'></a>
<details style='margin-bottom: 10px;'>
  <summary> **get_files_for_path** <span style='background-color:green; color:white; padding:2px 6px; border-radius:4px;'>function</span></summary>

  - **Defined on lines:** 160-174

  <h4>Purpose</h4>
  <p>Get all files for a given path, whether it's a folder or a file.</p>
  <h4>Details</h4>
  <p>If the path is a directory, calls `get_files_for_folder` to process all files in the directory. If the path is a file, checks if it's supported and adds it to the queue.</p>
  <h4>Usage</h4>
  <p>Use this function to get all files for a given path.</p>
</details>
<hr>
<a id='generate_docs'></a>
<details style='margin-bottom: 10px;'>
  <summary> **generate_docs** <span style='background-color:green; color:white; padding:2px 6px; border-radius:4px;'>function</span></summary>

  - **Defined on lines:** 176-184

  <h4>Purpose</h4>
  <p>Generate documentation for all files in the queue.</p>
  <h4>Details</h4>
  <p>Creates a list of tasks to generate documentation for each file in the queue and runs them concurrently using `asyncio`.</p>
  <h4>Usage</h4>
  <p>Use this function to generate documentation for all files in the queue.</p>
</details>
<hr>
<a id='load_docgen_ignore'></a>
<details style='margin-bottom: 10px;'>
  <summary> **load_docgen_ignore** <span style='background-color:green; color:white; padding:2px 6px; border-radius:4px;'>function</span></summary>

  - **Defined on lines:** 186-204

  <h4>Purpose</h4>
  <p>Load the .docgen_ignore file and add ignored languages and folders to their respective lists.</p>
  <h4>Details</h4>
  <p>Reads the .docgen_ignore file if it exists, adds each line to the `ignored_languages` or `ignored_folders` list based on whether it ends with a slash or not.</p>
  <h4>Usage</h4>
  <p>Use this function to load the .docgen_ignore file and configure ignored languages and folders.</p>
</details>
<hr>
<a id='main'></a>
<details style='margin-bottom: 10px;'>
  <summary> **main** <span style='background-color:green; color:white; padding:2px 6px; border-radius:4px;'>function</span></summary>

  - **Defined on lines:** 206-234

  <h4>Purpose</h4>
  <p>The main function to run the script.</p>
  <h4>Details</h4>
  <p>Checks if a path is provided as an argument, loads the .docgen_ignore file, processes all files in the folder and its subfolders, generates documentation for each file, and prints a success message.</p>
  <h4>Usage</h4>
  <p>Run this function to execute the script.</p>
</details>
<hr>