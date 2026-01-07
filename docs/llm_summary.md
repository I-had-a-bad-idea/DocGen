# **Documentation for `llm_summary.py`**
> _Generated on 2026-01-07 15:39:33_

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
This file contains a Python script that uses the Ollama API to generate summaries of code snippets. It includes functions for summarizing code in chunks and handling large inputs.			
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
To use this script, you need to have the Ollama API installed and running. You can then call the `summarize_code` function with an `Input` object containing the file path and code to be summarized.

---


# Symbols


## AsyncClient ![class](https://img.shields.io/badge/class-purple?style=flat)

- **Defined on line:** 1
- **Symbol kind:** class

### Definition
```python
from ollama import AsyncClient
```
### Purpose
An asynchronous client for interacting with the Ollama API.

### Details
This class is used to make requests to the Ollama API and handle responses asynchronously.

### Usage
To use this class, you need to create an instance of it and call its methods to interact with the API.

---

## BaseModel ![class](https://img.shields.io/badge/class-purple?style=flat)

- **Defined on line:** 2
- **Symbol kind:** class

### Definition
```python
from pydantic import BaseModel
```
### Purpose
A base class for Pydantic models.

### Details
This class provides a framework for defining data models with validation and serialization capabilities.

### Usage
To use this class, you need to create a subclass of it and define the fields that make up your model.

---

## tqdm_asyncio ![module](https://img.shields.io/badge/module-brown?style=flat)

- **Defined on line:** 3
- **Symbol kind:** module

### Definition
```python
import tqdm.asyncio
```
### Purpose
A module for adding progress bars to asynchronous code.

### Details
This module provides a simple way to add progress bars to asynchronous loops, making it easier to monitor the progress of long-running tasks.

### Usage
To use this module, you need to import it and call its functions within an asynchronous loop.

---

## json ![module](https://img.shields.io/badge/module-brown?style=flat)

- **Defined on line:** 4
- **Symbol kind:** module

### Definition
```python
import json
```
### Purpose
A module for encoding and decoding JSON data.

### Details
This module provides functions for converting Python objects to JSON strings and vice versa, making it easy to serialize and deserialize data.

### Usage
To use this module, you need to import it and call its functions to encode or decode JSON data.

---

## SymbolOutput ![class](https://img.shields.io/badge/class-purple?style=flat)

- **Defined on lines:** 10–23
- **Symbol kind:** class

### Definition
```python
class SymbolOutput(BaseModel):
```
### Purpose
A Pydantic model for representing a code symbol.

### Details
This class defines the structure of a code symbol, including its name, kind, start and end lines, definition, parent, purpose, details, usage, and limitations.

### Usage
To use this class, you need to create an instance of it and define the fields that make up your symbol.

---

## Documentation ![class](https://img.shields.io/badge/class-purple?style=flat)

- **Defined on lines:** 25–40
- **Symbol kind:** class

### Definition
```python
class Documentation(BaseModel):
```
### Purpose
A Pydantic model for representing the documentation of a code summary.

### Details
This class defines the structure of the documentation, including its overview, language, key components, requirements, usage, and symbols.

### Usage
To use this class, you need to create an instance of it and define the fields that make up your documentation.

---

## Input ![class](https://img.shields.io/badge/class-purple?style=flat)

- **Defined on lines:** 42–51
- **Symbol kind:** class

### Definition
```python
class Input(BaseModel):
```
### Purpose
A Pydantic model for representing the input to the summarization function.

### Details
This class defines the structure of the input, including its file path and code.

### Usage
To use this class, you need to create an instance of it and define the fields that make up your input.

---

## MAX_CONTEXT ![variable](https://img.shields.io/badge/variable-blue?style=flat)

- **Defined on line:** 53
- **Symbol kind:** variable

### Definition
```python
MAX_CONTEXT = 32768 # 32.768 tokens
```
### Purpose
A constant representing the maximum context size for summarization.

### Details
This variable defines the maximum number of tokens that can be processed in a single request to the Ollama API.

### Usage
To use this variable, you need to reference it within your code to set the maximum context size for summarization.

---

## ollama ![variable](https://img.shields.io/badge/variable-blue?style=flat)

- **Defined on line:** 54
- **Symbol kind:** variable

### Definition
```python
ollama = AsyncClient()
```
### Purpose
An instance of the AsyncClient class for interacting with the Ollama API.

### Details
This variable initializes an instance of the AsyncClient class, which is used to make requests to the Ollama API.

### Usage
To use this variable, you need to reference it within your code to interact with the Ollama API.

---

## OPTIONS ![variable](https://img.shields.io/badge/variable-blue?style=flat)

- **Defined on lines:** 56–58
- **Symbol kind:** variable

### Definition
```python
OPTIONS = {
```
### Purpose
A dictionary containing the options for making requests to the Ollama API.

### Details
This variable defines a dictionary of options that can be used when making requests to the Ollama API, including the temperature and maximum context size.

### Usage
To use this variable, you need to reference it within your code to set the options for making requests to the Ollama API.

---

## summarize_code_in_chunk ![function](https://img.shields.io/badge/function-green?style=flat)

- **Defined on lines:** 60–123
- **Symbol kind:** function

### Definition
```python
async def summarize_code_in_chunk(input: Input) -> Documentation:
```
### Purpose
A function for summarizing a code chunk using the Ollama API.

### Details
This function takes an `Input` object as input and uses it to generate a summary of the code using the Ollama API. It returns a `Documentation` object containing the summary.

### Usage
To use this function, you need to create an instance of the `Input` class and pass it to the function.

---

## summarize_code ![function](https://img.shields.io/badge/function-green?style=flat)

- **Defined on lines:** 125–190
- **Symbol kind:** function

### Definition
```python
async def summarize_code(input: Input) -> Documentation:
```
### Purpose
A function for summarizing a large code input using the Ollama API.

### Details
This function takes an `Input` object as input and uses it to generate a summary of the code using the Ollama API. If the code is too long, it splits it into chunks and summarizes each chunk separately before combining the results.

### Usage
To use this function, you need to create an instance of the `Input` class and pass it to the function.

---