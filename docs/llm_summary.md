# **Documentation for `llm_summary.py`**
> _Generated on 2026-01-06 14:19:59_

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
This file provides a function to summarize code symbols using the Ollama AI model.			
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
tqdm.asyncio library
## Usage
To use this file, you need to have the Ollama AI model installed and running. You can then call the `summarize_code` function with an `Input` object containing the file path and code as arguments.

---


# Symbols


## SymbolOutput ![class](https://img.shields.io/badge/class-purple?style=flat)

- **Defined on lines:** 12–30
- **Symbol kind:** class

### Purpose
A Pydantic model to represent the output of a symbol summary.

### Details
This class has fields for the name, kind, start line, end line, parent, purpose, details, usage, and limitations of a symbol.

### Usage
To use this class, you can create an instance with the desired values and then access its fields as needed.

---

## Documentation ![class](https://img.shields.io/badge/class-purple?style=flat)

- **Defined on lines:** 32–48
- **Symbol kind:** class

### Purpose
A Pydantic model to represent the documentation of a code summary.

### Details
This class has fields for the overview, language, key components, requirements, usage, and symbols of a code summary.

### Usage
To use this class, you can create an instance with the desired values and then access its fields as needed.

---

## Input ![class](https://img.shields.io/badge/class-purple?style=flat)

- **Defined on lines:** 49–58
- **Symbol kind:** class

### Purpose
A Pydantic model to represent the input for a code summary.

### Details
This class has fields for the file path and code of a code summary.

### Usage
To use this class, you can create an instance with the desired values and then access its fields as needed.

---

## MAX_CONTEXT ![variable](https://img.shields.io/badge/variable-blue?style=flat)

- **Defined on lines:** 60–61
- **Symbol kind:** variable

### Purpose
The maximum context size for the Ollama AI model.

### Details
This variable is used to determine how much code can be processed at once by the Ollama AI model.

### Usage
To use this variable, you can access its value directly or modify it as needed.

---

## ollama ![variable](https://img.shields.io/badge/variable-blue?style=flat)

- **Defined on lines:** 63–64
- **Symbol kind:** variable

### Purpose
An instance of the Ollama AI client.

### Details
This variable is used to interact with the Ollama AI model and generate summaries of code symbols.

### Usage
To use this variable, you can access its methods and properties as needed.

---

## OPTIONS ![variable](https://img.shields.io/badge/variable-blue?style=flat)

- **Defined on lines:** 65–70
- **Symbol kind:** variable

### Purpose
The options for the Ollama AI model.

### Details
This variable is used to configure the behavior of the Ollama AI model when generating summaries of code symbols.

### Usage
To use this variable, you can access its values directly or modify it as needed.

---

## summarize_code_in_chunk ![function](https://img.shields.io/badge/function-green?style=flat)

- **Defined on lines:** 72–104
- **Symbol kind:** function

### Purpose
A function to summarize a chunk of code symbols using the Ollama AI model.

### Details
This function takes an `Input` object as input and generates a summary of the code symbols in that chunk using the Ollama AI model. It returns a `Documentation` object containing the summary.

### Usage
To use this function, you can create an `Input` object with the desired values and then call the function with it.

---

## summarize_code ![function](https://img.shields.io/badge/function-green?style=flat)

- **Defined on lines:** 106–145
- **Symbol kind:** function

### Purpose
A function to summarize a code summary using the Ollama AI model.

### Details
This function takes an `Input` object as input and generates a summary of the code symbols in that code summary using the Ollama AI model. It returns a `Documentation` object containing the summary.

### Usage
To use this function, you can create an `Input` object with the desired values and then call the function with it.

---