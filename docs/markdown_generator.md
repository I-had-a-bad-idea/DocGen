# **Documentation for `markdown_generator.py`**
> _Generated on 2026-01-06 14:43:45_

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
Generates markdown documentation from code symbols.			
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
To generate markdown documentation from a Python file, call `generate_markdown(file_path: str, code: str)`.

---


# Symbols


## generate_markdown_from_symbols_async ![function](https://img.shields.io/badge/function-green?style=flat)

- **Defined on lines:** 1–24
- **Symbol kind:** function

### Definition
async def generate_markdown_from_symbols_async(file_path: str, code: str) -> str:

    # Header
    header_lines = []
    header_lines.append(f"# **Documentation for `{Path(file_path).name}`**")
    header_lines.append(f"> _Generated on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}_\n")
    header_lines.append(f"> _Generated with [DocGen](https://github.com/I-had-a-bad-idea/DocGen), may include wrong information!_\n\n")

    input = Input(code=code, file_path=file_path)

    header = "\n".join(header_lines)

    doc = await summarize_code(input)

    md = generate_markdown_from_doc(doc, header)

    return md
### Purpose
Generates markdown documentation from code symbols asynchronously.

### Details
This function takes a file path and code as input, generates a header, creates an input object, summarizes the code using `summarize_code`, and then generates markdown documentation using `generate_markdown_from_doc`.

### Usage
To use this function, call `await generate_markdown_from_symbols_async(file_path: str, code: str)`.

---

## generate_markdown_from_doc ![function](https://img.shields.io/badge/function-green?style=flat)

- **Defined on lines:** 26–103
- **Symbol kind:** function

### Definition
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
        md_lines.extend(generate_md_for_symbol(s))

    return "\n".join(md_lines)
### Purpose
Generates markdown documentation from a `Documentation` object.

### Details
This function takes a `Documentation` object and a header string, sorts the symbols by line number, creates a table of contents, adds an overview section, key components, requirements, usage, and detailed sections for each symbol using `generate_md_for_symbol`, and returns the final markdown content.

### Usage
To use this function, call `generate_markdown_from_doc(doc: Documentation, header: str)`.

---

## generate_md_for_symbol ![function](https://img.shields.io/badge/function-green?style=flat)

- **Defined on lines:** 105–142
- **Symbol kind:** function

### Definition
def generate_md_for_symbol(s: SymbolOutput) -> list[str]:
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
    md.append(s.definition)

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
### Purpose
Generates markdown documentation for a `SymbolOutput` object.

### Details
This function takes a `SymbolOutput` object and generates markdown content for it, including a strong heading, metadata block, definition, purpose, details, usage, and limitations sections.

### Usage
To use this function, call `generate_md_for_symbol(s: SymbolOutput)`.

---

## kind_badge ![function](https://img.shields.io/badge/function-green?style=flat)

- **Defined on lines:** 144–160
- **Symbol kind:** function

### Definition
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
### Purpose
Generates a colored badge for the kind of symbol.

### Details
This function takes a symbol kind as input and returns a colored badge using Shields.io. The color is determined based on the kind, with defaulting to gray if the kind is not recognized.

### Usage
To use this function, call `kind_badge(kind: str)`.

---

## save_markdown ![function](https://img.shields.io/badge/function-green?style=flat)

- **Defined on lines:** 162–185
- **Symbol kind:** function

### Definition
def save_markdown(file_path: str, markdown_content: str, output_dir: str = "docs"):

    output_path = Path(output_dir)
    output_path.mkdir(exist_ok=True)

    md_file = Path(f"{output_path}/{Path(file_path).stem}.md")
    md_file.write_text(markdown_content, encoding="utf-8")
### Purpose
Saves markdown content to a file.

### Details
This function takes a file path, markdown content, and an optional output directory, creates the output directory if it doesn't exist, writes the markdown content to a file with UTF-8 encoding, and saves it in the specified directory.

### Usage
To use this function, call `save_markdown(file_path: str, markdown_content: str, output_dir: str = "docs")`.

---

## generate_markdown ![function](https://img.shields.io/badge/function-green?style=flat)

- **Defined on lines:** 187–204
- **Symbol kind:** function

### Definition
async def generate_markdown(file_path: str, code: str):

    md = await generate_markdown_from_symbols_async(file_path, code)
    save_markdown(file_path, md)
### Purpose
Generates markdown documentation and saves it to a file.

### Details
This function takes a file path and code as input, generates markdown documentation using `generate_markdown_from_symbols_async`, and saves the generated markdown content to a file using `save_markdown`.

### Usage
To use this function, call `await generate_markdown(file_path: str, code: str)`.

---