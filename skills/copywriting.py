from utils.llm import call_llm
from skills.common import load_prompt


def write_landing_copy(input_data: str) -> str:
    prompt = load_prompt("copywriting.txt")
    return call_llm(prompt=prompt, input_data=input_data)
