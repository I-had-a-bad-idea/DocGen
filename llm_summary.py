from ollama import AsyncClient

MODEL = "deepseek-coder:6.7b"

BASE_PROMPT = """
You are a documentation engine.
Given the markdown below, replace the code with a summary that:
1. Explains what the code does at a high level
2. Explains its purpose and behavior in plain language
3. Highlights any important details, like side effects or constants
4. Uses a clean, human-readable style
5. Dont use markdonw blocks (```markdown  ```)!!"""

ollama = AsyncClient()


async def summarize_code_in_markdown(markdown: str) -> str:
    prompt = BASE_PROMPT + "\n\n" + markdown
    print("Generating LLLM summaries")
    resp = await ollama.generate(MODEL, prompt)
    return resp.response
