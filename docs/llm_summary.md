# **Documentation for `llm_summary.py`**
> _Generated on 2026-01-06 14:37:43_

> _Generated with [DocGen](https://github.com/I-had-a-bad-idea/DocGen), may include wrong information!_



# Table of Contents

- [SymbolOutput ![class](https://img.shields.io/badge/class-purple?style=flat)](#symboloutput-class)
- [Documentation ![class](https://img.shields.io/badge/class-purple?style=flat)](#documentation-class)
- [Input ![class](https://img.shields.io/badge/class-purple?style=flat)](#input-class)
- [MAX_CONTEXT ![variable](https://img.shields.io/badge/variable-blue?style=flat)](#max_context-variable)
- [ollama ![variable](https://img.shields.io/badge/variable-blue?style=flat)](#ollama-variable)
- [OPTIONS ![variable](https://img.shields.io/badge/variable-blue?style=flat)](#options-variable)
- [summarize_code_in_chunk ![function](https://img.shields.io/badge/function-green?style=flat)](#summarize_code_in_chunk-function)
- [summarize_code ![function](https://img.shields.io/badge/function-green?style=flat)](#summarize_code-function)

---

# Overview
This file contains a Python script for summarizing code symbols using the Ollama AI model.			
**Language**: python

## Key components
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
tqdm.asyncio library,
json library
## Usage
To use this file, you need to have the Ollama AI model installed and running. You can then call the `summarize_code` function with an `Input` object containing the code you want to summarize.

---


# Symbols


## SymbolOutput ![class](https://img.shields.io/badge/class-purple?style=flat)

- **Defined on lines:** 10–23
- **Symbol kind:** class

### Definition
class SymbolOutput(BaseModel):
    name: str
    kind: str
    start_line: int
    end_line: int
    definition: str
    parent: str
    purpose: str
    details: str
    usage: str
    limitations: list[str]
### Purpose
Represents the output of a symbol.

### Details
Not specified.

### Usage
To use this class, you need to create an instance with the desired values for each attribute.

---

## Documentation ![class](https://img.shields.io/badge/class-purple?style=flat)

- **Defined on lines:** 25–40
- **Symbol kind:** class

### Definition
class Documentation(BaseModel):
    overview: str
    language: str
    key_components: list[str]
    requirements: list[str]
    usage: str
    symbols: list[SymbolOutput]
### Purpose
Represents the documentation of a code file.

### Details
Not specified.

### Usage
To use this class, you need to create an instance with the desired values for each attribute.

---

## Input ![class](https://img.shields.io/badge/class-purple?style=flat)

- **Defined on lines:** 42–50
- **Symbol kind:** class

### Definition
class Input(BaseModel):
    file_path: str
    code: str
### Purpose
Represents the input to the summarization function.

### Details
Not specified.

### Usage
To use this class, you need to create an instance with the desired values for each attribute.

---

## MAX_CONTEXT ![variable](https://img.shields.io/badge/variable-blue?style=flat)

- **Defined on line:** 52
- **Symbol kind:** variable

### Definition
MAX_CONTEXT = 32768 # 32.768 tokens
### Purpose
The maximum context size for the summarization model.

### Details
Not specified.

### Usage
To use this variable, you need to assign it a value before calling the `summarize_code` function.

---

## ollama ![variable](https://img.shields.io/badge/variable-blue?style=flat)

- **Defined on line:** 54
- **Symbol kind:** variable

### Definition
ollama = AsyncClient()
### Purpose
The Ollama AI client.

### Details
Not specified.

### Usage
To use this variable, you need to create an instance of the `AsyncClient` class before calling the `summarize_code` function.

---

## OPTIONS ![variable](https://img.shields.io/badge/variable-blue?style=flat)

- **Defined on lines:** 56–59
- **Symbol kind:** variable

### Definition
OPTIONS = {
    "temperature": 0.1,
    "num_ctx": MAX_CONTEXT, 

}
### Purpose
The options for the summarization model.

### Details
Not specified.

### Usage
To use this variable, you need to assign it a value before calling the `summarize_code` function.

---

## summarize_code_in_chunk ![function](https://img.shields.io/badge/function-green?style=flat)

- **Defined on lines:** 61–90
- **Symbol kind:** function

### Definition
async def summarize_code_in_chunk(input: Input) -> Documentation:
    prompt = BASE_PROMPT + "\n\nINPUT:\n\n" + input.model_dump_json(indent=2)
    resp = await ollama.generate(MODEL,
                                 prompt=prompt,
                                 options=OPTIONS,
                                 format="json")
    
    # parsed = json.loads(resp.response)
    # with open("model_answers.log", "a") as f:
    #     json.dump(parsed, f, indent=2)
    #     f.write("\n")

    response = Documentation.model_validate_json(resp.response)

    return response
### Purpose
Summarizes a code chunk using the Ollama AI model.

### Details
Not specified.

### Usage
To use this function, you need to create an instance of the `Input` class with the desired values for each attribute and call the function with it.

---

## summarize_code ![function](https://img.shields.io/badge/function-green?style=flat)

- **Defined on lines:** 92–140
- **Symbol kind:** function

### Definition
async def summarize_code(input: Input) -> Documentation:
    code = input.code
    if len(code) > MAX_CONTEXT:
        codes = [
            Input(file_path=input.file_path,
                  code=code[i:i+MAX_CONTEXT])
            for i in range(0, len(code), MAX_CONTEXT)
        ]
    
        doc = Documentation(overview="",
                            symbols=[], language="", key_components=[], requirements=[], usage="")
        for chunk_input in tqdm_asyncio(codes, desc="Summarizing code chunks", unit="chunk"):
            chunk_doc = await summarize_code_in_chunk(chunk_input)
            if not doc.language:
                doc.language = chunk_doc.language
            doc.overview += chunk_doc.overview + "\n"
            doc.symbols.extend(chunk_doc.symbols)
        
        return doc
    
    return await summarize_code_in_chunk(input)
### Purpose
Summarizes a code file using the Ollama AI model.

### Details
Not specified.

### Usage
To use this function, you need to create an instance of the `Input` class with the desired values for each attribute and call the function with it.

---