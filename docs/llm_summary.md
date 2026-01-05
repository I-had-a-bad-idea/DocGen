# **Documentation for `llm_summary.py`**
> _Generated on 2026-01-05 12:16:07_

> _Generated with [DocGen](https://github.com/I-had-a-bad-idea/DocGen), may include wrong information!_



# Table of Contents

- [AsyncClient (class)](#asyncclient-class)
- [BaseModel (class)](#basemodel-class)
- [tqdm_asyncio (module)](#tqdm_asyncio-module)
- [json (module)](#json-module)
- [SymbolOutput (class)](#symboloutput-class)
- [Documentation (class)](#documentation-class)
- [Input (class)](#input-class)
- [MAX_CONTEXT (variable)](#max_context-variable)
- [ollama (variable)](#ollama-variable)
- [OPTIONS (variable)](#options-variable)
- [summarize_code_in_chunk (function)](#summarize_code_in_chunk-function)
- [summarize_code (function)](#summarize_code-function)

---

# Overview
This script is designed to summarize structured JSON describing code symbols using the Ollama AI model.			
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
To use this script, you need to have the Ollama AI model installed and running. You can then call the `summarize_code` function with an `Input` object containing the file path and code as arguments.

---


# Symbols


## AsyncClient (class)

- **Defined on line:** 1
- **Symbol kind:** class

### Purpose
An asynchronous client for interacting with Ollama AI models.

### Details
This class is used to connect to the Ollama AI model and send requests for generating text based on prompts.

### Usage
To use this class, you need to create an instance of it and call its methods to generate text.




## BaseModel (class)

- **Defined on line:** 3
- **Symbol kind:** class

### Purpose
A base class for Pydantic models, which are used to define data structures with type annotations.

### Details
This class is used to define the structure of the `SymbolOutput`, `Documentation`, and `Input` classes.

### Usage
To use this class, you need to create an instance of it and call its methods to validate and serialize data.




## tqdm_asyncio (module)

- **Defined on line:** 4
- **Symbol kind:** module

### Purpose
A module that provides a progress bar for asynchronous operations using the tqdm library.

### Details
This module is used to display a progress bar while summarizing code in chunks.

### Usage
To use this module, you need to import it and call its functions to create a progress bar.




## json (module)

- **Defined on line:** 5
- **Symbol kind:** module

### Purpose
A module that provides functions for encoding and decoding JSON data.

### Details
This module is used to parse the response from the Ollama AI model and serialize it into a `Documentation` object.

### Usage
To use this module, you need to import it and call its functions to encode and decode JSON data.




## SymbolOutput (class)

- **Defined on lines:** 7–13
- **Symbol kind:** class

### Purpose
A Pydantic model that represents the output of summarizing a code symbol.

### Details
This class is used to define the structure of the `SymbolOutput` object, which contains information about a code symbol such as its name, kind, start line, end line, parent, purpose, details, usage, and limitations.

### Usage
To use this class, you need to create an instance of it and call its methods to validate and serialize data.




## Documentation (class)

- **Defined on lines:** 15–24
- **Symbol kind:** class

### Purpose
A Pydantic model that represents the documentation of a code summary.

### Details
This class is used to define the structure of the `Documentation` object, which contains information about the overall purpose of the file, language, key components, requirements, usage, and symbols.

### Usage
To use this class, you need to create an instance of it and call its methods to validate and serialize data.




## Input (class)

- **Defined on lines:** 26–35
- **Symbol kind:** class

### Purpose
A Pydantic model that represents the input to the summarization function.

### Details
This class is used to define the structure of the `Input` object, which contains information about the file path and code.

### Usage
To use this class, you need to create an instance of it and call its methods to validate and serialize data.




## MAX_CONTEXT (variable)

- **Defined on line:** 37
- **Symbol kind:** variable

### Purpose
The maximum context size for summarizing code in chunks.

### Details
This variable is used to determine the maximum number of characters that can be processed by the Ollama AI model at once.

### Usage
To use this variable, you need to set its value before calling the `summarize_code` function.




## ollama (variable)

- **Defined on line:** 39
- **Symbol kind:** variable

### Purpose
An instance of the AsyncClient class for interacting with the Ollama AI model.

### Details
This variable is used to send requests to the Ollama AI model and receive responses.

### Usage
To use this variable, you need to create an instance of it before calling the `summarize_code` function.




## OPTIONS (variable)

- **Defined on lines:** 41–43
- **Symbol kind:** variable

### Purpose
The options for generating text using the Ollama AI model.

### Details
This variable is used to specify the temperature and context size for generating text.

### Usage
To use this variable, you need to set its value before calling the `summarize_code` function.




## summarize_code_in_chunk (function)

- **Defined on lines:** 45–62
- **Symbol kind:** function

### Purpose
A function that summarizes a code chunk using the Ollama AI model.

### Details
This function takes an `Input` object as input and sends a request to the Ollama AI model to generate text based on a prompt. The response is then parsed and serialized into a `Documentation` object.

### Usage
To use this function, you need to call it with an `Input` object containing the file path and code as arguments.




## summarize_code (function)

- **Defined on lines:** 64–103
- **Symbol kind:** function

### Purpose
A function that summarizes a code file using the Ollama AI model.

### Details
This function takes an `Input` object as input and checks if the length of the code is greater than the maximum context size. If it is, the code is split into chunks and summarized in parallel using the `summarize_code_in_chunk` function. The results are then combined into a single `Documentation` object.

### Usage
To use this function, you need to call it with an `Input` object containing the file path and code as arguments.


