from ollama import AsyncClient
from tqdm.asyncio import tqdm_asyncio

MODEL = "deepseek-r1:1.5b"

BASE_PROMPT = """
You are a documentation engine.
Given the structured symbol information below, generate a section that:
1. Explains what the symbol does at a high level
2. For each symbol, explains its purpose and behavior in plain language
3. Highlights any important details, like side effects or constants
4. Uses a clean, human-readable style
5. Can be used as a section in a markdown file"""

ollama = AsyncClient()

OPTIONS = {
    "num_ctx": 1000,  # Max Number of tokens in context
    "num_predict": 512 # Max number of tokens in answer
}

async def async_generate_llm_summary(code: str) -> str:
    prompt = BASE_PROMPT + "\n\n" + code
    resp = await ollama.generate(MODEL, prompt,options=OPTIONS)
    return resp["response"]

async def async_generate_llm_summaries(codes: list[str]) -> list[str]:
    results = []
    for coro in tqdm_asyncio.as_completed([async_generate_llm_summary(code) for code in codes], total=len(codes), unit="symbol"):
        result = await coro
        results.append(result.replace("```markdown", "").replace("```", ""))
    return results