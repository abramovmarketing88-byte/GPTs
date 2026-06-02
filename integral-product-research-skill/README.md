# integral-product-research-skill

Production-ready skill for AI agents and product teams that need to move from product idea to market research, value hypothesis validation, and implementation-ready product requirements.

## What this skill does

The skill combines:

- **AJTBD / Advanced Jobs To Be Done** — analyze progress, context, triggers, desired outcomes, alternatives, barriers, drivers, and job graphs.
- **ABCDX segmentation** — prioritize market segments by pain, frequency, WTP, accessibility, product fit, market size, competition, and strategic value.
- **RAT / Riskiest Assumption Test** — identify the assumptions most likely to kill the product and design minimal experiments.
- **Product Requirements methodology** — transform validated or priority hypotheses into PRDs suitable for UX/UI design, engineering, QA, analytics, and release planning.

## Package structure

```text
integral-product-research-skill/
  SKILL.md
  README.md
  commands/
    market-research.md
    craft-value-proposition.md
    product-requirements.md
  templates/
    market-research-report.md
    value-proposition-plan.md
    product-requirements-document.md
    segment-scorecard.md
    rat-experiment-card.md
    jtbd-job-map.md
  references/
    methodology.md
    scoring.md
    glossary.md
  examples/
    example-market-research.md
    example-value-proposition.md
    example-prd.md
```

## Commands

### 1. `market-research`

Use to produce a market research report with segment discovery, AJTBD maps, alternatives, TAM / SAM / SOM, ABCDX prioritization, recommended focus, key risks, and research plan.

### 2. `craft-value-proposition`

Use after selecting segments and jobs. Produces value hypotheses, value decomposition, barriers/drivers, riskiest assumptions, experiment plan, messaging, and decision rules.

### 3. `product-requirements`

Use after selecting priority or validated hypotheses. Produces a detailed PRD with product brief, segments, jobs, scenarios, user stories, functional and non-functional requirements, UX requirements, data requirements, integrations, edge cases, analytics, release plan, risks, and implementation checklist.

## Minimal input

```yaml
product_idea: ""
industry: ""
target_geography: ""
business_model: ""
current_stage: ""
known_audience: ""
known_problem: ""
known_solution: ""
competitors: []
available_data: []
constraints:
  budget: ""
  time: ""
  team: ""
  technology: ""
  legal: ""
desired_output_depth: "brief | standard | deep | exhaustive"
language: "ru"
```

## Core evidence rule

The agent must not treat model-generated research as proven. Any claim about the market, segment, pain, willingness-to-pay, or market size must remain a hypothesis until validated by external sources, interviews, analytics, or experiments.

## Recommended workflow

1. Run `market-research` to discover segments and prioritize focus.
2. Run `craft-value-proposition` for the top 1–3 segments and jobs.
3. Run validation experiments from the RAT plan.
4. Run `product-requirements` for the MVP, using either validated findings or explicitly marked priority hypotheses.
5. Continue iterating as new evidence arrives.

## Output depth

- `brief` — concise report with core tables and next steps.
- `standard` — complete but compact report suitable for team review.
- `deep` — detailed reasoning, tables, scoring rationale, experiment cards, and PRD sections.
- `exhaustive` — comprehensive artifact for high-stakes discovery and implementation planning.
