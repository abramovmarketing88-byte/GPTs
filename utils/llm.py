from __future__ import annotations

import json
import urllib.error
import urllib.request
from typing import Any, Dict

from config import LLM_PROVIDER, MODEL_NAME, OPENAI_API_KEY, OPENAI_BASE_URL


def call_llm(prompt: str, input_data: str) -> str:
    """Call LLM in mock mode or OpenAI-compatible mode."""
    if LLM_PROVIDER == "mock":
        payload: Dict[str, Any] = {
            "provider": LLM_PROVIDER,
            "model": MODEL_NAME,
            "prompt_preview": prompt.strip()[:220],
            "input_preview": input_data.strip()[:500],
        }
        return json.dumps(payload, ensure_ascii=False, indent=2)

    if LLM_PROVIDER == "openai":
        if not OPENAI_API_KEY:
            raise ValueError("OPENAI_API_KEY is required when LLM_PROVIDER=openai")

        body = {
            "model": MODEL_NAME,
            "messages": [
                {"role": "system", "content": prompt},
                {"role": "user", "content": input_data},
            ],
        }
        request = urllib.request.Request(
            url=f"{OPENAI_BASE_URL}/chat/completions",
            data=json.dumps(body).encode("utf-8"),
            headers={
                "Content-Type": "application/json",
                "Authorization": f"Bearer {OPENAI_API_KEY}",
            },
            method="POST",
        )
        try:
            with urllib.request.urlopen(request, timeout=90) as response:
                response_data = json.loads(response.read().decode("utf-8"))
            return response_data["choices"][0]["message"]["content"].strip()
        except urllib.error.HTTPError as exc:
            err_payload = exc.read().decode("utf-8", errors="replace")
            raise RuntimeError(f"OpenAI API HTTPError {exc.code}: {err_payload}") from exc
        except urllib.error.URLError as exc:
            raise RuntimeError(f"OpenAI API connection error: {exc}") from exc

    raise NotImplementedError(f"Unsupported LLM provider: {LLM_PROVIDER}")
