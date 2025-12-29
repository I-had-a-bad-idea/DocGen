from ollama import AsyncClient
from pydantic import BaseModel

MODEL = "deepseek-r1:1.5b"

BASE_PROMPT = """
In the given markdown REPLACE all code blocks with an SUMMARY of them.
The summary should include a DETAILED high-level and an even more DETAILED low-level explanation.
Explain everything in the code (variables, functions, etc.), but dont add hallucinate anything new.
Use Markdown to make it look good.
Keep the style.
Keep the rest as it is.
Make it detailed.
Dont use markdown blocks (```markdown ```)
Dont write stuff like "here is..."
"""

class Symbol:
    name: str
    type: str
    parent: str
    high_level_summary: str
    low_level_summary: str

class Documentation(BaseModel):
    symbols: list[Symbol]


ollama = AsyncClient()

OPTIONS = {
    "temperature": 0.25,
    "top_p": 0.5,
    "repeat_penalty": 1.5,
    "seed": 42,

}

async def summarize_code_in_markdown(markdown: str) -> Documentation:
    prompt = BASE_PROMPT + "\n\n" + markdown
    resp = await ollama.generate(MODEL,
                                 prompt,
                                 options=OPTIONS,
                                 format=Documentation.model_json_schema())
    
    response = Documentation.model_validate_json(resp.message.content) # type: ignore

    return response
