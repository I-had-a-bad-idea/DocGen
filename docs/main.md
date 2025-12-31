# **Documentation for `main.py`**
> _Generated on 2025-12-31 16:22:12_

> _Generated with [DocGen](https://github.com/I-had-a-bad-idea/DocGen), may include wrong information!_



# Overview
**Language**: python

This Python script is designed to generate documentation for Python files within a specified folder. It uses the `markdown_generator` library to convert code into Markdown format and utilizes `tqdm` for progress tracking.

---

# Symbols

<a id='queue'></a>
<details style='margin-bottom: 10px;'>
  <summary> **queue** <span style='background-color:blue; color:white; padding:2px 6px; border-radius:4px;'>variable</span></summary>

  - **Defined on line:** 1

  <h4>High-Level Summary</h4>
  <p>A set used to store paths of Python files that need documentation generation.</p>
  <h4>Low-Level Summary</h4>
  <p>This variable is initialized as an empty set and is used to keep track of all the file paths that are identified as supported languages and need their documentation generated.</p>
</details>
<hr>
<a id='languages'></a>
<details style='margin-bottom: 10px;'>
  <summary> **LANGUAGES** <span style='background-color:blue; color:white; padding:2px 6px; border-radius:4px;'>variable</span></summary>

  - **Defined on lines:** 3-10

  <h4>High-Level Summary</h4>
  <p>A dictionary mapping file extensions to their corresponding programming languages.</p>
  <h4>Low-Level Summary</h4>
  <p>This variable is a dictionary that maps the file extension ".py" to the language "python" and ".rs" to the language "rust". It is used to determine if a given file path corresponds to a supported language.</p>
</details>
<hr>
<a id='is_supported_language'></a>
<details style='margin-bottom: 10px;'>
  <summary> **is_supported_language** <span style='background-color:green; color:white; padding:2px 6px; border-radius:4px;'>function</span></summary>

  - **Defined on lines:** 12-20

  <h4>High-Level Summary</h4>
  <p>A function to check if a given file path corresponds to a supported language.</p>
  <h4>Low-Level Summary</h4>
  <p>This function takes a file path as input and returns `True` if the file extension is in the `LANGUAGES` dictionary, indicating that it is a supported language. It uses the `Path` class from the `pathlib` module to extract the file extension.</p>
</details>
<hr>
<a id='get_code_from_file'></a>
<details style='margin-bottom: 10px;'>
  <summary> **get_code_from_file** <span style='background-color:green; color:white; padding:2px 6px; border-radius:4px;'>function</span></summary>

  - **Defined on lines:** 22-34

  <h4>High-Level Summary</h4>
  <p>A function to read the content of a Python file.</p>
  <h4>Low-Level Summary</h4>
  <p>This function takes a file path as input and attempts to open and read the contents of the file. It uses UTF-8 encoding to ensure that non-ASCII characters are handled correctly. If an error occurs during reading, it prints an error message and returns an empty string.</p>
</details>
<hr>
<a id='generate_docs_for_file'></a>
<details style='margin-bottom: 10px;'>
  <summary> **generate_docs_for_file** <span style='background-color:green; color:white; padding:2px 6px; border-radius:4px;'>function</span></summary>

  - **Defined on lines:** 36-50

  <h4>High-Level Summary</h4>
  <p>A function to generate documentation for a single Python file.</p>
  <h4>Low-Level Summary</h4>
  <p>This function takes a file path as input and checks if it is a valid file. If so, it reads the code from the file using `get_code_from_file` and then calls `generate_markdown` to convert the code into Markdown format. The `tqdm` library is used for progress tracking.</p>
</details>
<hr>
<a id='get_files_for_folder'></a>
<details style='margin-bottom: 10px;'>
  <summary> **get_files_for_folder** <span style='background-color:green; color:white; padding:2px 6px; border-radius:4px;'>function</span></summary>

  - **Defined on lines:** 52-76

  <h4>High-Level Summary</h4>
  <p>A function to recursively retrieve all Python files within a folder.</p>
  <h4>Low-Level Summary</h4>
  <p>This function takes a folder path as input and checks if it is a valid directory. If so, it lists all the elements in the directory using `os.listdir`. For each element, it constructs the full file path and checks if it is a supported language using `is_supported_language`. If it is, the file path is added to the `queue` set. If the element is a subdirectory, the function calls itself recursively to process that subdirectory.</p>
</details>
<hr>
<a id='get_files_for_path'></a>
<details style='margin-bottom: 10px;'>
  <summary> **get_files_for_path** <span style='background-color:green; color:white; padding:2px 6px; border-radius:4px;'>function</span></summary>

  - **Defined on lines:** 78-94

  <h4>High-Level Summary</h4>
  <p>A function to retrieve all Python files based on the input path.</p>
  <h4>Low-Level Summary</h4>
  <p>This function takes a path as input and checks if it is a directory or a file. If it is a directory, it calls `get_files_for_folder` to process all files within that directory. If it is a file, it checks if it is a supported language using `is_supported_language`. If it is, the file path is added to the `queue` set.</p>
</details>
<hr>
<a id='generate_docs'></a>
<details style='margin-bottom: 10px;'>
  <summary> **generate_docs** <span style='background-color:green; color:white; padding:2px 6px; border-radius:4px;'>function</span></summary>

  - **Defined on lines:** 96-108

  <h4>High-Level Summary</h4>
  <p>A function to generate documentation for all files in the `queue` set.</p>
  <h4>Low-Level Summary</h4>
  <p>This function creates a list of tasks using a list comprehension, where each task is an asynchronous call to `generate_docs_for_file` for each file path in the `queue`. It then uses `tqdm_asyncio.as_completed` to process these tasks concurrently and print progress. The `asyncio.run` function is used to execute the main coroutine.</p>
</details>
<hr>
<a id='main'></a>
<details style='margin-bottom: 10px;'>
  <summary> **main** <span style='background-color:green; color:white; padding:2px 6px; border-radius:4px;'>function</span></summary>

  - **Defined on lines:** 110-134

  <h4>High-Level Summary</h4>
  <p>The entry point of the script, which handles command-line arguments and orchestrates the documentation generation process.</p>
  <h4>Low-Level Summary</h4>
  <p>This function checks if there are any command-line arguments. If so, it retrieves all files in the specified path using `get_files_for_path` and generates documentation for them using `generate_docs`. If no arguments are provided, it prints a usage message.</p>
</details>
<hr>