# **Documentation for `llm_summary.py`**
> _Generated on 2026-01-01 15:38:30_

> _Generated with [DocGen](https://github.com/I-had-a-bad-idea/DocGen), may include wrong information!_



# Overview
**Language**: python

This Python script is designed to summarize code symbols using the Ollama AI model. It processes input code, breaks it into chunks if necessary, and generates summaries for each chunk.
## Key components
Ollama,
Pydantic,
TQDM,
JSON

---

# Symbols

<a id='asyncclient'></a>
<details style='margin-bottom: 10px;'>
  <summary> **AsyncClient** <span style='background-color:purple; color:white; padding:2px 6px; border-radius:4px;'>class</span></summary>

  - **Defined on line:** 1

  <h4>Purpose</h4>
  <p>An asynchronous client for interacting with the Ollama AI model.</p>
  <h4>Details</h4>
  <p>This class is used to establish a connection to the Ollama server and send requests for generating summaries.</p>
  <h4>Usage</h4>
  <p>ollama = AsyncClient()</p>
  <h4>Limitations</h4>
  <p>Requires an active internet connection to connect to the Ollama server.</p>
</details>
<hr>
<a id='basemodel'></a>
<details style='margin-bottom: 10px;'>
  <summary> **BaseModel** <span style='background-color:purple; color:white; padding:2px 6px; border-radius:4px;'>class</span></summary>

  - **Defined on lines:** 3-10

  <h4>Purpose</h4>
  <p>A base class for Pydantic models.</p>
  <h4>Details</h4>
  <p>This class provides a framework for defining data models with validation and serialization capabilities.</p>
  <h4>Usage</h4>
  <p>class SymbolOutput(BaseModel):
    name: str
    kind: str
    start_line: int
    end_line: int
    parent: str
    purpose: str
    details: str
    usage: str
    limitations: list[str]
</p>
  <h4>Limitations</h4>
  <p>Requires Pydantic to be installed.</p>
</details>
<hr>
<a id='documentation'></a>
<details style='margin-bottom: 10px;'>
  <summary> **Documentation** <span style='background-color:purple; color:white; padding:2px 6px; border-radius:4px;'>class</span></summary>

  - **Defined on lines:** 12-20

  <h4>Purpose</h4>
  <p>A class for representing the documentation of code symbols.</p>
  <h4>Details</h4>
  <p>This class contains information about the overview, language, key components, and symbols of a code summary.</p>
  <h4>Usage</h4>
  <p>response = Documentation.model_validate_json(resp.response)</p>
  <h4>Limitations</h4>
  <p>Requires Pydantic to be installed.</p>
</details>
<hr>
<a id='input'></a>
<details style='margin-bottom: 10px;'>
  <summary> **Input** <span style='background-color:purple; color:white; padding:2px 6px; border-radius:4px;'>class</span></summary>

  - **Defined on lines:** 22-30

  <h4>Purpose</h4>
  <p>A class for representing the input data for summarizing code.</p>
  <h4>Details</h4>
  <p>This class contains the file path and code to be summarized.</p>
  <h4>Usage</h4>
  <p>input = Input(file_path=input.file_path, code=code)</p>
  <h4>Limitations</h4>
  <p>Requires Pydantic to be installed.</p>
</details>
<hr>
<a id='max_context'></a>
<details style='margin-bottom: 10px;'>
  <summary> **MAX_CONTEXT** <span style='background-color:blue; color:white; padding:2px 6px; border-radius:4px;'>variable</span></summary>

  - **Defined on line:** 32

  <h4>Purpose</h4>
  <p>The maximum context length for the Ollama model.</p>
  <h4>Details</h4>
  <p>This variable defines the maximum number of tokens that can be processed in a single request to the Ollama server.</p>
  <h4>Usage</h4>
  <p>MAX_CONTEXT = 32768</p>
  <h4>Limitations</h4>
  <p>May need to adjust based on the specific requirements of the Ollama model.</p>
</details>
<hr>
<a id='ollama'></a>
<details style='margin-bottom: 10px;'>
  <summary> **ollama** <span style='background-color:blue; color:white; padding:2px 6px; border-radius:4px;'>variable</span></summary>

  - **Defined on line:** 34

  <h4>Purpose</h4>
  <p>An instance of the AsyncClient class.</p>
  <h4>Details</h4>
  <p>This variable holds the connection to the Ollama server and is used for generating summaries.</p>
  <h4>Usage</h4>
  <p>ollama = AsyncClient()</p>
  <h4>Limitations</h4>
  <p>Requires an active internet connection to connect to the Ollama server.</p>
</details>
<hr>
<a id='options'></a>
<details style='margin-bottom: 10px;'>
  <summary> **OPTIONS** <span style='background-color:blue; color:white; padding:2px 6px; border-radius:4px;'>variable</span></summary>

  - **Defined on lines:** 36-40

  <h4>Purpose</h4>
  <p>The options for generating summaries.</p>
  <h4>Details</h4>
  <p>This variable contains the temperature and context length settings for the Ollama model.</p>
  <h4>Usage</h4>
  <p>OPTIONS = {
    "temperature": 0.1,
    "num_ctx": MAX_CONTEXT, 

}</p>
  <h4>Limitations</h4>
  <p>May need to adjust based on the specific requirements of the Ollama model.</p>
</details>
<hr>
<a id='summarize_code_in_chunk'></a>
<details style='margin-bottom: 10px;'>
  <summary> **summarize_code_in_chunk** <span style='background-color:green; color:white; padding:2px 6px; border-radius:4px;'>function</span></summary>

  - **Defined on lines:** 42-58

  <h4>Purpose</h4>
  <p>A function to summarize a single code chunk.</p>
  <h4>Details</h4>
  <p>This function generates a summary for a given input and writes the response to a log file.</p>
  <h4>Usage</h4>
  <p>async def summarize_code_in_chunk(input: Input) -> Documentation:
    prompt = BASE_PROMPT + "\n\nINPUT:\n\n" + input.model_dump_json(indent=2)
    resp = await ollama.generate(MODEL,
                                 prompt=prompt,
                                 options=OPTIONS,
                                 format="json")
</p>
  <h4>Limitations</h4>
  <p>Requires the Ollama AI model to be installed and running.</p>
</details>
<hr>
<a id='summarize_code_in_markdown'></a>
<details style='margin-bottom: 10px;'>
  <summary> **summarize_code_in_markdown** <span style='background-color:green; color:white; padding:2px 6px; border-radius:4px;'>function</span></summary>

  - **Defined on lines:** 60-125

  <h4>Purpose</h4>
  <p>A function to summarize the entire code.</p>
  <h4>Details</h4>
  <p>This function processes the input code, breaks it into chunks if necessary, and generates summaries for each chunk.</p>
  <h4>Usage</h4>
  <p>async def summarize_code_in_markdown(input: Input) -> Documentation:
    code = input.code
    if len(code) > MAX_CONTEXT:
        codes = [
            Input(file_path=input.file_path,
                  code=code[i:i+MAX_CONTEXT])
            for i in range(0, len(code), MAX_CONTEXT)
        ]
</p>
  <h4>Limitations</h4>
  <p>Requires the Ollama AI model to be installed and running.</p>
</details>
<hr>