# **Documentation for `markdown_generator.py`**
> _Generated on 2026-01-07 15:39:33_

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
This file contains functions and classes for generating markdown documentation from code symbols.			
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
To use this file, you can call the `generate_markdown` function with a file path and code string. This will generate markdown documentation for the given code symbols.

---


# Symbols


## generate_markdown_from_symbols_async ![function](https://img.shields.io/badge/function-green?style=flat)

- **Defined on lines:** 1–23
- **Symbol kind:** function

### Definition
```python
async def generate_markdown_from_symbols_async(file_path: str, code: str) -> str:
```
### Purpose
Generates markdown documentation from code symbols asynchronously.

### Details
This function takes a file path and code string as input, generates the necessary headers, creates an `Input` object, summarizes the code using `summarize_code`, and then generates markdown using `generate_markdown_from_doc`. The resulting markdown is returned.

### Usage
To use this function, call it with a file path and code string. For example:

```python
import asyncio
from pathlib import Path
from datetime import datetime
from llm_summary import summarize_code, Documentation, Input, SymbolOutput

def generate_markdown(file_path: str, code: str) -> str:
    md = await generate_markdown_from_symbols_async(file_path, code)
    save_markdown(file_path, md)
```


### Limitations
- Asynchronous nature of the function

---

## generate_markdown_from_doc ![function](https://img.shields.io/badge/function-green?style=flat)

- **Defined on lines:** 25–103
- **Symbol kind:** function

### Definition
```python
def generate_markdown_from_doc(doc: Documentation, header: str) -> str:
```
### Purpose
Generates markdown from a `Documentation` object.

### Details
This function takes a `Documentation` object and a header string as input, sorts the symbols by their start line, creates a table of contents, adds an overview section, key components, requirements, usage, and detailed sections for each symbol. The resulting markdown is returned.

### Usage
To use this function, call it with a `Documentation` object and a header string. For example:

```python
def generate_markdown_from_doc(doc: Documentation, header: str) -> str:
    md_lines = [header, ""]  # Start with header and a blank line

    doc.symbols.sort(key=lambda s: s.start_line)

    # # Create a table of contents 
    md_lines.append("# Table of Contents\n")
    for s in doc.symbols:
        slug = (s.name + "-" + s.kind).lower().replace(" ", "-")
        md_lines.append(f"- [{s.name} {kind_badge(s.kind)}](#{slug})")
    md_lines.append("\n---\n")
    
    # Overview
    md_lines.append("# Overview")
    md_lines.append(doc.overview + "\t\t\t")
    md_lines.append(f"**Language**: {doc.language}\n")
    md_lines.append("## Key components")
    md_lines.append(",\n".join(doc.key_components))
    md_lines.append("## Requirements")
    md_lines.append(",\n".join(doc.requirements))
    md_lines.append("## Usage")
    md_lines.append(doc.usage)
    md_lines.append("\n---\n")  # separator before detailed sections

    # Symbols
    md_lines.append("")
    md_lines.append("# Symbols")
    md_lines.append("") # Spacing

    for s in doc.symbols:
        md_lines.extend(generate_md_for_symbol(s, doc.language))

    return "\n".join(md_lines)
```


### Limitations
- Sorting of symbols by start line

---

## generate_md_for_symbol ![function](https://img.shields.io/badge/function-green?style=flat)

- **Defined on lines:** 105–173
- **Symbol kind:** function

### Definition
```python
def generate_md_for_symbol(s: SymbolOutput, lang: str) -> list[str]:
```
### Purpose
Generates markdown for a `SymbolOutput` object.

### Details
This function takes a `SymbolOutput` object and a language string as input, generates the necessary headings, metadata block, definition, purpose, details, usage, and limitations sections. The resulting markdown is returned.

### Usage
To use this function, call it with a `SymbolOutput` object and a language string. For example:

```python
def generate_md_for_symbol(s: SymbolOutput, lang: str) -> list[str]:
    md = []

    # Strong heading
    md.append(f"\n## {s.name} {kind_badge(s.kind)}")
    md.append("")

    # Metadata block
    if s.start_line == s.end_line:
        md.append(f"- **Defined on line:** {s.start_line}")
    else:
        md.append(f"- **Defined on lines:** {s.start_line}–{s.end_line}")

    if s.parent:
        md.append(f"- **Parent:** {s.parent}")

    md.append(f"- **Symbol kind:** {s.kind}")
    md.append("")

    md.append("### Definition")
    md.append(f"```{lang}")
    md.append(s.definition.split("\n")[0])
    md.append("```")

    # Semantic sections
    md.append("### Purpose")
    md.append(s.purpose or "Not specified.")
    md.append("")

    md.append("### Details")
    md.append(s.details or "Not specified.")
    md.append("")

    md.append("### Usage")
    md.append(s.usage or "Not specified.")
    md.append("")

    if s.limitations:
        md.append("### Limitations")
        md.append("\n".join(f"- {l}" for l in s.limitations))
        md.append("")

    md.append("---")
    return md
```


### Limitations
- Handling of limitations

---

## kind_badge ![function](https://img.shields.io/badge/function-green?style=flat)

- **Defined on lines:** 175–204
- **Symbol kind:** function

### Definition
```python
def kind_badge(kind: str) -> str:
```
### Purpose
Generates a colored badge for the kind of symbol.

### Details
This function takes a symbol kind as input and returns a colored badge using shields.io. The color is determined by the kind, with defaulting to gray if the kind is not recognized.

### Usage
To use this function, call it with a symbol kind string. For example:

```python
def kind_badge(kind: str) -> str:
    colors = {
        "variable": "blue",
        "function": "green",
        "class": "purple",
        "enum": "orange",
        "struct": "teal",
        "module": "brown"
    }
    color = colors.get(kind.lower(), "gray")
    return f"![{kind}](https://img.shields.io/badge/{kind}-{color}?style=flat)"
```


### Limitations
- Defaulting to gray if kind is not recognized

---

## save_markdown ![function](https://img.shields.io/badge/function-green?style=flat)

- **Defined on lines:** 206–243
- **Symbol kind:** function

### Definition
```python
def save_markdown(file_path: str, markdown_content: str, output_dir: str = "docs"):
```
### Purpose
Saves markdown content to a file.

### Details
This function takes a file path, markdown content, and an optional output directory as input. It creates the necessary directories if they do not exist and writes the markdown content to a file with the same name as the input file in the specified output directory.

### Usage
To use this function, call it with a file path, markdown content, and an optional output directory. For example:

```python
def save_markdown(file_path: str, markdown_content: str, output_dir: str = "docs"):

    output_path = Path(output_dir)
    output_path.mkdir(exist_ok=True)

    md_file = Path(f"{output_path}/{Path(file_path).stem}.md")
    md_file.write_text(markdown_content, encoding="utf-8")
```


### Limitations
- Writing to a file

---

## generate_markdown ![function](https://img.shields.io/badge/function-green?style=flat)

- **Defined on lines:** 245–263
- **Symbol kind:** function

### Definition
```python
def generate_markdown(file_path: str, code: str):
```
### Purpose
Generates markdown documentation from a file and saves it.

### Details
This function takes a file path and code string as input, generates the markdown documentation using `generate_markdown_from_symbols_async`, and then saves the resulting markdown to a file using `save_markdown`. The generated markdown is returned.

### Usage
To use this function, call it with a file path and code string. For example:

```python
def generate_markdown(file_path: str, code: str):
    md = await generate_markdown_from_symbols_async(file_path, code)
    save_markdown(file_path, md)
```


### Limitations
- Asynchronous nature of the function

---