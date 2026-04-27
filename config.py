import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
PROMPTS_DIR = BASE_DIR / "prompts"

# Provider mode:
# - "mock": offline placeholder output (fast)
# - "openai": real API call through OpenAI-compatible Chat Completions endpoint
LLM_PROVIDER = os.getenv("LLM_PROVIDER", "mock").strip().lower()
MODEL_NAME = os.getenv("MODEL_NAME", "gpt-4o-mini").strip()

# OpenAI-compatible settings (used only when LLM_PROVIDER=openai)
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "").strip()
OPENAI_BASE_URL = os.getenv("OPENAI_BASE_URL", "https://api.openai.com/v1").rstrip("/")
