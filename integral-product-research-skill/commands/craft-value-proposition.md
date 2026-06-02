# Command: craft-value-proposition

## Goal

Generate value hypotheses linked to selected segments and jobs, decompose the value, identify barriers and drivers, apply RAT, design validation experiments, and produce value proposition messaging.

## Input

```yaml
selected_segments: []
selected_jobs: []
market_research_summary: ""
current_solution_idea: ""
business_model: ""
constraints: {}
desired_output_depth: "brief | standard | deep | exhaustive"
language: "ru"
```

If market research is missing, create a draft and mark all conclusions as hypotheses. Do not imply that value or willingness-to-pay is proven without evidence.

## Required evidence behavior

- Every value hypothesis must include confidence and validation need.
- Distinguish validated facts from model-generated assumptions.
- Do not create “universal” value propositions detached from jobs.
- Treat willingness-to-pay as unproven unless supported by payment behavior, pre-orders, pricing tests, sales conversations, or comparable evidence.

## Process

### Step 1. Select target jobs

For each selected segment, identify:

- main job;
- most painful moment;
- desired outcome;
- current alternative;
- why the current alternative is unsatisfactory;
- context and trigger;
- success criteria from the user’s perspective.

Output table:

| Segment | Job | Painful Moment | Desired Outcome | Current Alternative | Why Unsatisfactory | Confidence |
|---|---|---|---|---|---|---|

### Step 2. Formulate value hypotheses

Create **5–10 value hypotheses per segment**.

Format:

```text
Для [сегмент], который хочет [job], наш продукт помогает [desired outcome] за счет [механика ценности], в отличие от [альтернатива], потому что [ключевое отличие].
```

Each hypothesis must contain:

- segment;
- job;
- pain;
- desired outcome;
- value mechanism;
- proof point;
- differentiation;
- expected behavior change;
- monetization assumption;
- confidence level;
- evidence status.

Good value mechanisms include:

- reducing time to complete job;
- reducing cost;
- reducing risk;
- increasing accuracy;
- making decisions clearer;
- reducing cognitive load;
- enabling collaboration;
- automating repetitive sub-jobs;
- making compliance easier;
- changing a high-friction workflow into a guided flow.

### Step 3. Decompose value

For each hypothesis, decompose:

- functional value;
- emotional value;
- social value;
- economic value;
- time-saving value;
- risk-reduction value;
- cognitive-load-reduction value.

Make clear which value dimensions are primary and which are secondary.

### Step 4. Identify barriers and drivers

For each hypothesis, state:

- what pushes the user to try the product;
- what stops the user;
- what makes the user switch from current alternatives;
- what makes the user reject the product;
- what increases trust;
- what lowers perceived risk;
- what must be true for adoption.

### Step 5. Apply RAT

For every value hypothesis, identify assumptions by type:

- problem assumption;
- segment assumption;
- value assumption;
- channel assumption;
- payment assumption;
- usage assumption;
- retention assumption;
- technical assumption;
- operational assumption;
- legal/compliance assumption if relevant.

Then select the **3–7 most dangerous assumptions** using:

```text
RAT Priority = Kill Potential * 0.45 + Uncertainty * 0.30 + Test Urgency * 0.15 + Low Test Cost Advantage * 0.10
```

Where each factor is 0–100.

### Step 6. Design validation plan

For each risky assumption, propose:

- experiment type;
- minimal test;
- target audience;
- sample size or exposure;
- scenario;
- success metric;
- failure criterion;
- duration;
- cost;
- tools;
- data to collect;
- expected decision after result: continue, change, defer, kill.

Possible experiments:

- problem interview;
- solution interview;
- landing page smoke test;
- fake door test;
- concierge MVP;
- Wizard of Oz MVP;
- prototype test;
- paid ads test;
- pricing test;
- pre-order test;
- manual service test;
- cold outreach test;
- retention cohort test.

### Step 7. Produce value proposition and messaging

Output:

- short UVP;
- long UVP;
- positioning statement;
- elevator pitch;
- landing page hero;
- offer;
- headline;
- subheadline;
- CTA;
- reasons to believe;
- objection handling;
- messaging variants by segment if needed.

## Output format

Use `templates/value-proposition-plan.md`.

Required sections:

```markdown
# Value Proposition & Hypothesis Validation Plan

## 1. Selected Segment & Job
## 2. Value Hypotheses
## 3. Value Decomposition
## 4. Barriers & Drivers
## 5. Riskiest Assumptions
## 6. RAT Experiment Plan
## 7. Recommended Value Proposition
## 8. Messaging
## 9. Next Experiments
## 10. Decision Rules
```
