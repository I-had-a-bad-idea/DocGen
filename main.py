import sys
import os
from markdown_generator import generate_markdown
from tqdm import tqdm
from tqdm.asyncio import tqdm_asyncio
import asyncio
from pathlib import Path

queue = set()

LANGUAGES = {
    # Python
    ".py": "Python",
    ".pyw": "Python",
    ".pyi": "Python (type hints)",

    # Rust
    ".rs": "Rust",

    # JavaScript
    ".js": "JavaScript",
    ".mjs": "JavaScript (ES modules)",
    ".cjs": "JavaScript (CommonJS)",

    # TypeScript
    ".ts": "TypeScript",
    ".tsx": "TypeScript (React)",
    ".d.ts": "TypeScript (declarations)",

    # Go
    ".go": "Go",

    # Java
    ".java": "Java",
    ".jar": "Java (archive)",
    ".class": "Java (bytecode)",

    # C
    ".c": "C",
    ".h": "C/C++ header",

    # C++
    ".cpp": "C++",
    ".cc": "C++",
    ".cxx": "C++",
    ".hpp": "C++ header",
    ".hh": "C++ header",
    ".hxx": "C++ header",

    # C#
    ".cs": "C#",
    ".csproj": "C# project",

    # PHP
    ".php": "PHP",
    ".phtml": "PHP",

    # Ruby
    ".rb": "Ruby",
    ".erb": "Ruby (ERB templates)",
    ".rake": "Ruby (Rake)",

    # Web
    ".html": "HTML",
    ".htm": "HTML",
    ".css": "CSS",
    ".scss": "CSS (Sass)",
    ".sass": "CSS (Sass)",
    ".less": "CSS (Less)",

    # Shell
    ".sh": "Shell",
    ".bash": "Bash",
    ".zsh": "Zsh",

    # Other common languages
    ".kt": "Kotlin",
    ".kts": "Kotlin (script)",
    ".swift": "Swift",
    ".lua": "Lua",
    ".pl": "Perl",
    ".pm": "Perl module",
    ".dart": "Dart",
    ".r": "R",
    ".m": "Objective-C / MATLAB",
    ".mm": "Objective-C++",

    # Data / config / markup
    ".json": "JSON",
    ".yaml": "YAML",
    ".yml": "YAML",
    ".xml": "XML",
    ".toml": "TOML",
    ".ini": "INI",
    ".cfg": "Config",
    ".md": "Markdown",
    ".sql": "SQL"
}

def is_supported_language(file_path: str) -> bool:
    path = Path(file_path)
    suffix = path.suffix
    return LANGUAGES.get(suffix) != None

def get_code_from_file(file_path: str) -> str:
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            code = f.read()
        return code
    except Exception as e:
        print(f"Error reading file {file_path}: {e}")
        return ""

async def generate_docs_for_file(file_path):
    if not os.path.isfile(file_path):
        print("Not a file")
        return

    code = get_code_from_file(file_path)
    if code:
        await generate_markdown(file_path, code)


async def get_files_for_folder(folder_path):
    if not os.path.isdir(folder_path):
        print("Not a folder")
        return
    
    elements = os.listdir(folder_path)
    
    for element in tqdm(elements, desc=f"Getting files in {folder_path}", unit="item"):
        element_path = os.path.join(folder_path, element)

        if os.path.isfile(element_path):
            if is_supported_language(element_path):
                queue.add(element_path)
        elif os.path.isdir(element_path):
            await get_files_for_folder(element_path)


async def get_files_for_path(path):
    if os.path.isdir(path):
        await get_files_for_folder(path)
    elif os.path.isfile(path):
        if is_supported_language(path):
            queue.add(path)

async def generate_docs():
    tasks = [generate_docs_for_file(path) for path in queue]

    for task in tqdm_asyncio.as_completed(tasks, total=len(tasks), desc="Processing files", unit="file"):
        await task

def main():
    if len(sys.argv) >= 2:
        path = sys.argv[1]
        asyncio.run(get_files_for_path(path))
        asyncio.run(generate_docs())
        print("\n\nGenerated docs!")
    else:
        print("Usage: python main.py path_to_folder")


if __name__ == "__main__":
    main()