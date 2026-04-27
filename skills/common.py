from pathlib import Path

from config import PROMPTS_DIR


def load_prompt(prompt_filename: str) -> str:
    prompt_path = Path(PROMPTS_DIR) / prompt_filename
    if not prompt_path.exists():
        raise FileNotFoundError(f"Prompt file not found: {prompt_path}")
    return prompt_path.read_text(encoding="utf-8")
