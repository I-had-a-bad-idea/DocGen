# **Documentation for `markdown_generator.py`**
> _Generated on 2026-01-05 12:51:22_

> _Generated with [DocGen](https://github.com/I-had-a-bad-idea/DocGen), may include wrong information!_



# Table of Contents

- [generate_markdown_from_symbols_async ![function](https://img.shields.io/badge/function-green?style=flat)](#generate_markdown_from_symbols_async)
- [generate_markdown_from_doc ![function](https://img.shields.io/badge/function-green?style=flat)](#generate_markdown_from_doc)
- [generate_md_for_symbol ![function](https://img.shields.io/badge/function-green?style=flat)](#generate_md_for_symbol)
- [kind_badge ![function](https://img.shields.io/badge/function-green?style=flat)](#kind_badge)
- [save_markdown ![function](https://img.shields.io/badge/function-green?style=flat)](#save_markdown)
- [generate_markdown ![function](https://img.shields.io/badge/function-green?style=flat)](#generate_markdown)

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


## generate_markdown_from_symbols_async ![function](https://img.shields.io/badge/function-green?style=flat)

- **Defined on lines:** 1–25
- **Symbol kind:** function

### Purpose
Asynchronously generates markdown documentation for a Python file.

### Details
This function takes the file path and code as arguments, generates the markdown content using `generate_markdown_from_doc`, and saves it to a file in the specified output directory.

### Usage
To use this function, call it with the file path and code as arguments. For example:

```python
generate_markdown_from_symbols_async('path/to/file.py', 'code here')
```


---

## generate_markdown_from_doc ![function](https://img.shields.io/badge/function-green?style=flat)

- **Defined on lines:** 27–103
- **Symbol kind:** function

### Purpose
Generates markdown content from a `Documentation` object.

### Details
This function takes a `Documentation` object and a header string as arguments, generates the markdown content by sorting symbols by line number, creating a table of contents, adding overview information, key components, requirements, usage, and detailed symbol information.

### Usage
To use this function, call it with a `Documentation` object and a header string. For example:

```python
doc = Documentation(...)
header = "..."
markdown_content = generate_markdown_from_doc(doc, header)
```


---

## generate_md_for_symbol ![function](https://img.shields.io/badge/function-green?style=flat)

- **Defined on lines:** 105–143
- **Symbol kind:** function

### Purpose
Generates markdown content for a symbol.

### Details
This function takes a symbol object as an argument, generates the markdown content by creating a strong heading, metadata block, purpose, details, usage, and limitations sections.

### Usage
To use this function, call it with a symbol object. For example:

```python
symbol = Symbol(...)
markdown_content = generate_md_for_symbol(symbol)
```


---

## kind_badge ![function](https://img.shields.io/badge/function-green?style=flat)

- **Defined on lines:** 145–162
- **Symbol kind:** function

### Purpose
Creates a colored badge for the symbol kind.

### Details
This function takes a symbol kind as an argument and returns a markdown badge string based on the color associated with that kind.

### Usage
To use this function, call it with a symbol kind. For example:

```python
color_badge = kind_badge('function')
```


---

## save_markdown ![function](https://img.shields.io/badge/function-green?style=flat)

- **Defined on lines:** 164–203
- **Symbol kind:** function

### Purpose
Saves markdown content to a file.

### Details
This function takes the file path, markdown content, and output directory as arguments, creates the output directory if it doesn't exist, writes the markdown content to a file in the specified output directory, and returns the file path.

### Usage
To use this function, call it with the file path, markdown content, and output directory. For example:

```python
save_markdown('path/to/file.md', 'markdown content here', 'docs')
```


---

## generate_markdown ![function](https://img.shields.io/badge/function-green?style=flat)

- **Defined on lines:** 205–213
- **Symbol kind:** function

### Purpose
Generates markdown documentation for a Python file.

### Details
This function is an alias for `generate_markdown_from_symbols_async` and takes the file path and code as arguments, generates the markdown content using `generate_markdown_from_symbols_async`, and saves it to a file in the specified output directory.

### Usage
To use this function, call it with the file path and code. For example:

```python
generate_markdown('path/to/file.py', 'code here')
```


---