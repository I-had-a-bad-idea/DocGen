# **Documentation for `markdown_generator.py`**
> _Generated on 2025-12-31 16:22:12_

> _Generated with [DocGen](https://github.com/I-had-a-bad-idea/DocGen), may include wrong information!_



# Overview
**Language**: python

Generates Markdown documentation from Python code symbols.

---

# Symbols

<a id='generate_markdown_from_symbols_async'></a>
<details style='margin-bottom: 10px;'>
  <summary> **generate_markdown_from_symbols_async** <span style='background-color:green; color:white; padding:2px 6px; border-radius:4px;'>function</span></summary>

  - **Defined on lines:** 1-26

  <h4>High-Level Summary</h4>
  <p>Asynchronously generates Markdown documentation from Python code symbols.</p>
  <h4>Low-Level Summary</h4>
  <p>This function takes a file path and code as input, processes the code to extract symbol information, and then generates an asynchronous Markdown document based on that information.</p>
<h4>Examples</h4>

```python
generate_markdown_from_symbols_async('path/to/file.py', 'code here')
```

</details>
<hr>
<a id='generate_markdown_from_doc'></a>
<details style='margin-bottom: 10px;'>
  <summary> **generate_markdown_from_doc** <span style='background-color:green; color:white; padding:2px 6px; border-radius:4px;'>function</span></summary>

  - **Defined on lines:** 30-58

  <h4>High-Level Summary</h4>
  <p>Generates Markdown from a Documentation object.</p>
  <h4>Low-Level Summary</h4>
  <p>This function takes a Documentation object and a header string as input, processes the documentation to generate an asynchronous Markdown document based on that information.</p>
<h4>Examples</h4>

```python
generate_markdown_from_doc(doc_object, 'header here')
```

</details>
<hr>
<a id='kind_badge'></a>
<details style='margin-bottom: 10px;'>
  <summary> **kind_badge** <span style='background-color:green; color:white; padding:2px 6px; border-radius:4px;'>function</span></summary>

  - **Defined on lines:** 62-78

  <h4>High-Level Summary</h4>
  <p>Creates a colored badge for the kind of symbol.</p>
  <h4>Low-Level Summary</h4>
  <p>This function takes a kind string as input and returns a colored badge based on predefined colors. The color is determined by the kind's lowercase representation, with defaulting to 'gray' if not found.</p>
<h4>Examples</h4>

```python
kind_badge('function')
```

</details>
<hr>
<a id='save_markdown'></a>
<details style='margin-bottom: 10px;'>
  <summary> **save_markdown** <span style='background-color:green; color:white; padding:2px 6px; border-radius:4px;'>function</span></summary>

  - **Defined on lines:** 82-104

  <h4>High-Level Summary</h4>
  <p>Saves Markdown content to a file.</p>
  <h4>Low-Level Summary</h4>
  <p>This function takes a file path, markdown content, and an optional output directory as input. It creates the necessary directories if they do not exist and writes the markdown content to a file with UTF-8 encoding.</p>
<h4>Examples</h4>

```python
save_markdown('path/to/file.md', 'markdown here')
```

</details>
<hr>
<a id='generate_markdown'></a>
<details style='margin-bottom: 10px;'>
  <summary> **generate_markdown** <span style='background-color:green; color:white; padding:2px 6px; border-radius:4px;'>function</span></summary>

  - **Defined on lines:** 108-124

  <h4>High-Level Summary</h4>
  <p>Generates Markdown from Python code.</p>
  <h4>Low-Level Summary</h4>
  <p>This function takes a file path and code as input, processes the code to extract symbol information, and then generates an asynchronous Markdown document based on that information. It calls `generate_markdown_from_symbols_async` internally.</p>
<h4>Examples</h4>

```python
generate_markdown('path/to/file.py', 'code here')
```

</details>
<hr>