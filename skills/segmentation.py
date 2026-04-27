from utils.llm import call_llm
from skills.common import load_prompt


def segment_audience(input_data: str) -> str:
    prompt = load_prompt("segmentation.txt")
    return call_llm(prompt=prompt, input_data=input_data)
