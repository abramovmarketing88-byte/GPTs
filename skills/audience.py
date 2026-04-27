from utils.llm import call_llm
from skills.common import load_prompt


def analyze_audience(input_data: str) -> str:
    prompt = load_prompt("audience_analysis.txt")
    return call_llm(prompt=prompt, input_data=input_data)
