from tree_sitter_language_pack import get_parser
from pathlib import Path
from dataclasses import dataclass
from typing import Optional, List
from tqdm import tqdm

LANGUAGES = {
    ".py": "python",
    ".rs": "rust",
}

_PARSERS = {}

EXTRACTION_RULES = {
    "python": {
        "class": "class_definition",
        "function": "function_definition",
        "variable": "assignment",
    },
    "rust": {
        "class": ["struct_item", "enum_item"],
        "function": "function_item",
        "variable": "constant_item",
    },
}

errors : list[str] = []

@dataclass
class Symbol:
    name: str
    kind: str
    parent: Optional[str]
    start_line: int
    code: str

def parse_code(code: str, language_name):
    if not language_name:
        errors.append("Unsupported language")
        return

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
        errors.append(f"Unsupported file type: {path.suffix}")
        return None, None, None

    code = path.read_text(encoding="utf-8")

    root_node = parse_code(code, language_name)

    return root_node, language_name, code

def extract_symbols(node, language_name, code, parent=None) -> List[Symbol]:
    if not node:
        return []
    
    symbols: List[Symbol] = []
    rules = EXTRACTION_RULES[language_name]

    node_type = node.type
    name_node = node.child_by_field_name("name")
    start_point = node.start_point[0] + 1
    code_snippet = code[node.start_byte-1:node.end_byte-2]


    # Class detection
    class_types = rules["class"]
    if isinstance(class_types, str): 
        class_types = [class_types] # Make list

    if node_type in class_types and name_node:
        name = name_node.text.decode()
        symbols.append(Symbol(name, "class", parent, start_point, code_snippet))
        parent = name   # update parent context

    # Function detection
    function_types = rules["function"]
    if isinstance(function_types, str):
        function_types = [function_types] # Make list

    if node_type in function_types and name_node:
        name = name_node.text.decode()
        symbols.append(Symbol(name, "function", parent, start_point, code_snippet))
        parent = name   # update parent context

    # Variable detection (only top-level)
    variable_types = rules["variable"]
    if isinstance(variable_types, str):
        variable_types = [variable_types]
    
    if node_type in variable_types and parent is None:
        name_node = node.child_by_field_name("left") or name_node

        if name_node:
            name = name_node.text.decode()
            symbols.append(Symbol(name, "variable", None, start_point, code_snippet))
    
    # Traverse children
    for child in node.children:
        symbols.extend(extract_symbols(child, language_name, code, parent))

    return symbols

def print_symbols(symbols: List[Symbol]):
    for s in symbols:
        parent = f"(parent: {s.parent})" if s.parent else ""
        tqdm.write(f"{s.kind:8} {s.name} {parent} [line {s.start_line}] (code: {s.code})")

def print_tree(node, indent=0):
    tqdm.write("  " * indent + f"{node.type}")
    for child in node.children:
        print_tree(child, indent + 1)

def code_structure_of_file(path: str):
    root_node, language_name, code = parse_file(path)
    symbols = extract_symbols(root_node, language_name, code)
    with open("errors.log", "w") as f:
        f.write("\n".join(errors))
    return symbols
