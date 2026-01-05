# **Documentation for `markdown_generator.py`**
> _Generated on 2026-01-05 12:16:07_

> _Generated with [DocGen](https://github.com/I-had-a-bad-idea/DocGen), may include wrong information!_



# Table of Contents

- [generate_markdown_from_symbols_async (function)](#generate_markdown_from_symbols_async-function)
- [generate_markdown_from_doc (function)](#generate_markdown_from_doc-function)
- [generate_md_for_symbol (function)](#generate_md_for_symbol-function)
- [kind_badge (function)](#kind_badge-function)
- [save_markdown (function)](#save_markdown-function)
- [generate_markdown (function)](#generate_markdown-function)

---

# Overview
Generates markdown documentation from Python code symbols.			
**Language**: python

## Key components
generate_markdown_from_symbols_async,
generate_markdown_from_doc,
generate_md_for_symbol,
kind_badge,
save_markdown
## Requirements
pathlib,
datetime,
llm_summary
## Usage
1. Import the necessary modules:
   ```python
   from pathlib import Path
   from datetime import datetime
   from llm_summary import summarize_code, Documentation, Input
   ```
2. Define a function to generate markdown documentation asynchronously:
   ```python
   async def generate_markdown_from_symbols_async(file_path: str, code: str) -> str:
       # Your implementation here
   ```

---


# Symbols


## generate_markdown_from_symbols_async (function)

- **Defined on lines:** 1–24
- **Symbol kind:** function

### Purpose
Generates markdown documentation asynchronously from Python code symbols.

### Details
This function takes a file path and code as input, generates the markdown documentation using other functions, and returns the final markdown content.

### Usage
1. Import the necessary modules:
   ```python
   from pathlib import Path
   from datetime import datetime
   from llm_summary import summarize_code, Documentation, Input
   ```
2. Define a function to generate markdown documentation asynchronously:
   ```python
   async def generate_markdown_from_symbols_async(file_path: str, code: str) -> str:
       # Your implementation here
   ```




## generate_markdown_from_doc (function)

- **Defined on lines:** 26–104
- **Symbol kind:** function

### Purpose
Generates markdown content from a `Documentation` object.

### Details
This function takes a `Documentation` object and a header string as input, generates the markdown content by sorting symbols, creating a table of contents, and adding sections for overview, key components, requirements, usage, and detailed symbol information.

### Usage
1. Import the necessary modules:
   ```python
   from pathlib import Path
   from datetime import datetime
   from llm_summary import summarize_code, Documentation, Input
   ```
2. Define a function to generate markdown documentation asynchronously:
   ```python
   async def generate_markdown_from_symbols_async(file_path: str, code: str) -> str:
       # Your implementation here
   ```




## generate_md_for_symbol (function)

- **Defined on lines:** 106–153
- **Symbol kind:** function

### Purpose
Generates markdown content for a single symbol.

### Details
This function takes a symbol object as input and generates the markdown content by creating a strong heading, metadata block, semantic sections (purpose, details, usage), and limitations if applicable.

### Usage
1. Import the necessary modules:
   ```python
   from pathlib import Path
   from datetime import datetime
   from llm_summary import summarize_code, Documentation, Input
   ```
2. Define a function to generate markdown documentation asynchronously:
   ```python
   async def generate_markdown_from_symbols_async(file_path: str, code: str) -> str:
       # Your implementation here
   ```




## kind_badge (function)

- **Defined on lines:** 155–172
- **Symbol kind:** function

### Purpose
Creates a colored badge for the symbol kind.

### Details
This function takes a symbol kind as input and returns a colored badge using HTML styles.

### Usage
1. Import the necessary modules:
   ```python
   from pathlib import Path
   from datetime import datetime
   from llm_summary import summarize_code, Documentation, Input
   ```
2. Define a function to generate markdown documentation asynchronously:
   ```python
   async def generate_markdown_from_symbols_async(file_path: str, code: str) -> str:
       # Your implementation here
   ```




## save_markdown (function)

- **Defined on lines:** 174–203
- **Symbol kind:** function

### Purpose
Saves the generated markdown content to a file.

### Details
This function takes a file path, markdown content, and an optional output directory as input, creates the necessary directories if they do not exist, writes the markdown content to a file with UTF-8 encoding, and returns nothing.

### Usage
1. Import the necessary modules:
   ```python
   from pathlib import Path
   from datetime import datetime
   from llm_summary import summarize_code, Documentation, Input
   ```
2. Define a function to generate markdown documentation asynchronously:
   ```python
   async def generate_markdown_from_symbols_async(file_path: str, code: str) -> str:
       # Your implementation here
   ```




## generate_markdown (function)

- **Defined on lines:** 205–214
- **Symbol kind:** function

### Purpose
Generates markdown documentation from Python code.

### Details
This function is a wrapper around `generate_markdown_from_symbols_async` and saves the generated markdown content to a file using the `save_markdown` function.

### Usage
1. Import the necessary modules:
   ```python
   from pathlib import Path
   from datetime import datetime
   from llm_summary import summarize_code, Documentation, Input
   ```
2. Define a function to generate markdown documentation asynchronously:
   ```python
   async def generate_markdown_from_symbols_async(file_path: str, code: str) -> str:
       # Your implementation here
   ```


