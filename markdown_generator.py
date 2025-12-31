from pathlib import Path
from datetime import datetime
from llm_summary import summarize_code_in_markdown, Documentation, Input

async def generate_markdown_from_symbols_async(file_path: str, code: str) -> str:

    # Header
    header_lines = []
    header_lines.append(f"# **Documentation for `{Path(file_path).name}`**")
    header_lines.append(f"> _Generated on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}_\n")
    header_lines.append(f"> _Generated with [DocGen](https://github.com/I-had-a-bad-idea/DocGen), may include wrong information!_\n\n")

    input = Input(code=code, file_path=file_path)
    # for s in symbols:
    #     symbol = SymbolInput(name=s.name,
    #                          kind=s.kind,
    #                          start_line=s.start_line,
    #                          parent=s.parent if s.parent else "",
    #                          code=s.code)
    #     input.symbols.append(symbol)
    
    # input.symbols.sort(key=lambda s: s.start_line)

    header = "\n".join(header_lines)

    doc = await summarize_code_in_markdown(input)

    md = generate_markdown_from_doc(doc, header)

    return md

def generate_markdown_from_doc(doc: Documentation, header: str) -> str:
    md_lines = [header, ""]  # Start with header and a blank line

    doc.symbols.sort(key=lambda s: s.start_line)

    # # Create a table of contents 
    # md_lines.append("# Table of Contents\n")
    # for s in doc.symbols:
    #     # Create an anchor-friendly name (for clickable links)
    #     anchor = s.name.lower().replace(" ", "-")
    #     md_lines.append(f"- [{s.name}](#{anchor}) `{s.kind}`")
    # md_lines.append("\n---\n")  # separator before detailed sections
    
    # Overview
    md_lines.append("# Overview")
    md_lines.append(doc.overview)

    # Symbols
    md_lines.append("# Symbols")
    md_lines.append("") # Spacing

    # Helper to create a colored badge for kind
    def kind_badge(kind: str) -> str:
        colors = {
            "class": "blue",
            "function": "green",
            "variable": "orange",
        }
        color = colors.get(kind.lower(), "gray")
        return f"<span style='background-color:{color}; color:white; padding:2px 6px; border-radius:4px;'>{kind}</span>"

    for s in doc.symbols:
        # Create an anchor for linking from overview
        anchor = s.name.lower().replace(" ", "-")
        md_lines.append(f"<a id='{anchor}'></a>")
        md_lines.append(f"<details style='margin-bottom: 10px;'>")
        md_lines.append(f"  <summary> **{s.name}** {kind_badge(s.kind)}</summary>\n")
        md_lines.append(f"  - **Defined on line:** `<code>{s.start_line}</code>`")
        if s.parent:
            md_lines.append(f"  - **Parent:** `<code>{s.parent}</code>`")
        md_lines.append("")  # blank line before summaries

        md_lines.append(f"  <h4>High-Level Summary</h4>")
        md_lines.append(f"  <p>{s.high_level_summary}</p>")

        md_lines.append(f"  <h4>Low-Level Summary</h4>")
        md_lines.append(f"  <p>{s.low_level_summary}</p>")

        md_lines.append(f"</details>")
        md_lines.append("<hr>")  # horizontal rule between symbols

    return "\n".join(md_lines)


def save_markdown(file_path: str, markdown_content: str, output_dir: str = "docs"):

    output_path = Path(output_dir)
    output_path.mkdir(exist_ok=True)

    md_file = Path(f"{output_path}/{Path(file_path).stem}.md")
    md_file.write_text(markdown_content, encoding="utf-8")

async def generate_markdown(file_path: str, code: str):

    md = await generate_markdown_from_symbols_async(file_path, code)
    save_markdown(file_path, md)

    
