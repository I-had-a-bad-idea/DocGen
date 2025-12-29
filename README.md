# Docgen

Generate documentation files from your source code. 

## Overview
- [Docgen](#docgen)
  - [Overview](#overview)
  - [Installation](#installation)
    - [Python Dependencies](#python-dependencies)
    - [Olama + Model](#olama--model)
  - [Usage](#usage)
  - [License](#license)

---

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

ollama pull gemma3:4b-it-q8_0

```

---

## Usage

```bash

python main.py <path_to_folder>

```


## License

MIT License. See [LICENSE](LICENSE) for details.