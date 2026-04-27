from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Callable, Dict

from skills.audience import analyze_audience
from skills.copywriting import write_landing_copy
from skills.insights import synthesize_insights
from skills.pains import analyze_pain_points
from skills.review import review_copy
from skills.segmentation import segment_audience
from skills.structure import build_landing_structure
from skills.common import to_json


@dataclass
class PipelineResult:
    input_data: str
    steps: Dict[str, str]
    final_output: str


SKILL_HANDLERS: Dict[str, Callable[[str], str]] = {
    "audience": analyze_audience,
    "segmentation": segment_audience,
    "pains": analyze_pain_points,
    "insights": synthesize_insights,
    "structure": build_landing_structure,
    "copy": write_landing_copy,
    "review": review_copy,
}


def _build_step_input(step_name: str, pipeline_input: str, outputs: Dict[str, str]) -> str:
    context: Dict[str, Any] = {
        "pipeline_input": pipeline_input,
        "step": step_name,
        "previous_steps": outputs,
    }
    return to_json(context)


def run_pipeline(input_data: str) -> PipelineResult:
    outputs: Dict[str, str] = {}

    for step_name, handler in SKILL_HANDLERS.items():
        step_input = input_data if step_name == "audience" else _build_step_input(step_name, input_data, outputs)
        outputs[step_name] = handler(step_input)

    return PipelineResult(
        input_data=input_data,
        steps=outputs,
        final_output=outputs["review"],
    )
