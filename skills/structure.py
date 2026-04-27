from utils.llm import call_llm
from skills.common import load_prompt


def build_landing_structure(input_data: str) -> str:
    prompt = load_prompt("landing_structure.txt")
    return call_llm(prompt=prompt, input_data=input_data)
