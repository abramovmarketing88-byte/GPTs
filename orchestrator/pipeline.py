from __future__ import annotations

import json
from dataclasses import dataclass
from typing import Dict

from skills.audience import analyze_audience
from skills.segmentation import segment_audience
from skills.pains import analyze_pain_points
from skills.insights import synthesize_insights
from skills.structure import build_landing_structure
from skills.copywriting import write_landing_copy
from skills.review import review_copy


@dataclass
class PipelineResult:
    input_data: str
    steps: Dict[str, str]
    final_output: str


def run_pipeline(input_data: str) -> PipelineResult:
    audience_output = analyze_audience(input_data)

    segmentation_input = json.dumps(
        {"product_input": input_data, "audience": audience_output},
        ensure_ascii=False,
        indent=2,
    )
    segmentation_output = segment_audience(segmentation_input)

    pains_input = json.dumps(
        {
            "product_input": input_data,
            "audience": audience_output,
            "segments": segmentation_output,
        },
        ensure_ascii=False,
        indent=2,
    )
    pains_output = analyze_pain_points(pains_input)

    insights_input = json.dumps(
        {
            "audience": audience_output,
            "segments": segmentation_output,
            "pain_points": pains_output,
        },
        ensure_ascii=False,
        indent=2,
    )
    insights_output = synthesize_insights(insights_input)

    structure_input = json.dumps(
        {
            "product_input": input_data,
            "insights": insights_output,
        },
        ensure_ascii=False,
        indent=2,
    )
    structure_output = build_landing_structure(structure_input)

    copy_input = json.dumps(
        {
            "product_input": input_data,
            "insights": insights_output,
            "structure": structure_output,
        },
        ensure_ascii=False,
        indent=2,
    )
    copy_output = write_landing_copy(copy_input)

    review_input = json.dumps(
        {
            "copy_draft": copy_output,
            "strategy_inputs": {
                "audience": audience_output,
                "segments": segmentation_output,
                "pain_points": pains_output,
                "insights": insights_output,
            },
        },
        ensure_ascii=False,
        indent=2,
    )
    reviewed_output = review_copy(review_input)

    steps = {
        "audience": audience_output,
        "segmentation": segmentation_output,
        "pains": pains_output,
        "insights": insights_output,
        "structure": structure_output,
        "copy": copy_output,
        "review": reviewed_output,
    }

    return PipelineResult(
        input_data=input_data,
        steps=steps,
        final_output=reviewed_output,
    )
