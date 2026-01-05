# **Documentation for `llm_summary.py`**
> _Generated on 2026-01-05 12:45:42_

> _Generated with [DocGen](https://github.com/I-had-a-bad-idea/DocGen), may include wrong information!_



# Table of Contents

- [AsyncClient ![class](https://img.shields.io/badge/class-purple&style=flat)](#asyncclient)
- [BaseModel ![class](https://img.shields.io/badge/class-purple&style=flat)](#basemodel)
- [tqdm_asyncio ![module](https://img.shields.io/badge/module-brown&style=flat)](#tqdm_asyncio)
- [json ![module](https://img.shields.io/badge/module-brown&style=flat)](#json)
- [SymbolOutput ![class](https://img.shields.io/badge/class-purple&style=flat)](#symboloutput)
- [Documentation ![class](https://img.shields.io/badge/class-purple&style=flat)](#documentation)
- [Input ![class](https://img.shields.io/badge/class-purple&style=flat)](#input)
- [MAX_CONTEXT ![variable](https://img.shields.io/badge/variable-blue&style=flat)](#max_context)
- [ollama ![variable](https://img.shields.io/badge/variable-blue&style=flat)](#ollama)
- [OPTIONS ![variable](https://img.shields.io/badge/variable-blue&style=flat)](#options)
- [summarize_code_in_chunk ![function](https://img.shields.io/badge/function-green&style=flat)](#summarize_code_in_chunk)
- [summarize_code ![function](https://img.shields.io/badge/function-green&style=flat)](#summarize_code)

---

# Overview
This file provides a function to summarize code using an OpenAI-like model.			
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
OpenAI-like model,
Pydantic for data validation,
TQDM for progress tracking,
JSON parsing and handling
## Usage
To use this file, you need to have the OpenAI-like model installed. You can then call the `summarize_code` function with an `Input` object containing the code you want to summarize.

---


# Symbols


## AsyncClient ![class](https://img.shields.io/badge/class-purple&style=flat)

- **Defined on line:** 1
- **Symbol kind:** class

### Purpose
An asynchronous client for interacting with an OpenAI-like model.

### Details
Not specified.

### Usage
Instantiate and use this class to interact with the model.

---

## BaseModel ![class](https://img.shields.io/badge/class-purple&style=flat)

- **Defined on line:** 2
- **Symbol kind:** class

### Purpose
A base class for Pydantic models, providing data validation and serialization.

### Details
Not specified.

### Usage
Use this class to define your own models with specific fields and constraints.

---

## tqdm_asyncio ![module](https://img.shields.io/badge/module-brown&style=flat)

- **Defined on line:** 3
- **Symbol kind:** module

### Purpose
A wrapper for tqdm that works with asynchronous iterators.

### Details
Not specified.

### Usage
Use this module to add progress bars to your asynchronous code.

---

## json ![module](https://img.shields.io/badge/module-brown&style=flat)

- **Defined on line:** 4
- **Symbol kind:** module

### Purpose
A module for JSON encoding and decoding.

### Details
Not specified.

### Usage
Use this module to parse and serialize JSON data.

---

## SymbolOutput ![class](https://img.shields.io/badge/class-purple&style=flat)

- **Defined on lines:** 6–12
- **Symbol kind:** class

### Purpose
A Pydantic model representing the output of a symbol in the documentation.

### Details
Not specified.

### Usage
Use this class to define the structure of the symbol output.

---

## Documentation ![class](https://img.shields.io/badge/class-purple&style=flat)

- **Defined on lines:** 13–20
- **Symbol kind:** class

### Purpose
A Pydantic model representing the documentation for a code summary.

### Details
Not specified.

### Usage
Use this class to define the structure of the documentation output.

---

## Input ![class](https://img.shields.io/badge/class-purple&style=flat)

- **Defined on lines:** 21–27
- **Symbol kind:** class

### Purpose
A Pydantic model representing the input to the code summarization function.

### Details
Not specified.

### Usage
Use this class to define the structure of the input data.

---

## MAX_CONTEXT ![variable](https://img.shields.io/badge/variable-blue&style=flat)

- **Defined on line:** 28
- **Symbol kind:** variable

### Purpose
The maximum context size for code summarization.

### Details
Not specified.

### Usage
Use this variable to set the maximum context size for code summarization.

---

## ollama ![variable](https://img.shields.io/badge/variable-blue&style=flat)

- **Defined on line:** 29
- **Symbol kind:** variable

### Purpose
An instance of the AsyncClient class for interacting with the OpenAI-like model.

### Details
Not specified.

### Usage
Use this variable to interact with the model.

---

## OPTIONS ![variable](https://img.shields.io/badge/variable-blue&style=flat)

- **Defined on lines:** 30–32
- **Symbol kind:** variable

### Purpose
The options for interacting with the OpenAI-like model.

### Details
Not specified.

### Usage
Use this variable to set the options for interacting with the model.

---

## summarize_code_in_chunk ![function](https://img.shields.io/badge/function-green&style=flat)

- **Defined on lines:** 34–52
- **Symbol kind:** function

### Purpose
A function to summarize a code chunk using the OpenAI-like model.

### Details
Not specified.

### Usage
Use this function to summarize a code chunk.

---

## summarize_code ![function](https://img.shields.io/badge/function-green&style=flat)

- **Defined on lines:** 54–81
- **Symbol kind:** function

### Purpose
A function to summarize the entire code using the OpenAI-like model.

### Details
Not specified.

### Usage
Use this function to summarize the entire code.

---