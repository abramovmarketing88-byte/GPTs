from utils.llm import call_llm
from skills.common import load_prompt


def synthesize_insights(input_data: str) -> str:
    prompt = load_prompt("insights_synthesis.txt")
    return call_llm(prompt=prompt, input_data=input_data)
