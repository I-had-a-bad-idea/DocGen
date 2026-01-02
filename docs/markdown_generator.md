# **Documentation for `markdown_generator.py`**
> _Generated on 2026-01-02 16:43:13_

> _Generated with [DocGen](https://github.com/I-had-a-bad-idea/DocGen), may include wrong information!_



# Overview
Generates markdown documentation for Python files based on their symbols.                                   
**Language**: python

## Key components
generate_markdown_from_symbols_async,
generate_markdown_from_doc,
generate_md_for_symbol,
kind_badge
## Requirements
pathlib,
datetime,
llm_summary
## Usage
To use this file, call `generate_markdown(file_path: str, code: str)` with the path to a Python file and its source code. The function will return the generated markdown content.

---


# Symbols

<a id='generate_markdown_from_symbols_async'></a>
<details style='margin-bottom: 10px;'>
  <summary> **generate_markdown_from_symbols_async** <span style='background-color:green; color:white; padding:2px 6px; border-radius:4px;'>function</span></summary>

  - **Defined on lines:** 1-23

  <h4>Purpose</h4>
  <p>Asynchronously generates markdown documentation for a Python file based on its symbols.</p>
  <h4>Details</h4>
  <p>This function takes the path to a Python file and its source code as input, processes it using `summarize_code` from the `llm_summary` module, and then generates markdown content using `generate_markdown_from_doc`. The resulting markdown is saved to a file in the specified output directory.</p>
  <h4>Usage</h4>
  <p>To use this function, call `await generate_markdown_from_symbols_async(file_path: str, code: str)` with the path to a Python file and its source code. The function will return the generated markdown content.</p>
</details>
<hr>
<a id='generate_markdown_from_doc'></a>
<details style='margin-bottom: 10px;'>
  <summary> **generate_markdown_from_doc** <span style='background-color:green; color:white; padding:2px 6px; border-radius:4px;'>function</span></summary>

  - **Defined on lines:** 25-103

  <h4>Purpose</h4>
  <p>Generates markdown documentation from a `Documentation` object.</p>
  <h4>Details</h4>
  <p>This function takes a `Documentation` object and a header string as input, sorts the symbols by their start line, and generates markdown content for each symbol using `generate_md_for_symbol`. The resulting markdown is returned as a single string.</p>
  <h4>Usage</h4>
  <p>To use this function, call `generate_markdown_from_doc(doc: Documentation, header: str)` with a `Documentation` object and a header string. The function will return the generated markdown content.</p>
</details>
<hr>
<a id='generate_md_for_symbol'></a>
<details style='margin-bottom: 10px;'>
  <summary> **generate_md_for_symbol** <span style='background-color:green; color:white; padding:2px 6px; border-radius:4px;'>function</span></summary>

  - **Defined on lines:** 105-162

  <h4>Purpose</h4>
  <p>Generates markdown documentation for a single symbol.</p>
  <h4>Details</h4>
  <p>This function takes a symbol object as input, creates an anchor for linking from the overview, and generates markdown content for the symbol's purpose, details, usage, and limitations. The resulting markdown is returned as a list of strings.</p>
  <h4>Usage</h4>
  <p>To use this function, call `generate_md_for_symbol(s: Symbol)` with a symbol object. The function will return the generated markdown content.</p>
</details>
<hr>
<a id='kind_badge'></a>
<details style='margin-bottom: 10px;'>
  <summary> **kind_badge** <span style='background-color:green; color:white; padding:2px 6px; border-radius:4px;'>function</span></summary>

  - **Defined on lines:** 164-203

  <h4>Purpose</h4>
  <p>Creates a colored badge for the kind of symbol.</p>
  <h4>Details</h4>
  <p>This function takes the kind of symbol as input and returns a colored badge string. The color is determined based on a predefined mapping of kinds to colors.</p>
  <h4>Usage</h4>
  <p>To use this function, call `kind_badge(kind: str)` with the kind of symbol. The function will return the generated markdown content.</p>
</details>
<hr>