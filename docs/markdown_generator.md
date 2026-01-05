# **Documentation for `markdown_generator.py`**
> _Generated on 2026-01-05 12:45:42_

> _Generated with [DocGen](https://github.com/I-had-a-bad-idea/DocGen), may include wrong information!_



# Table of Contents

- [generate_markdown_from_symbols_async ![function](https://img.shields.io/badge/function-green&style=flat)](#generate_markdown_from_symbols_async)
- [generate_markdown_from_doc ![function](https://img.shields.io/badge/function-green&style=flat)](#generate_markdown_from_doc)
- [generate_md_for_symbol ![function](https://img.shields.io/badge/function-green&style=flat)](#generate_md_for_symbol)
- [kind_badge ![function](https://img.shields.io/badge/function-green&style=flat)](#kind_badge)
- [save_markdown ![function](https://img.shields.io/badge/function-green&style=flat)](#save_markdown)
- [generate_markdown ![function](https://img.shields.io/badge/function-green&style=flat)](#generate_markdown)

---

# Overview
Generates markdown documentation for Python files.			
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
To generate markdown documentation for a Python file, call the `generate_markdown` function with the file path and code as arguments.

---


# Symbols


## generate_markdown_from_symbols_async ![function](https://img.shields.io/badge/function-green&style=flat)

- **Defined on lines:** 1–25
- **Symbol kind:** function

### Purpose
Asynchronously generates markdown documentation for a Python file.

### Details
This function takes the file path and code as arguments, generates the header, input object, and doc object using `summarize_code`, and then calls `generate_markdown_from_doc` to generate the markdown content. Finally, it saves the markdown content to a file.

### Usage
To use this function, call it with the file path and code as arguments.

---

## generate_markdown_from_doc ![function](https://img.shields.io/badge/function-green&style=flat)

- **Defined on lines:** 27–103
- **Symbol kind:** function

### Purpose
Generates markdown content from a doc object.

### Details
This function takes the doc object and header as arguments, creates an empty list of markdown lines, sorts the symbols by start line, adds the table of contents to the markdown lines, appends the overview, key components, requirements, usage, and symbols to the markdown lines, and returns the markdown content.

### Usage
To use this function, call it with the doc object and header as arguments.

---

## generate_md_for_symbol ![function](https://img.shields.io/badge/function-green&style=flat)

- **Defined on lines:** 105–147
- **Symbol kind:** function

### Purpose
Generates markdown content for a symbol object.

### Details
This function takes the symbol object as an argument, creates an empty list of markdown lines, appends the strong heading and metadata block to the markdown lines, checks if the symbol is defined on one line or multiple lines, appends the parent, kind, purpose, details, usage, and limitations to the markdown lines, and returns the markdown content.

### Usage
To use this function, call it with the symbol object as an argument.

---

## kind_badge ![function](https://img.shields.io/badge/function-green&style=flat)

- **Defined on lines:** 149–165
- **Symbol kind:** function

### Purpose
Creates a colored badge for the kind of symbol.

### Details
This function takes the kind of symbol as an argument, returns a string containing the color badge using the `colors` dictionary.

### Usage
To use this function, call it with the kind of symbol as an argument.

---

## save_markdown ![function](https://img.shields.io/badge/function-green&style=flat)

- **Defined on lines:** 167–203
- **Symbol kind:** function

### Purpose
Saves the markdown content to a file.

### Details
This function takes the file path, markdown content, and output directory as arguments, creates an output path object, writes the markdown content to a file with UTF-8 encoding, and returns nothing.

### Usage
To use this function, call it with the file path, markdown content, and output directory as arguments.

---

## generate_markdown ![function](https://img.shields.io/badge/function-green&style=flat)

- **Defined on lines:** 205–213
- **Symbol kind:** function

### Purpose
Generates markdown content for a Python file synchronously.

### Details
This function takes the file path and code as arguments, calls `generate_markdown_from_symbols_async` to generate the markdown content, saves the markdown content to a file using `save_markdown`, and returns nothing.

### Usage
To use this function, call it with the file path and code as arguments.

---