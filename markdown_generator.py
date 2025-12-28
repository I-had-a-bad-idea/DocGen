from typing import List
from pathlib import Path
from datetime import datetime
from code_structure_extractor import Symbol

def generate_markdown_from_symbols(file_path: str, symbols: List[Symbol]) -> str:

    md_lines = []

    # Header
    md_lines.append(f"# Documentation for `{Path(file_path).name}`")
    md_lines.append(f"> _Generated on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}_\n")

    # Overview
    md_lines.append("## Overview")
    md_lines.append("This file contains the following symbols and definitions.")
    md_lines.append("")

    # Symbols
    md_lines.append("## Symbols")

    for s in symbols:
        md_lines.append(f"### {s.name}")
        
        md_lines.append(f"- is a {s.kind}")
        if s.parent:
            md_lines.append(f"- parent: {s.parent}")
        md_lines.append(f"- defined on line {s.start_line}")
        
        md_lines.append("") # Spacing
    
    md =  "\n".join(md_lines)

    return md

def save_markdown(file_path: str, markdown_content: str, output_dir: str = "docs"):

    output_path = Path(output_dir)
    output_path.mkdir(exist_ok=True)

    md_file = Path(f"{output_path}/{Path(file_path).stem}.md")
    md_file.write_text(markdown_content, encoding="utf-8")

def generate_markdown(file_path: str, symbols: List[Symbol]):

    md = generate_markdown_from_symbols(file_path, symbols)

    save_markdown(file_path, md)

    