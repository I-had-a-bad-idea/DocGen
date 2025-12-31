from ollama import AsyncClient
from pydantic import BaseModel
from tqdm.asyncio import tqdm_asyncio
import json

MODEL = "qwen2.5-coder:3b"

BASE_PROMPT = """
You are given structured JSON describing code symbols.

For EACH symbol:
- Analyze the code
- Produce a high-level and a detailed low-level summary
- Do NOT keep the code
- Do NOT invent new symbols

Return ONLY valid JSON matching this schema:

{
  "overview": "an_overview_of_the_file",
  "language:" "the_language_of_the_file",
  "symbols": [
    {
      "name": "the_symbol_name",
      "kind": "the_symbol_lo",
      "start_line": 0,
      "end_line": 0,
      "parent": "",
      "high_level_summary": "",
      "low_level_summary": ""
      "examples": [""]
      "notes":  "some_notes"
    }
  ]
}

Examples should be an array of strings or empty.

Return JSON only. No markdown. No explanations.
"""

class SymbolOutput(BaseModel):
    name: str
    kind: str
    start_line: int
    end_line: int
    parent: str
    high_level_summary: str
    low_level_summary: str
    examples: list[str] | None
    notes: str | None

class Documentation(BaseModel):
    overview: str
    language: str
    symbols: list[SymbolOutput]

class Input(BaseModel):
    file_path: str
    code: str

MAX_TOKENS = 32768 # 32.768

ollama = AsyncClient()

OPTIONS = {
    "temperature": 0.1,
    "num_ctx": MAX_TOKENS, 

}

async def summarize_code_in_chunk(input: Input) -> Documentation:
    prompt = BASE_PROMPT + "\n\nINPUT:\n\n" + input.model_dump_json(indent=2)
    resp = await ollama.generate(MODEL,
                                 prompt=prompt,
                                 options=OPTIONS,
                                 format="json")
    
    # parsed = json.loads(resp.response)
    # with open("model_answers.log", "a") as f:
    #     json.dump(parsed, f, indent=2)
    #     f.write("\n")

    response = Documentation.model_validate_json(resp.response)

    return response

async def summarize_code_in_markdown(input: Input) -> Documentation:
    code = input.code
    if len(code) > MAX_TOKENS:
        codes = [
            Input(file_path=input.file_path,
                  code=code[i:i+MAX_TOKENS])
            for i in range(0, len(code), MAX_TOKENS)
        ]
    
        doc = Documentation(overview="",
                            symbols=[], language="")
        for chunk_input in tqdm_asyncio(codes, desc="Summarizing code chunks", unit="chunk"):
            chunk_doc = await summarize_code_in_chunk(chunk_input)
            doc.overview += chunk_doc.overview + "\n"
            doc.symbols.extend(chunk_doc.symbols)
        
        return doc
    
    return await summarize_code_in_chunk(input)

