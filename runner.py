import argparse

from orchestrator.pipeline import run_pipeline


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Run modular AI marketing pipeline for landing page generation."
    )
    parser.add_argument("product_description", type=str, help="Product or service description")
    parser.add_argument(
        "--show-steps",
        action="store_true",
        help="Print intermediate outputs for every pipeline step",
    )
    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()

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
