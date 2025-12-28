from ollama import Client


ollama = Client()

MODEL = "deepseek-r1:1.5b"

BASE_PROMPT = """
You are a documentation engine.
Given the structured symbol information below, generate a Markdown section that:
1. Explains what the symbol does at a high level
2. For each symbol, explains its purpose and behavior in plain language
3. Highlights any important details, like side effects or constants
4. Uses a clean, human-readable style"""

def generate_llm_summary(code: str) -> str:

    prompt = BASE_PROMPT + "\n\n" + code
    
    resp = ollama.generate(MODEL, prompt)
    return resp["response"]