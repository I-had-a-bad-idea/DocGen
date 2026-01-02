# **Documentation for `llm_summary.py`**
> _Generated on 2026-01-02 16:43:13_

> _Generated with [DocGen](https://github.com/I-had-a-bad-idea/DocGen), may include wrong information!_



# Overview
This file provides a function to summarize code using the Ollama AI model.                                   
**Language**: python

## Key components
AsyncClient,
BaseModel,
tqdm_asyncio,
json,
SymbolOutput,
Documentation,
Input,
MAX_CONTEXT,
ollama,
OPTIONS,
summarize_code_in_chunk,
summarize_code
## Requirements
Ollama AI model,
Pydantic library,
TQDM library
## Usage
To use this file, you need to have the Ollama AI model installed and running. You can then call the `summarize_code` function with an `Input` object containing the code you want to summarize.

---


# Symbols

<a id='asyncclient'></a>
<details style='margin-bottom: 10px;'>
  <summary> **AsyncClient** <span style='background-color:purple; color:white; padding:2px 6px; border-radius:4px;'>class</span></summary>

  - **Defined on line:** 1

  <h4>Purpose</h4>
  <p>An asynchronous client for interacting with the Ollama AI model.</p>
  <h4>Details</h4>
  <p></p>
  <h4>Usage</h4>
  <p>To use this class, you need to import it from the `ollama` module and create an instance of it.</p>
</details>
<hr>
<a id='basemodel'></a>
<details style='margin-bottom: 10px;'>
  <summary> **BaseModel** <span style='background-color:purple; color:white; padding:2px 6px; border-radius:4px;'>class</span></summary>

  - **Defined on line:** 2

  <h4>Purpose</h4>
  <p>A base class for Pydantic models, which provides a way to define data structures with type annotations.</p>
  <h4>Details</h4>
  <p></p>
  <h4>Usage</h4>
  <p>To use this class, you need to import it from the `pydantic` module and create an instance of it.</p>
</details>
<hr>
<a id='tqdm_asyncio'></a>
<details style='margin-bottom: 10px;'>
  <summary> **tqdm_asyncio** <span style='background-color:brown; color:white; padding:2px 6px; border-radius:4px;'>module</span></summary>

  - **Defined on line:** 3

  <h4>Purpose</h4>
  <p>A wrapper around the `tqdm` library that provides asynchronous progress bars.</p>
  <h4>Details</h4>
  <p></p>
  <h4>Usage</h4>
  <p>To use this module, you need to import it from the `tqdm.asyncio` module and create an instance of it.</p>
</details>
<hr>
<a id='json'></a>
<details style='margin-bottom: 10px;'>
  <summary> **json** <span style='background-color:brown; color:white; padding:2px 6px; border-radius:4px;'>module</span></summary>

  - **Defined on line:** 4

  <h4>Purpose</h4>
  <p>A module for encoding and decoding JSON data.</p>
  <h4>Details</h4>
  <p></p>
  <h4>Usage</h4>
  <p>To use this module, you need to import it from the `json` module and create an instance of it.</p>
</details>
<hr>
<a id='symboloutput'></a>
<details style='margin-bottom: 10px;'>
  <summary> **SymbolOutput** <span style='background-color:purple; color:white; padding:2px 6px; border-radius:4px;'>class</span></summary>

  - **Defined on lines:** 10-24

  <h4>Purpose</h4>
  <p>A Pydantic model that represents the output of a symbol.</p>
  <h4>Details</h4>
  <p></p>
  <h4>Usage</h4>
  <p>To use this class, you need to import it from the `llm_summary` module and create an instance of it.</p>
</details>
<hr>
<a id='documentation'></a>
<details style='margin-bottom: 10px;'>
  <summary> **Documentation** <span style='background-color:purple; color:white; padding:2px 6px; border-radius:4px;'>class</span></summary>

  - **Defined on lines:** 26-40

  <h4>Purpose</h4>
  <p>A Pydantic model that represents the documentation for a file.</p>
  <h4>Details</h4>
  <p></p>
  <h4>Usage</h4>
  <p>To use this class, you need to import it from the `llm_summary` module and create an instance of it.</p>
</details>
<hr>
<a id='input'></a>
<details style='margin-bottom: 10px;'>
  <summary> **Input** <span style='background-color:purple; color:white; padding:2px 6px; border-radius:4px;'>class</span></summary>

  - **Defined on lines:** 42-50

  <h4>Purpose</h4>
  <p>A Pydantic model that represents the input for summarizing code.</p>
  <h4>Details</h4>
  <p></p>
  <h4>Usage</h4>
  <p>To use this class, you need to import it from the `llm_summary` module and create an instance of it.</p>
</details>
<hr>
<a id='max_context'></a>
<details style='margin-bottom: 10px;'>
  <summary> **MAX_CONTEXT** <span style='background-color:blue; color:white; padding:2px 6px; border-radius:4px;'>variable</span></summary>

  - **Defined on line:** 52

  <h4>Purpose</h4>
  <p>The maximum context size for summarizing code.</p>
  <h4>Details</h4>
  <p></p>
  <h4>Usage</h4>
  <p>To use this variable, you need to import it from the `llm_summary` module and access it directly.</p>
</details>
<hr>
<a id='ollama'></a>
<details style='margin-bottom: 10px;'>
  <summary> **ollama** <span style='background-color:blue; color:white; padding:2px 6px; border-radius:4px;'>variable</span></summary>

  - **Defined on line:** 54

  <h4>Purpose</h4>
  <p>An instance of the `AsyncClient` class for interacting with the Ollama AI model.</p>
  <h4>Details</h4>
  <p></p>
  <h4>Usage</h4>
  <p>To use this variable, you need to import it from the `ollama` module and access it directly.</p>
</details>
<hr>
<a id='options'></a>
<details style='margin-bottom: 10px;'>
  <summary> **OPTIONS** <span style='background-color:blue; color:white; padding:2px 6px; border-radius:4px;'>variable</span></summary>

  - **Defined on lines:** 56-58

  <h4>Purpose</h4>
  <p>The options for interacting with the Ollama AI model.</p>
  <h4>Details</h4>
  <p></p>
  <h4>Usage</h4>
  <p>To use this variable, you need to import it from the `llm_summary` module and access it directly.</p>
</details>
<hr>
<a id='summarize_code_in_chunk'></a>
<details style='margin-bottom: 10px;'>
  <summary> **summarize_code_in_chunk** <span style='background-color:green; color:white; padding:2px 6px; border-radius:4px;'>function</span></summary>

  - **Defined on lines:** 60-124

  <h4>Purpose</h4>
  <p>A function that summarizes a chunk of code using the Ollama AI model.</p>
  <h4>Details</h4>
  <p></p>
  <h4>Usage</h4>
  <p>To use this function, you need to import it from the `llm_summary` module and call it with an `Input` object containing the code you want to summarize.</p>
</details>
<hr>
<a id='summarize_code'></a>
<details style='margin-bottom: 10px;'>
  <summary> **summarize_code** <span style='background-color:green; color:white; padding:2px 6px; border-radius:4px;'>function</span></summary>

  - **Defined on lines:** 126-174

  <h4>Purpose</h4>
  <p>A function that summarizes a file of code using the Ollama AI model.</p>
  <h4>Details</h4>
  <p></p>
  <h4>Usage</h4>
  <p>To use this function, you need to import it from the `llm_summary` module and call it with an `Input` object containing the code you want to summarize.</p>
</details>
<hr>