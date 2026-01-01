# **Documentation for `llm_summary.py`**
> _Generated on 2026-01-01 15:22:00_

> _Generated with [DocGen](https://github.com/I-had-a-bad-idea/DocGen), may include wrong information!_



# Overview
**Language**: python

This Python script is designed to generate summaries of code symbols using the Ollama AI model. It includes functions for summarizing code in chunks and as a single markdown document.
## Key components
OllamaClient
Pydantic BaseModel
TQDMAsyncio

---

# Symbols

<a id='symboloutput'></a>
<details style='margin-bottom: 10px;'>
  <summary> **SymbolOutput** <span style='background-color:purple; color:white; padding:2px 6px; border-radius:4px;'>class</span></summary>

  - **Defined on lines:** 10-23

  <h4>Purpose</h4>
  <p>Represents the output of a symbol summary.</p>
  <h4>Details</h4>
  <p>Contains fields for the name, kind, start line, end line, parent, purpose, details, usage, and problems of a symbol.</p>
  <h4>Usage</h4>
  <p>Used to validate and serialize symbol summaries.</p>
</details>
<hr>
<a id='documentation'></a>
<details style='margin-bottom: 10px;'>
  <summary> **Documentation** <span style='background-color:purple; color:white; padding:2px 6px; border-radius:4px;'>class</span></summary>

  - **Defined on lines:** 25-38

  <h4>Purpose</h4>
  <p>Represents the documentation of code symbols.</p>
  <h4>Details</h4>
  <p>Contains fields for the overview, language, key components, and symbols of a document.</p>
  <h4>Usage</h4>
  <p>Used to validate and serialize documentation of code symbols.</p>
</details>
<hr>
<a id='input'></a>
<details style='margin-bottom: 10px;'>
  <summary> **Input** <span style='background-color:purple; color:white; padding:2px 6px; border-radius:4px;'>class</span></summary>

  - **Defined on lines:** 40-51

  <h4>Purpose</h4>
  <p>Represents the input for summarizing code.</p>
  <h4>Details</h4>
  <p>Contains fields for the file path and code of an input.</p>
  <h4>Usage</h4>
  <p>Used to pass input data to the summarization functions.</p>
</details>
<hr>
<a id='max_context'></a>
<details style='margin-bottom: 10px;'>
  <summary> **MAX_CONTEXT** <span style='background-color:gray; color:white; padding:2px 6px; border-radius:4px;'>constant</span></summary>

  - **Defined on lines:** 53-54

  <h4>Purpose</h4>
  <p>The maximum context length for code chunks.</p>
  <h4>Details</h4>
  <p>Sets the maximum number of tokens allowed in a code chunk.</p>
  <h4>Usage</h4>
  <p>Used to determine how to split the input code into chunks.</p>
</details>
<hr>
<a id='ollama'></a>
<details style='margin-bottom: 10px;'>
  <summary> **ollama** <span style='background-color:blue; color:white; padding:2px 6px; border-radius:4px;'>variable</span></summary>

  - **Defined on lines:** 56-57

  <h4>Purpose</h4>
  <p>An instance of the OllamaClient class for generating summaries.</p>
  <h4>Details</h4>
  <p>Used to interact with the Ollama AI model for summarizing code.</p>
  <h4>Usage</h4>
  <p>Initialized at the beginning of the script.</p>
</details>
<hr>
<a id='options'></a>
<details style='margin-bottom: 10px;'>
  <summary> **OPTIONS** <span style='background-color:blue; color:white; padding:2px 6px; border-radius:4px;'>variable</span></summary>

  - **Defined on lines:** 59-62

  <h4>Purpose</h4>
  <p>The options for generating summaries using the Ollama model.</p>
  <h4>Details</h4>
  <p>Sets the temperature and number of context tokens for summarization.</p>
  <h4>Usage</h4>
  <p>Used when calling the generate method of the OllamaClient class.</p>
</details>
<hr>
<a id='summarize_code_in_chunk'></a>
<details style='margin-bottom: 10px;'>
  <summary> **summarize_code_in_chunk** <span style='background-color:green; color:white; padding:2px 6px; border-radius:4px;'>function</span></summary>

  - **Defined on lines:** 64-103

  <h4>Purpose</h4>
  <p>Summarizes a code chunk using the Ollama AI model.</p>
  <h4>Details</h4>
  <p>Takes an Input object as input, constructs a prompt with the input code, generates a summary using the Ollama model, and returns a Documentation object.</p>
  <h4>Usage</h4>
  <p>Used to summarize individual code chunks.</p>
</details>
<hr>
<a id='summarize_code_in_markdown'></a>
<details style='margin-bottom: 10px;'>
  <summary> **summarize_code_in_markdown** <span style='background-color:green; color:white; padding:2px 6px; border-radius:4px;'>function</span></summary>

  - **Defined on lines:** 105-142

  <h4>Purpose</h4>
  <p>Summarizes the entire code using the Ollama AI model.</p>
  <h4>Details</h4>
  <p>Takes an Input object as input, checks if the code is too long to summarize in a single chunk, splits it into chunks if necessary, summarizes each chunk, and combines the summaries into a single Documentation object.</p>
  <h4>Usage</h4>
  <p>Used to summarize the entire code.</p>
</details>
<hr>