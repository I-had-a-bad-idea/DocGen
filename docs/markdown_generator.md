# **Documentation for `markdown_generator.py`**
> _Generated on 2026-01-06 14:37:43_

> _Generated with [DocGen](https://github.com/I-had-a-bad-idea/DocGen), may include wrong information!_



# Table of Contents

- [generate_markdown_from_symbols_async ![function](https://img.shields.io/badge/function-green?style=flat)](#generate_markdown_from_symbols_async-function)
- [Input ![class](https://img.shields.io/badge/class-purple?style=flat)](#input-class)
- [Documentation ![class](https://img.shields.io/badge/class-purple?style=flat)](#documentation-class)
- [SymbolOutput ![class](https://img.shields.io/badge/class-purple?style=flat)](#symboloutput-class)
- [kind_badge ![function](https://img.shields.io/badge/function-green?style=flat)](#kind_badge-function)

---

# Overview
Generates markdown documentation for Python files.			
**Language**: python

## Key components
generate_markdown_from_symbols_async,
Input,
Documentation,
SymbolOutput,
kind_badge
## Requirements
pathlib,
datetime,
llm_summary
## Usage
1. Import the necessary modules:

   ```python
   from pathlib import Path
   from datetime import datetime
   from llm_summary import summarize_code, Documentation, Input, SymbolOutput
   ```

2. Define a function to generate markdown documentation for a Python file:

   ```python
   async def generate_markdown(file_path: str, code: str) -> str:
       # Your implementation here
   ```

---


# Symbols


## generate_markdown_from_symbols_async ![function](https://img.shields.io/badge/function-green?style=flat)

- **Defined on lines:** 1–23
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
Generates markdown documentation for a Python file asynchronously.

### Details
Not specified.

### Usage
1. Import the necessary modules:

   ```python
   from pathlib import Path
   from datetime import datetime
   from llm_summary import summarize_code, Documentation, Input, SymbolOutput
   ```

2. Define a function to generate markdown documentation for a Python file:

   ```python
   async def generate_markdown(file_path: str, code: str) -> str:
       md = await generate_markdown_from_symbols_async(file_path, code)
       save_markdown(file_path, md)
   ```

---

## Input ![class](https://img.shields.io/badge/class-purple?style=flat)

- **Defined on lines:** 3–10
- **Symbol kind:** class

### Definition
class Input:

    def __init__(self, code: str, file_path: str):
        self.code = code
        self.file_path = file_path
### Purpose
Represents input data for generating markdown documentation.

### Details
Not specified.

### Usage
1. Import the necessary modules:

   ```python
   from pathlib import Path
   from datetime import datetime
   from llm_summary import summarize_code, Documentation, Input, SymbolOutput
   ```

2. Define a function to generate markdown documentation for a Python file:

   ```python
   async def generate_markdown(file_path: str, code: str) -> str:
       md = await generate_markdown_from_symbols_async(file_path, code)
       save_markdown(file_path, md)
   ```

---

## Documentation ![class](https://img.shields.io/badge/class-purple?style=flat)

- **Defined on lines:** 12–30
- **Symbol kind:** class

### Definition
class Documentation:

    def __init__(self, overview: str, language: str, key_components: list[str], requirements: list[str], usage: str):
        self.overview = overview
        self.language = language
        self.key_components = key_components
        self.requirements = requirements
        self.usage = usage
### Purpose
Represents the documentation generated for a Python file.

### Details
Not specified.

### Usage
1. Import the necessary modules:

   ```python
   from pathlib import Path
   from datetime import datetime
   from llm_summary import summarize_code, Documentation, Input, SymbolOutput
   ```

2. Define a function to generate markdown documentation for a Python file:

   ```python
   async def generate_markdown(file_path: str, code: str) -> str:
       md = await generate_markdown_from_symbols_async(file_path, code)
       save_markdown(file_path, md)
   ```

---

## SymbolOutput ![class](https://img.shields.io/badge/class-purple?style=flat)

- **Defined on lines:** 32–50
- **Symbol kind:** class

### Definition
class SymbolOutput:

    def __init__(self, name: str, kind: str, start_line: int, end_line: int, parent: str = None, purpose: str = None, details: str = None, usage: str = None, limitations: list[str] = None):
        self.name = name
        self.kind = kind
        self.start_line = start_line
        self.end_line = end_line
        self.parent = parent
        self.purpose = purpose
        self.details = details
        self.usage = usage
        self.limitations = limitations
### Purpose
Represents the output of a symbol in the documentation.

### Details
Not specified.

### Usage
1. Import the necessary modules:

   ```python
   from pathlib import Path
   from datetime import datetime
   from llm_summary import summarize_code, Documentation, Input, SymbolOutput
   ```

2. Define a function to generate markdown documentation for a Python file:

   ```python
   async def generate_markdown(file_path: str, code: str) -> str:
       md = await generate_markdown_from_symbols_async(file_path, code)
       save_markdown(file_path, md)
   ```

---

## kind_badge ![function](https://img.shields.io/badge/function-green?style=flat)

- **Defined on lines:** 52–70
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
Not specified.

### Usage
1. Import the necessary modules:

   ```python
   from pathlib import Path
   from datetime import datetime
   from llm_summary import summarize_code, Documentation, Input, SymbolOutput
   ```

2. Define a function to generate markdown documentation for a Python file:

   ```python
   async def generate_markdown(file_path: str, code: str) -> str:
       md = await generate_markdown_from_symbols_async(file_path, code)
       save_markdown(file_path, md)
   ```

---