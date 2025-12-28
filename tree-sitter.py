from tree_sitter_language_pack import get_parser
from pathlib import Path

LANGUAGES = {
    ".py": "python",
    ".rs": "rust",
}

_PARSERS = {}

def parse_code(code: str, language_name):
    if not language_name:
        raise ValueError("Unsupported language")

    parser = get_cached_parser(language_name)

    # Parse code
    tree = parser.parse(code.encode("utf-8"))

    return tree.root_node

def get_cached_parser(language_name):
    if language_name not in _PARSERS:
        _PARSERS[language_name] = get_parser(language_name)

    return _PARSERS[language_name]

def parse_file(file_path: str):
    path = Path(file_path)
    language_name = LANGUAGES.get(path.suffix)

    if not language_name:
        raise ValueError(f"Unsupported file type: {path.suffix}")

    code = path.read_text(encoding="utf-8")

    root_node = parse_code(code, language_name)

    return root_node

def print_tree(node, indent=0):
    print("  " * indent + f"{node.type}")
    for child in node.children:
        print_tree(child, indent + 1)

if __name__ == "__main__":
    root_node = parse_file("test_files/test.py")
    print_tree(root_node)