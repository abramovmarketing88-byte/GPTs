from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Dict

from config import PROMPTS_DIR


def load_prompt(prompt_filename: str) -> str:
    prompt_path = Path(PROMPTS_DIR) / prompt_filename
    if not prompt_path.exists():
        raise FileNotFoundError(f"Prompt file not found: {prompt_path}")
    return prompt_path.read_text(encoding="utf-8")


def to_json(data: Dict[str, Any]) -> str:
    return json.dumps(data, ensure_ascii=False, indent=2)
