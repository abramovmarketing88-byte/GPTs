from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
PROMPTS_DIR = BASE_DIR / "prompts"

# Keep abstract; replace with real provider integration when needed.
LLM_PROVIDER = "mock"
MODEL_NAME = "local-placeholder-model"
