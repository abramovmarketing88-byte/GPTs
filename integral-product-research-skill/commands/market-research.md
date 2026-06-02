# Command: market-research

## Goal

Conduct market research for a product idea. Discover potential segments, formulate jobs-to-be-done, map alternatives and competition, estimate market size, prioritize segments with ABCDX and scoring, and recommend focus.

## Input

```yaml
product_idea: ""
industry: ""
geography: ""
audience_hypothesis: ""
problem_hypothesis: ""
solution_hypothesis: ""
business_model: ""
known_competitors: []
available_sources: []
desired_output_depth: "brief | standard | deep | exhaustive"
language: "ru"
```

If inputs are incomplete, continue with explicit assumptions. Ask clarifying questions only if product idea or target context is impossible to infer.

## Required evidence behavior

- Separate `Fact`, `Hypothesis`, `Assumption`, `Unknown`, and `Needs validation`.
- Do not invent market data, interview results, competitor revenue, or statistics.
- If no external sources are provided or browsed, label all market-size, segment-pain, WTP, and competition conclusions as hypotheses.
- Provide confidence level for each segment and major claim.

## Process

### Step 1. Understand the initial product idea

Output:

- short product description;
- presumed problem;
- presumed users / buyers / beneficiaries;
- context of use;
- business model assumptions;
- key uncertainties;
- evidence table.

Questions to answer:

- What progress is the user trying to make?
- What situation triggers the need?
- Is this a user problem, buyer problem, operational problem, or strategic problem?
- What would happen if the product did not exist?

### Step 2. Build a market map

Output:

- market categories;
- adjacent markets;
- direct alternatives;
- indirect alternatives;
- non-consumption patterns;
- major players;
- solution types;
- buying channels;
- adoption constraints;
- regulatory or compliance context if relevant.

Classify alternatives:

| Type | Description | Examples / Hypotheses | Why Users Hire It | Why Users Fire It |
|---|---|---|---|---|
| Direct product | Same job, similar solution |  |  |  |
| Indirect product | Same job, different solution |  |  |  |
| Service / agency | Human-delivered alternative |  |  |  |
| Internal workaround | Spreadsheet, manual process, staff |  |  |  |
| Non-consumption | User avoids or postpones job |  |  |  |

### Step 3. Discover segments

Find **5–12 potential segments**. Do not define segments only by demographics. Prefer job-context-access segment definitions, e.g. `small B2B SaaS founders who need to understand churn drivers before fundraising`.

For each segment, provide:

- segment name;
- description;
- problem context;
- main jobs;
- current alternatives;
- pain intensity;
- pain frequency;
- urgency;
- budget;
- willingness-to-pay;
- accessibility through channels;
- barriers;
- drivers;
- expected ABCDX class;
- confidence level;
- data needed.

### Step 4. Formulate jobs

For every segment, include:

- main job;
- related jobs;
- functional jobs;
- emotional jobs;
- social jobs;
- desired outcomes;
- struggling moments;
- hiring criteria;
- firing criteria for current alternatives.

Job format:

```text
Когда [ситуация], я хочу [выполнить работу], чтобы [получить прогресс / outcome].
```

Quality checks:

- The job must describe progress, not a feature.
- The job must include a situation and an outcome.
- The job must be plausible for the segment and context.

### Step 5. Build a job graph for priority segments

For the top 2–4 candidate segments, map:

- preceding jobs;
- main job;
- sub-jobs;
- dependent jobs;
- recurring jobs;
- post-completion jobs;
- pain points;
- decision points;
- product insertion points;
- metrics that indicate job success.

Represent as text graph or table:

```text
Trigger → Pre-job → Main job → Sub-jobs → Decision point → Outcome → Follow-up job
              pain          pain        insertion point        metric
```

### Step 6. Estimate market and segment size

Provide TAM / SAM / SOM:

- TAM — total market that could theoretically need the job;
- SAM — reachable market within geography, business model, platform, constraints;
- SOM — realistic initial capture based on channels, competition, adoption, and team capacity.

If exact data is unavailable:

- give a range only if the assumptions are explicit;
- label it as `Hypothesis` or `Assumption`;
- state confidence;
- list required sources: public reports, industry databases, census/statistical data, competitor pricing, interviews, funnel tests, customer analytics.

### Step 7. Prioritize segments

Use this formula:

```text
Segment Score =
Pain Intensity * 0.20 +
Frequency * 0.15 +
Willingness To Pay * 0.15 +
Accessibility * 0.15 +
Market Size * 0.10 +
Product Fit * 0.15 +
Low Competition Advantage * 0.05 +
Strategic Value * 0.05
```

For each factor use 0–100. Explain scoring rationale. If evidence is weak, mark score as assumption and reduce confidence.

Output for each segment:

- final score 0–100;
- ABCDX class;
- rationale;
- main risks;
- needed research.

### Step 8. Recommend focus

Recommend:

- 1–3 focus segments;
- jobs to prioritize;
- why these segments now;
- segments not to pursue now;
- first hypotheses to validate;
- data to collect;
- research plan with sequence, sample, methods, and decision rules.

## Output format

Use `templates/market-research-report.md`.

Required sections:

```markdown
# Market Research Report

## 1. Executive Summary
## 2. Product Idea Interpretation
## 3. Market Map
## 4. Segment Discovery
## 5. Jobs Map
## 6. Alternatives & Competition
## 7. TAM / SAM / SOM
## 8. Segment Prioritization
## 9. Recommended Focus
## 10. Key Risks
## 11. Research Plan
## 12. Open Questions
```
