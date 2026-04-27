from __future__ import annotations

import argparse
import sys

from orchestrator.pipeline import run_pipeline
from skills.registry import analyze_prompt_roles


def configure_utf8_stdio() -> None:
    """Force UTF-8 stdout/stderr in Windows terminals when possible."""
    for stream_name in ("stdout", "stderr"):
        stream = getattr(sys, stream_name, None)
        if stream is None:
            continue
        reconfigure = getattr(stream, "reconfigure", None)
        if callable(reconfigure):
            reconfigure(encoding="utf-8")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Run modular AI marketing pipeline for landing page generation."
    )
    parser.add_argument("product_description", nargs="?", type=str, help="Product or service description")
    parser.add_argument(
        "--show-steps",
        action="store_true",
        help="Print intermediate outputs for every pipeline step",
    )
    parser.add_argument(
        "--list-prompts",
        action="store_true",
        help="Print prompt files and assigned roles",
    )
    return parser


def main() -> None:
    configure_utf8_stdio()
    parser = build_parser()
    args = parser.parse_args()

    if args.list_prompts:
        print("\n=== PROMPT ROLE MAP ===")
        for item in analyze_prompt_roles():
            print(f"- {item['step']}: {item['prompt']} ({item['role']}) [{item['status']}]")
        if not args.product_description:
            return

    if not args.product_description:
        parser.error("product_description is required unless --list-prompts is used")

    result = run_pipeline(args.product_description)

    if args.show_steps:
        print("\n=== PIPELINE STEPS ===")
        for step_name, step_output in result.steps.items():
            print(f"\n--- {step_name.upper()} ---")
            print(step_output)

    print("\n=== FINAL RESULT ===")
    print(result.final_output)


if __name__ == "__main__":
    main()
