from ollama import AsyncClient
from pydantic import BaseModel
import json
from tqdm import tqdm

MODEL = "qwen2.5-coder:3b"

BASE_PROMPT = """
You are given structured JSON describing code symbols.

For EACH symbol:
- Analyze the code
- Produce a high-level and a low-level summary
- Do NOT keep the code
- Do NOT invent new symbols

Return ONLY valid JSON matching this schema:

{
  "symbols": [
    {
      "name": "the_symbol_name",
      "kind": "the_symbol_lo",
      "start_line": 0,
      "parent": "",
      "high_level_summary": "",
      "low_level_summary": ""
    }
  ]
}

Return JSON only. No markdown. No explanations.
"""

class SymbolOutput(BaseModel):
    name: str
    kind: str
    start_line: int
    parent: str
    high_level_summary: str
    low_level_summary: str

class Documentation(BaseModel):
    symbols: list[SymbolOutput]

class SymbolInput(BaseModel):
    name: str
    kind: str
    start_line: int
    parent: str
    code: str

class Input(BaseModel):
    symbols: list[SymbolInput]


ollama = AsyncClient()

OPTIONS = {
    "temperature": 0.1,

}

async def summarize_code_in_chunk(input: Input) -> Documentation:
    prompt = BASE_PROMPT + "\n\nINPUT:\n\n" + input.model_dump_json(indent=2)
    resp = await ollama.generate(MODEL,
                                 prompt=prompt,
                                 options=OPTIONS,
                                 format="json")

    response = Documentation.model_validate_json(resp.response)

    return response

async def summarize_code_in_markdown(input: Input) -> Documentation:
    chunk_size = 5
    doc = Documentation(symbols=[])

    # Split input.symbols into chunks of size 5
    for i in tqdm(range(0, len(input.symbols), chunk_size), desc="Processing chunks", unit=" chunk"):
        chunk = input.symbols[i:i + chunk_size]
        chunk_input = Input(symbols=chunk)
        summary = await summarize_code_in_chunk(chunk_input)
        doc.symbols.extend(summary.symbols)

    return doc
