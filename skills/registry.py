from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Dict, List

from config import PROMPTS_DIR


@dataclass(frozen=True)
class PromptSpec:
    step_name: str
    prompt_file: str
    role: str


PIPELINE_SPECS: List[PromptSpec] = [
    PromptSpec("audience", "audience_analysis.txt", "Audience analysis"),
    PromptSpec("segmentation", "segmentation.txt", "Audience segmentation"),
    PromptSpec("pains", "pain_points.txt", "Pain-point and barrier analysis"),
    PromptSpec("insights", "insights_synthesis.txt", "Strategic insights synthesis"),
    PromptSpec("structure", "landing_structure.txt", "Landing-page structure design"),
    PromptSpec("copy", "copywriting.txt", "Conversion copywriting"),
    PromptSpec("review", "review_qa.txt", "QA and polishing"),
]


def analyze_prompt_roles() -> List[Dict[str, str]]:
    """Return prompt-role mapping for all prompt files used by the pipeline."""
    prompt_files = {path.name for path in Path(PROMPTS_DIR).glob("*.txt")}
    analyzed: List[Dict[str, str]] = []

    for spec in PIPELINE_SPECS:
        analyzed.append(
            {
                "step": spec.step_name,
                "prompt": spec.prompt_file,
                "role": spec.role,
                "status": "found" if spec.prompt_file in prompt_files else "missing",
            }
        )

    return analyzed
