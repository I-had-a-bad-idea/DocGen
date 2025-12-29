from typing import List
from pathlib import Path
from datetime import datetime
from code_structure_extractor import Symbol
from llm_summary import summarize_code_in_markdown, Documentation, Input, SymbolInput

async def generate_markdown_from_symbols_async(file_path: str, symbols: List[Symbol]) -> str:

    # Header
    header_lines = []
    header_lines.append(f"# **Documentation for `{Path(file_path).name}`**")
    header_lines.append(f"> _Generated on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}_\n")
    header_lines.append(f"> _Generated with DocGen, may include wrong information!_\n\n")
    
    # Overview
    header_lines.append("# Overview")
    header_lines.append("This file contains the following symbols and definitions.")
    header_lines.append("")

    # Symbols
    header_lines.append("# Symbols")
    header_lines.append("") # Spacing

    input = Input(symbols=[])
    for s in symbols:
        symbol = SymbolInput(name=s.name,
                             kind=s.kind,
                             start_line=s.start_line,
                             parent=s.parent if s.parent else "",
                             code=s.code)
        input.symbols.append(symbol)

    header = "\n".join(header_lines)

    doc = await summarize_code_in_markdown(input)

    md = generate_markdown_from_doc(doc, header)

    return md

def generate_markdown_from_doc(doc: Documentation, header):
    md_lines = []

    for s in doc.symbols:
        md_lines.append(f"<details>\n<summary>**{s.name}** ({s.kind})</summary>\n")
        md_lines.append(f"- **Defined on line:** {s.start_line}")
        if s.parent:
            md_lines.append(f"- **Parent:** {s.parent}")
        md_lines.append("")
        md_lines.append("### High-Level Summary")
        md_lines.append(s.high_level_summary)
        md_lines.append("")
        md_lines.append("### Low-Level Summary")
        md_lines.append(s.low_level_summary)
        md_lines.append("</details>\n")

    md = header + "\n".join(md_lines)
    return md


def save_markdown(file_path: str, markdown_content: str, output_dir: str = "docs"):

    output_path = Path(output_dir)
    output_path.mkdir(exist_ok=True)

    md_file = Path(f"{output_path}/{Path(file_path).stem}.md")
    md_file.write_text(markdown_content, encoding="utf-8")

async def generate_markdown(file_path: str, symbols: List[Symbol]):

    md = await generate_markdown_from_symbols_async(file_path, symbols)
    save_markdown(file_path, md)

    