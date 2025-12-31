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
  - [License](#license)

---

## Features

- Supports multiple programming languages (Python, JavaScript, TypeScript, Go, Rust, Java, C, C++, C#, PHP, Ruby, HTML, CSS, Shell Script, and more).
- Generates comprehensive Markdown documentation files.
- Utilizes local LLM via Ollama for code understanding.
- Easy to use command-line interface.
- [Example Output](docs/llm_summary.md)

## Installation

### Python Dependencies

Install python dependencies

```bash

pip install tree_sitter_language-pack datetime ollama tqdm pydantic

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


## License

MIT License. See [LICENSE](LICENSE) for details.