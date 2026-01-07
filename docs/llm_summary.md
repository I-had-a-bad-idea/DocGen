# **Documentation for `llm_summary.py`**
> _Generated on 2026-01-06 14:43:45_

> _Generated with [DocGen](https://github.com/I-had-a-bad-idea/DocGen), may include wrong information!_



# Table of Contents

- [AsyncClient ![class](https://img.shields.io/badge/class-purple?style=flat)](#asyncclient-class)
- [BaseModel ![class](https://img.shields.io/badge/class-purple?style=flat)](#basemodel-class)
- [tqdm_asyncio ![module](https://img.shields.io/badge/module-brown?style=flat)](#tqdm_asyncio-module)
- [json ![module](https://img.shields.io/badge/module-brown?style=flat)](#json-module)
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
This file contains a Python script that uses the Ollama API to generate summaries of code symbols based on structured JSON input.			
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
Ollama API,
Pydantic library,
TQDM library
## Usage
To use this file, you need to have the Ollama API installed and running. You can then call the `summarize_code` function with an `Input` object containing the file path and code as arguments.

---


# Symbols


## AsyncClient ![class](https://img.shields.io/badge/class-purple?style=flat)

- **Defined on line:** 1
- **Symbol kind:** class

### Definition
from ollama import AsyncClient

### Purpose
An asynchronous client for interacting with the Ollama API.

### Details
This class provides methods for making requests to the Ollama API and handling responses.

### Usage
To use this class, you need to create an instance of it and call its methods.

---

## BaseModel ![class](https://img.shields.io/badge/class-purple?style=flat)

- **Defined on line:** 2
- **Symbol kind:** class

### Definition
from pydantic import BaseModel

### Purpose
A base class for creating Pydantic models.

### Details
This class provides a framework for defining data models with validation and serialization capabilities.

### Usage
To use this class, you need to create a subclass of it and define its fields.

---

## tqdm_asyncio ![module](https://img.shields.io/badge/module-brown?style=flat)

- **Defined on line:** 3
- **Symbol kind:** module

### Definition
import tqdm.asyncio

### Purpose
A module for adding progress bars to asynchronous code.

### Details
This module provides a `tqdm` function that can be used to add progress bars to asynchronous loops.

### Usage
To use this module, you need to import it and call its functions.

---

## json ![module](https://img.shields.io/badge/module-brown?style=flat)

- **Defined on line:** 4
- **Symbol kind:** module

### Definition
import json

### Purpose
A module for working with JSON data.

### Details
This module provides functions for encoding and decoding JSON data.

### Usage
To use this module, you need to import it and call its functions.

---

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
A Pydantic model for representing a code symbol.

### Details
This class defines the fields that represent a code symbol, including its name, kind, start and end lines, definition, parent, purpose, details, usage, and limitations.

### Usage
To use this class, you need to create an instance of it and define its fields.

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
A Pydantic model for representing the documentation of code.

### Details
This class defines the fields that represent the documentation of code, including its overview, language, key components, requirements, usage, and a list of symbols.

### Usage
To use this class, you need to create an instance of it and define its fields.

---

## Input ![class](https://img.shields.io/badge/class-purple?style=flat)

- **Defined on lines:** 42–51
- **Symbol kind:** class

### Definition
class Input(BaseModel):
    file_path: str
    code: str

### Purpose
A Pydantic model for representing input to the summarization function.

### Details
This class defines the fields that represent input to the summarization function, including its file path and code.

### Usage
To use this class, you need to create an instance of it and define its fields.

---

## MAX_CONTEXT ![variable](https://img.shields.io/badge/variable-blue?style=flat)

- **Defined on line:** 53
- **Symbol kind:** variable

### Definition
MAX_CONTEXT = 32768 # 32.768 tokens

### Purpose
The maximum context size for the summarization function.

### Details
This variable defines the maximum number of tokens that can be processed in a single request to the Ollama API.

### Usage
To use this variable, you need to reference it when calling the `summarize_code` function.

---

## ollama ![variable](https://img.shields.io/badge/variable-blue?style=flat)

- **Defined on line:** 54
- **Symbol kind:** variable

### Definition
ollama = AsyncClient()

### Purpose
An instance of the `AsyncClient` class for interacting with the Ollama API.

### Details
This variable holds an instance of the `AsyncClient` class, which can be used to make requests to the Ollama API.

### Usage
To use this variable, you need to reference it when calling the `summarize_code` function.

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
The options for the summarization function.

### Details
This variable holds a dictionary of options that can be used when making requests to the Ollama API.

### Usage
To use this variable, you need to reference it when calling the `summarize_code` function.

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
A function for summarizing code in a chunk.

### Details
This function takes an `Input` object as input and uses the Ollama API to generate a summary of the code. The summary is returned as a `Documentation` object.

### Usage
To use this function, you need to call it with an `Input` object containing the file path and code as arguments.

---

## summarize_code ![function](https://img.shields.io/badge/function-green?style=flat)

- **Defined on lines:** 92–130
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
A function for summarizing code.

### Details
This function takes an `Input` object as input and uses the Ollama API to generate a summary of the code. If the code is too long, it splits it into chunks and summarizes each chunk separately. The summaries are then combined into a single `Documentation` object.

### Usage
To use this function, you need to call it with an `Input` object containing the file path and code as arguments.

---