from utils.llm import call_llm
from skills.common import load_prompt


def review_copy(input_data: str) -> str:
    prompt = load_prompt("review_qa.txt")
    return call_llm(prompt=prompt, input_data=input_data)
