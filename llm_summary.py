from ollama import AsyncClient

MODEL = "deepseek-r1:1.5b"

BASE_PROMPT = """
In the given markdown replace all code blocks with an summary of them.
Summary should include a high-level and low-level explaination.
Keep the style.
Keep the rest as it is.
Dont write stuff like "here is..."
Dont use markdown blocks, like ```markdown ```
"""


ollama = AsyncClient()


async def summarize_code_in_markdown(markdown: str) -> str:
    prompt = BASE_PROMPT + "\n\n" + markdown
    resp = await ollama.generate(MODEL, prompt)
    response = resp.response

    return response
