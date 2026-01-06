from ollama import AsyncClient
from pydantic import BaseModel
from tqdm.asyncio import tqdm_asyncio
import json

MODEL = "qwen2.5-coder:3b"

BASE_PROMPT = """
You are given structured JSON describing code symbols.

Look at every single symbol. Every variable, function, class, etc.
For EACH symbol:
- Analyze the code
- Fill out the JSON below.
- Do NOT keep the code
- Do NOT invent new symbols
- Always write details
- Key components should not be all symbols!
- Usage should contain code if it makes sense
- Someone new to the project must understand it.
- The definition should show the variable, function, class definition, without the body. ONLY the actual definition, NO body.


Return ONLY valid JSON matching this schema:

{
  "overview": "the_purpose_of_the_file",
  "language": "the_language_of_the_file",
  "key_components": ["the_key_components_of_the_file"],
  "requirements": ["the_requirements_of_the_file"],
  "usage": "how_to_use_the_file",
  "symbols": [
    {
      "name": "the_symbol_name",
      "kind": "the_symbol_type",
      "start_line": 0,
      "end_line": 0,
      "definition": "some_code",
      "parent": "",
      "purpose": "",
      "details": "",
      "usage":  "how_to_use_it",
      "limitations": ["limitations"],
    }
  ]
}


Return JSON only. No markdown. No explanations.
"""

class SymbolOutput(BaseModel):
    name: str
    kind: str
    start_line: int
    end_line: int
    definition: str
    parent: str
    purpose: str
    details: str
    usage: str
    limitations: list[str]

class Documentation(BaseModel):
    overview: str
    language: str
    key_components: list[str]
    requirements: list[str]
    usage: str
    symbols: list[SymbolOutput]

class Input(BaseModel):
    file_path: str
    code: str

MAX_CONTEXT = 32768 # 32.768 tokens

ollama = AsyncClient()

OPTIONS = {
    "temperature": 0.1,
    "num_ctx": MAX_CONTEXT, 

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

async def summarize_code(input: Input) -> Documentation:
    code = input.code
    if len(code) > MAX_CONTEXT:
        codes = [
            Input(file_path=input.file_path,
                  code=code[i:i+MAX_CONTEXT])
            for i in range(0, len(code), MAX_CONTEXT)
        ]
    
        doc = Documentation(overview="",
                            symbols=[], language="", key_components=[], requirements=[], usage="")
        for chunk_input in tqdm_asyncio(codes, desc="Summarizing code chunks", unit="chunk"):
            chunk_doc = await summarize_code_in_chunk(chunk_input)
            if not doc.language:
                doc.language = chunk_doc.language
            doc.overview += chunk_doc.overview + "\n"
            doc.symbols.extend(chunk_doc.symbols)
        
        return doc
    
    return await summarize_code_in_chunk(input)

