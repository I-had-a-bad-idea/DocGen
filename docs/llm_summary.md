# **Documentation for `llm_summary.py`**
> _Generated on 2025-12-31 16:22:12_

> _Generated with [DocGen](https://github.com/I-had-a-bad-idea/DocGen), may include wrong information!_



# Overview
**Language**: python

This Python script is designed to generate summaries of code symbols using the Ollama AI model. It includes functions for summarizing code in chunks and as a whole.

---

# Symbols

<a id='asyncclient'></a>
<details style='margin-bottom: 10px;'>
  <summary> **AsyncClient** <span style='background-color:purple; color:white; padding:2px 6px; border-radius:4px;'>class</span></summary>

  - **Defined on lines:** 1-2

  <h4>High-Level Summary</h4>
  <p>An asynchronous client for interacting with the Ollama AI model.</p>
  <h4>Low-Level Summary</h4>
  <p>This class is used to establish an asynchronous connection to the Ollama server and handle requests.</p>
<h4>Examples</h4>

```python
ollama = AsyncClient()
```

</details>
<hr>
<a id='basemodel'></a>
<details style='margin-bottom: 10px;'>
  <summary> **BaseModel** <span style='background-color:purple; color:white; padding:2px 6px; border-radius:4px;'>class</span></summary>

  - **Defined on lines:** 3-4

  <h4>High-Level Summary</h4>
  <p>A base class for Pydantic models, used to define the structure of data.</p>
  <h4>Low-Level Summary</h4>
  <p>This class provides a framework for defining and validating data structures using Python classes.</p>
<h4>Examples</h4>

```python
class SymbolOutput(BaseModel):
    name: str
    kind: str
    start_line: int
    end_line: int
    parent: str
    high_level_summary: str
    low_level_summary: str
    examples: list[str] | None
    notes: str | None
```

</details>
<hr>
<a id='tqdm_asyncio'></a>
<details style='margin-bottom: 10px;'>
  <summary> **tqdm_asyncio** <span style='background-color:brown; color:white; padding:2px 6px; border-radius:4px;'>module</span></summary>

  - **Defined on lines:** 5-6

  <h4>High-Level Summary</h4>
  <p>A module for adding progress bars to asynchronous iterators.</p>
  <h4>Low-Level Summary</h4>
  <p>This module provides a simple way to add progress bars to loops that iterate over asynchronous data sources.</p>
<h4>Examples</h4>

```python
async def summarize_code_in_chunk(input: Input) -> Documentation:
    prompt = BASE_PROMPT + "\n\nINPUT:\n\n" + input.model_dump_json(indent=2)
```

</details>
<hr>
<a id='json'></a>
<details style='margin-bottom: 10px;'>
  <summary> **json** <span style='background-color:brown; color:white; padding:2px 6px; border-radius:4px;'>module</span></summary>

  - **Defined on lines:** 7-8

  <h4>High-Level Summary</h4>
  <p>A module for encoding and decoding JSON data.</p>
  <h4>Low-Level Summary</h4>
  <p>This module provides functions to convert Python objects into JSON format and vice versa.</p>
<h4>Examples</h4>

```python
resp = await ollama.generate(MODEL,
                                 prompt=prompt,
                                 options=OPTIONS,
                                 format="json")
```

</details>
<hr>
<a id='model'></a>
<details style='margin-bottom: 10px;'>
  <summary> **MODEL** <span style='background-color:blue; color:white; padding:2px 6px; border-radius:4px;'>variable</span></summary>

  - **Defined on lines:** 9-10

  <h4>High-Level Summary</h4>
  <p>A string representing the model name and version used for summarization.</p>
  <h4>Low-Level Summary</h4>
  <p>This variable holds the configuration details for the Ollama model to be used for generating summaries.</p>
<h4>Examples</h4>

```python
MODEL = "qwen2.5-coder:3b"
```

</details>
<hr>
<a id='base_prompt'></a>
<details style='margin-bottom: 10px;'>
  <summary> **BASE_PROMPT** <span style='background-color:blue; color:white; padding:2px 6px; border-radius:4px;'>variable</span></summary>

  - **Defined on lines:** 11-14

  <h4>High-Level Summary</h4>
  <p>A string containing the base prompt for generating code summaries.</p>
  <h4>Low-Level Summary</h4>
  <p>This variable holds the introductory text that is prepended to each input when summarizing code.</p>
<h4>Examples</h4>

```python
BASE_PROMPT = """
You are given structured JSON describing code symbols.

For EACH symbol:
- Analyze the code
- Produce a high-level and a detailed low-level summary
- Do NOT keep the code
- Do NOT invent new symbols

Return ONLY valid JSON matching this schema:

{
  "overview": "an_overview_of_the_file",
  "language:" "the_language_of_the_file",
  "symbols": [
    {
      "name": "the_symbol_name",
      "kind": "the_symbol_lo",
      "start_line": 0,
      "end_line": 0,
      "parent": "",
      "high_level_summary": "",
      "low_level_summary": ""
      "examples": [""]
      "notes":  "some_notes"
    }
  ]
}

Examples should be an array of strings or empty.

Return JSON only. No markdown. No explanations.
"""
```

</details>
<hr>
<a id='symboloutput'></a>
<details style='margin-bottom: 10px;'>
  <summary> **SymbolOutput** <span style='background-color:purple; color:white; padding:2px 6px; border-radius:4px;'>class</span></summary>

  - **Defined on lines:** 15-30

  <h4>High-Level Summary</h4>
  <p>A Pydantic model for representing the output of a code symbol summary.</p>
  <h4>Low-Level Summary</h4>
  <p>This class defines the structure of the data returned by the summarization process, including details about each symbol.</p>
<h4>Examples</h4>

```python
class SymbolOutput(BaseModel):
    name: str
    kind: str
    start_line: int
    end_line: int
    parent: str
    high_level_summary: str
    low_level_summary: str
    examples: list[str] | None
    notes: str | None
```

</details>
<hr>
<a id='documentation'></a>
<details style='margin-bottom: 10px;'>
  <summary> **Documentation** <span style='background-color:purple; color:white; padding:2px 6px; border-radius:4px;'>class</span></summary>

  - **Defined on lines:** 31-40

  <h4>High-Level Summary</h4>
  <p>A Pydantic model for representing the overall documentation of code summaries.</p>
  <h4>Low-Level Summary</h4>
  <p>This class defines the structure of the data returned by summarizing multiple code chunks, including an overview and a list of symbol summaries.</p>
<h4>Examples</h4>

```python
class Documentation(BaseModel):
    overview: str
    language: str
    symbols: list[SymbolOutput]
```

</details>
<hr>
<a id='input'></a>
<details style='margin-bottom: 10px;'>
  <summary> **Input** <span style='background-color:purple; color:white; padding:2px 6px; border-radius:4px;'>class</span></summary>

  - **Defined on lines:** 41-50

  <h4>High-Level Summary</h4>
  <p>A Pydantic model for representing the input data to be summarized.</p>
  <h4>Low-Level Summary</h4>
  <p>This class defines the structure of the data provided as input to the summarization process, including a file path and code content.</p>
<h4>Examples</h4>

```python
class Input(BaseModel):
    file_path: str
    code: str
```

</details>
<hr>
<a id='max_context'></a>
<details style='margin-bottom: 10px;'>
  <summary> **MAX_CONTEXT** <span style='background-color:blue; color:white; padding:2px 6px; border-radius:4px;'>variable</span></summary>

  - **Defined on lines:** 51-52

  <h4>High-Level Summary</h4>
  <p>An integer representing the maximum context length for summarization.</p>
  <h4>Low-Level Summary</h4>
  <p>This variable sets the limit on the amount of code that can be processed in a single request to the Ollama model.</p>
<h4>Examples</h4>

```python
MAX_CONTEXT = 32768 # 32.768 tokens
```

</details>
<hr>
<a id='ollama'></a>
<details style='margin-bottom: 10px;'>
  <summary> **ollama** <span style='background-color:blue; color:white; padding:2px 6px; border-radius:4px;'>variable</span></summary>

  - **Defined on lines:** 54-55

  <h4>High-Level Summary</h4>
  <p>An instance of the AsyncClient class for interacting with the Ollama AI model.</p>
  <h4>Low-Level Summary</h4>
  <p>This variable holds the connection to the Ollama server, used to send requests and receive responses.</p>
<h4>Examples</h4>

```python
ollama = AsyncClient()
```

</details>
<hr>
<a id='options'></a>
<details style='margin-bottom: 10px;'>
  <summary> **OPTIONS** <span style='background-color:blue; color:white; padding:2px 6px; border-radius:4px;'>variable</span></summary>

  - **Defined on lines:** 56-60

  <h4>High-Level Summary</h4>
  <p>A dictionary containing options for the Ollama model request.</p>
  <h4>Low-Level Summary</h4>
  <p>This variable holds configuration settings for the request, including temperature and context length.</p>
<h4>Examples</h4>

```python
OPTIONS = {
    "temperature": 0.1,
    "num_ctx": MAX_CONTEXT, 

}
```

</details>
<hr>
<a id='summarize_code_in_chunk'></a>
<details style='margin-bottom: 10px;'>
  <summary> **summarize_code_in_chunk** <span style='background-color:green; color:white; padding:2px 6px; border-radius:4px;'>function</span></summary>

  - **Defined on lines:** 62-78

  <h4>High-Level Summary</h4>
  <p>Asynchronous function for summarizing code in a single chunk.</p>
  <h4>Low-Level Summary</h4>
  <p>This function constructs a prompt, sends it to the Ollama model, and processes the response to generate a summary of a code symbol.</p>
<h4>Examples</h4>

```python
async def summarize_code_in_chunk(input: Input) -> Documentation:
    prompt = BASE_PROMPT + "\n\nINPUT:\n\n" + input.model_dump_json(indent=2)
```

</details>
<hr>
<a id='summarize_code_in_markdown'></a>
<details style='margin-bottom: 10px;'>
  <summary> **summarize_code_in_markdown** <span style='background-color:green; color:white; padding:2px 6px; border-radius:4px;'>function</span></summary>

  - **Defined on lines:** 79-108

  <h4>High-Level Summary</h4>
  <p>Asynchronous function for summarizing code in markdown format.</p>
  <h4>Low-Level Summary</h4>
  <p>This function processes the input code, splits it into chunks if necessary, and summarizes each chunk using the `summarize_code_in_chunk` function. It then combines the summaries to produce a comprehensive documentation of the code.</p>
<h4>Examples</h4>

```python
async def summarize_code_in_markdown(input: Input) -> Documentation:
    code = input.code
```

</details>
<hr>