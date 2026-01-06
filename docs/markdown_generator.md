# **Documentation for `markdown_generator.py`**
> _Generated on 2026-01-06 14:19:59_

> _Generated with [DocGen](https://github.com/I-had-a-bad-idea/DocGen), may include wrong information!_



# Table of Contents

- [generate_markdown_from_symbols_async ![function](https://img.shields.io/badge/function-green?style=flat)](#generate_markdown_from_symbols_async-function)
- [generate_markdown_from_doc ![function](https://img.shields.io/badge/function-green?style=flat)](#generate_markdown_from_doc-function)
- [generate_md_for_symbol ![function](https://img.shields.io/badge/function-green?style=flat)](#generate_md_for_symbol-function)
- [kind_badge ![function](https://img.shields.io/badge/function-green?style=flat)](#kind_badge-function)
- [save_markdown ![function](https://img.shields.io/badge/function-green?style=flat)](#save_markdown-function)
- [generate_markdown ![function](https://img.shields.io/badge/function-green?style=flat)](#generate_markdown-function)

---

# Overview
Generates markdown documentation from Python symbols.			
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
To generate markdown documentation from a Python file, call `generate_markdown(file_path: str, code: str)` or `generate_markdown_from_symbols_async(file_path: str, code: str)`. This function will return the generated markdown content.

---


# Symbols


## generate_markdown_from_symbols_async ![function](https://img.shields.io/badge/function-green?style=flat)

- **Defined on lines:** 1–20
- **Symbol kind:** function

### Purpose
Asynchronously generates markdown documentation from Python symbols.

### Details
This function takes a file path and code as input, processes the code to generate markdown documentation, and returns the generated markdown content.

### Usage
To use this function, call `generate_markdown_from_symbols_async(file_path: str, code: str)`. This function will return the generated markdown content.

---

## generate_markdown_from_doc ![function](https://img.shields.io/badge/function-green?style=flat)

- **Defined on lines:** 23–50
- **Symbol kind:** function

### Purpose
Generates markdown from a documentation object.

### Details
This function takes a documentation object and header as input, processes the documentation to generate markdown content, and returns the generated markdown content.

### Usage
To use this function, call `generate_markdown_from_doc(doc: Documentation, header: str)`. This function will return the generated markdown content.

---

## generate_md_for_symbol ![function](https://img.shields.io/badge/function-green?style=flat)

- **Defined on lines:** 53–104
- **Symbol kind:** function

### Purpose
Generates markdown for a symbol object.

### Details
This function takes a symbol object as input, processes the symbol to generate markdown content, and returns the generated markdown content.

### Usage
To use this function, call `generate_md_for_symbol(s)`. This function will return the generated markdown content.

---

## kind_badge ![function](https://img.shields.io/badge/function-green?style=flat)

- **Defined on lines:** 107–128
- **Symbol kind:** function

### Purpose
Creates a colored badge for the kind of symbol.

### Details
This function takes a symbol kind as input, returns a colored badge based on the kind.

### Usage
To use this function, call `kind_badge(kind: str)`. This function will return a colored badge based on the kind.

---

## save_markdown ![function](https://img.shields.io/badge/function-green?style=flat)

- **Defined on lines:** 131–154
- **Symbol kind:** function

### Purpose
Saves markdown content to a file.

### Details
This function takes a file path, markdown content, and output directory as input, saves the markdown content to a file in the specified output directory.

### Usage
To use this function, call `save_markdown(file_path: str, markdown_content: str, output_dir: str = "docs")`. This function will save the markdown content to a file in the specified output directory.

---

## generate_markdown ![function](https://img.shields.io/badge/function-green?style=flat)

- **Defined on lines:** 157–160
- **Symbol kind:** function

### Purpose
Generates markdown from a Python file.

### Details
This function takes a file path and code as input, processes the code to generate markdown documentation, and saves the generated markdown content to a file.

### Usage
To use this function, call `generate_markdown(file_path: str, code: str)`. This function will generate markdown from a Python file and save it to a file.

---