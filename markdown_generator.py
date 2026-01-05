from pathlib import Path
from datetime import datetime
from llm_summary import summarize_code, Documentation, Input

async def generate_markdown_from_symbols_async(file_path: str, code: str) -> str:

    # Header
    header_lines = []
    header_lines.append(f"# **Documentation for `{Path(file_path).name}`**")
    header_lines.append(f"> _Generated on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}_\n")
    header_lines.append(f"> _Generated with [DocGen](https://github.com/I-had-a-bad-idea/DocGen), may include wrong information!_\n\n")

    input = Input(code=code, file_path=file_path)

    header = "\n".join(header_lines)

    doc = await summarize_code(input)

    md = generate_markdown_from_doc(doc, header)

    return md

def generate_markdown_from_doc(doc: Documentation, header: str) -> str:
    md_lines = [header, ""]  # Start with header and a blank line

    doc.symbols.sort(key=lambda s: s.start_line)

    # # Create a table of contents 
    md_lines.append("# Table of Contents\n")
    for s in doc.symbols:
        slug = (s.name).lower().replace(" ", "-")
        md_lines.append(f"- [{s.name} {kind_badge(s.kind)}](#{slug})")
    md_lines.append("\n---\n")
    
    # Overview
    md_lines.append("# Overview")
    md_lines.append(doc.overview + "\t\t\t")
    md_lines.append(f"**Language**: {doc.language}\n")
    md_lines.append("## Key components")
    md_lines.append(",\n".join(doc.key_components))
    md_lines.append("## Requirements")
    md_lines.append(",\n".join(doc.requirements))
    md_lines.append("## Usage")
    md_lines.append(doc.usage)
    md_lines.append("\n---\n")  # separator before detailed sections

    # Symbols
    md_lines.append("")
    md_lines.append("# Symbols")
    md_lines.append("") # Spacing

    for s in doc.symbols:
        md_lines.extend(generate_md_for_symbol(s))

    return "\n".join(md_lines)


def generate_md_for_symbol(s) -> list[str]:
    md = []

    # Strong heading
    md.append(f"\n## {s.name} {kind_badge(s.kind)}")
    md.append("")

    # Metadata block
    if s.start_line == s.end_line:
        md.append(f"- **Defined on line:** {s.start_line}")
    else:
        md.append(f"- **Defined on lines:** {s.start_line}–{s.end_line}")

    if s.parent:
        md.append(f"- **Parent:** {s.parent}")

    md.append(f"- **Symbol kind:** {s.kind}")
    md.append("")

    # Semantic sections
    md.append("### Purpose")
    md.append(s.purpose or "Not specified.")
    md.append("")

    md.append("### Details")
    md.append(s.details or "Not specified.")
    md.append("")

    md.append("### Usage")
    md.append(s.usage or "Not specified.")
    md.append("")

    if s.limitations:
        md.append("### Limitations")
        md.append("\n".join(f"- {l}" for l in s.limitations))
        md.append("")

    md.append("---")
    return md

# Helper to create a colored badge for kind
def kind_badge(kind: str) -> str:
    colors = {
        "variable": "blue",
        "function": "green",
        "class": "purple",
        "enum": "orange",
        "struct": "teal",
        "module": "brown"
    }
    color = colors.get(kind.lower(), "gray")
    return f"![{kind}](https://img.shields.io/badge/{kind}-{color}?style=flat)"


def save_markdown(file_path: str, markdown_content: str, output_dir: str = "docs"):

    output_path = Path(output_dir)
    output_path.mkdir(exist_ok=True)

    md_file = Path(f"{output_path}/{Path(file_path).stem}.md")
    md_file.write_text(markdown_content, encoding="utf-8")

async def generate_markdown(file_path: str, code: str):

    md = await generate_markdown_from_symbols_async(file_path, code)
    save_markdown(file_path, md)

    
