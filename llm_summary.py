from ollama import AsyncClient
from pydantic import BaseModel

MODEL = "deepseek-r1:1.5b"

BASE_PROMPT = """
You are given structured JSON describing code symbols.

For EACH symbol:
- Analyze the `code`
- Produce a detailed high-level summary
- Produce a very detailed low-level summary
- Do NOT invent new symbols
- Do NOT modify existing fields

Return ONLY valid JSON matching this schema:

{
  "symbols": [
    {
      "name": "...",
      "kind": "...",
      "start_line": 0,
      "parent": "..." or "",
      "high_level_summary": "...",
      "low_level_summary": "..."
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
    "temperature": 0.25,
    "top_p": 0.5,
    "repeat_penalty": 1.5,
    "seed": 42,

}

async def summarize_code_in_markdown(input: Input) -> Documentation:
    prompt = BASE_PROMPT + "\n\nINPUT:\n\n" + input.model_dump_json(indent=2)
    resp = await ollama.generate(MODEL,
                                 prompt=prompt,
                                 options=OPTIONS,
                                 format=Documentation.model_json_schema())
    
    response = Documentation.model_validate_json(resp.response)

    return response
