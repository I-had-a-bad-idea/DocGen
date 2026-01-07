# DocGen

If you are too lazy to manually write docs for your code, look no further.

DocGen automatically generates documentation files from your source code.
It uses local Ollama to understand your code and create Markdown files for them.

## Overview
- [DocGen](#docgen)
  - [Overview](#overview)
  - [Features](#features)
  - [Installation](#installation)
    - [Python Dependencies](#python-dependencies)
    - [Olama + Model](#olama--model)
  - [Usage](#usage)
  - [Ignoring Languages And Folders](#ignoring-languages-and-folders)
  - [License](#license)

---

## Features

- Supports multiple programming languages (Python, JavaScript, TypeScript, Go, Rust, Java, C, C++, C#, PHP, HTML, CSS and more).
- Generates comprehensive Markdown documentation files.
- Utilizes local LLM via Ollama for code understanding.
- Easy to use command-line interface.
- [Example Output](docs/llm_summary.md)
- Supports ignoring specific languages or folders using a `.docgen_ignore` file

## Installation

### Python Dependencies

Install python dependencies

```bash

pip install datetime ollama tqdm pydantic

```
### Olama + Model

Install ollama from [here](https://ollama.com/download).

Download the model:

```bash

ollama pull qwen2.5-coder:3b

```

You need around 3500MB of VRAM in the default configuration.

If you dont have this much you can reduce the required amount by reducing the `MAX_CONTEXT` in `llm_summary.py`.

---

## Usage

```bash

python main.py <path_to_folder>

```

DocGen will gett all supported files in the folder and its subfolders.      
Then it will pass their code through a local LLM and construct a Markdown file.        
You can extend the accepted languages in the `LANGUAGES` dict in `main.py`.          


## Ignoring Languages And Folders

Create a `.docgen_ignore` file in the root of your project.
To ignore specific languages, add their file extensions (e.g. `.py`, `.js`) to the file.
To ignore specific folders, add their folder names (e.g. `node_modules/`, `venv/`) to the file.

DocGen will skip files with the specified extensions and any files located in the specified folders during documentation generation.

## License

MIT License. See [LICENSE](LICENSE) for details.