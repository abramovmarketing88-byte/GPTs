from __future__ import annotations

import json
from typing import Any, Dict

from config import LLM_PROVIDER, MODEL_NAME


def call_llm(prompt: str, input_data: str) -> str:
    """Abstract LLM call wrapper.

    Replace this mock block with a real provider client (OpenAI, Anthropic, local model, etc.)
    while keeping the same signature.
    """
    if LLM_PROVIDER == "mock":
        payload: Dict[str, Any] = {
            "provider": LLM_PROVIDER,
            "model": MODEL_NAME,
            "prompt_preview": prompt.strip()[:220],
            "input": input_data,
        }
        return json.dumps(payload, ensure_ascii=False, indent=2)

    raise NotImplementedError(f"Unsupported LLM provider: {LLM_PROVIDER}")
