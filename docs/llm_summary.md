# **Documentation for `llm_summary.py`**
> _Generated on 2026-01-05 12:51:22_

> _Generated with [DocGen](https://github.com/I-had-a-bad-idea/DocGen), may include wrong information!_



# Table of Contents

- [AsyncClient ![class](https://img.shields.io/badge/class-purple?style=flat)](#asyncclient)
- [BaseModel ![class](https://img.shields.io/badge/class-purple?style=flat)](#basemodel)
- [tqdm_asyncio ![module](https://img.shields.io/badge/module-brown?style=flat)](#tqdm_asyncio)
- [json ![module](https://img.shields.io/badge/module-brown?style=flat)](#json)
- [SymbolOutput ![class](https://img.shields.io/badge/class-purple?style=flat)](#symboloutput)
- [Documentation ![class](https://img.shields.io/badge/class-purple?style=flat)](#documentation)
- [Input ![class](https://img.shields.io/badge/class-purple?style=flat)](#input)
- [MAX_CONTEXT ![variable](https://img.shields.io/badge/variable-blue?style=flat)](#max_context)
- [ollama ![variable](https://img.shields.io/badge/variable-blue?style=flat)](#ollama)
- [OPTIONS ![variable](https://img.shields.io/badge/variable-blue?style=flat)](#options)
- [summarize_code_in_chunk ![function](https://img.shields.io/badge/function-green?style=flat)](#summarize_code_in_chunk)
- [summarize_code ![function](https://img.shields.io/badge/function-green?style=flat)](#summarize_code)

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
To use this script, you need to have the Ollama API installed and running. You can then call the `summarize_code` function with an `Input` object containing the file path and code as input.

---


# Symbols


## AsyncClient ![class](https://img.shields.io/badge/class-purple?style=flat)

- **Defined on line:** 1
- **Symbol kind:** class

### Purpose
A class for interacting with the Ollama API asynchronously.

### Details
This class provides methods for generating text using the Ollama API.

### Usage
To use this class, you need to create an instance of it and call its `generate` method.

---

## BaseModel ![class](https://img.shields.io/badge/class-purple?style=flat)

- **Defined on lines:** 3–4
- **Symbol kind:** class

### Purpose
A base class for Pydantic models.

### Details
This class provides a framework for defining data models with validation and serialization capabilities.

### Usage
To use this class, you need to create a subclass of it and define its fields using the `Field` decorator.

---

## tqdm_asyncio ![module](https://img.shields.io/badge/module-brown?style=flat)

- **Defined on line:** 5
- **Symbol kind:** module

### Purpose
A module for adding progress bars to asynchronous code.

### Details
This module provides a `tqdm` function that can be used to add progress bars to asynchronous loops.

### Usage
To use this module, you need to import it and call its `tqdm_asyncio` function with an iterable as input.

---

## json ![module](https://img.shields.io/badge/module-brown?style=flat)

- **Defined on line:** 6
- **Symbol kind:** module

### Purpose
A module for working with JSON data.

### Details
This module provides functions for encoding and decoding JSON data.

### Usage
To use this module, you need to import it and call its `loads` and `dumps` functions.

---

## SymbolOutput ![class](https://img.shields.io/badge/class-purple?style=flat)

- **Defined on lines:** 10–23
- **Symbol kind:** class

### Purpose
A Pydantic model for representing the output of a symbol summarization.

### Details
This class has fields for the name, kind, start line, end line, parent, purpose, details, usage, and limitations of a symbol.

### Usage
To use this class, you need to create an instance of it and set its fields using keyword arguments.

---

## Documentation ![class](https://img.shields.io/badge/class-purple?style=flat)

- **Defined on lines:** 25–40
- **Symbol kind:** class

### Purpose
A Pydantic model for representing the documentation of a code summary.

### Details
This class has fields for the overview, language, key components, requirements, usage, and symbols of a code summary.

### Usage
To use this class, you need to create an instance of it and set its fields using keyword arguments.

---

## Input ![class](https://img.shields.io/badge/class-purple?style=flat)

- **Defined on lines:** 42–51
- **Symbol kind:** class

### Purpose
A Pydantic model for representing the input to a code summarization.

### Details
This class has fields for the file path and code of a code summary.

### Usage
To use this class, you need to create an instance of it and set its fields using keyword arguments.

---

## MAX_CONTEXT ![variable](https://img.shields.io/badge/variable-blue?style=flat)

- **Defined on line:** 53
- **Symbol kind:** variable

### Purpose
The maximum context length for code summarization.

### Details
This variable is used to limit the amount of code that can be summarized in a single request to the Ollama API.

### Usage
To use this variable, you need to set its value before calling the `summarize_code` function.

---

## ollama ![variable](https://img.shields.io/badge/variable-blue?style=flat)

- **Defined on line:** 54
- **Symbol kind:** variable

### Purpose
An instance of the AsyncClient class for interacting with the Ollama API.

### Details
This variable is used to generate text using the Ollama API.

### Usage
To use this variable, you need to create an instance of it and call its `generate` method.

---

## OPTIONS ![variable](https://img.shields.io/badge/variable-blue?style=flat)

- **Defined on lines:** 56–57
- **Symbol kind:** variable

### Purpose
The options for generating text using the Ollama API.

### Details
This variable is used to set the temperature and context length for generating text.

### Usage
To use this variable, you need to set its value before calling the `summarize_code` function.

---

## summarize_code_in_chunk ![function](https://img.shields.io/badge/function-green?style=flat)

- **Defined on lines:** 60–81
- **Symbol kind:** function

### Purpose
A function for summarizing code symbols in a single chunk.

### Details
This function takes an `Input` object as input and generates text using the Ollama API to summarize the code symbols.

### Usage
To use this function, you need to create an instance of it and call its `summarize_code_in_chunk` method with an `Input` object as input.

---

## summarize_code ![function](https://img.shields.io/badge/function-green?style=flat)

- **Defined on lines:** 83–124
- **Symbol kind:** function

### Purpose
A function for summarizing code symbols in multiple chunks.

### Details
This function takes an `Input` object as input and generates text using the Ollama API to summarize the code symbols. If the code is too long, it splits it into multiple chunks and summarizes each chunk separately.

### Usage
To use this function, you need to create an instance of it and call its `summarize_code` method with an `Input` object as input.

---