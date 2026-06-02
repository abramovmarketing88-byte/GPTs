# Integral Methodology: AJTBD + ABCDX + RAT + Product Requirements

## Purpose

This methodology connects discovery, value design, risk testing, and implementation requirements into one workflow. The goal is not to produce persuasive text; the goal is to reduce product uncertainty and preserve the chain of reasoning from market insight to buildable requirements.

## Core principle

A product requirement is only meaningful if it can be traced back to:

```text
Segment → Context → Job → Pain → Desired Outcome → Value Hypothesis → Risk → Experiment → Requirement → Metric
```

If this trace is missing, the requirement may be a feature idea rather than a product requirement.

## AJTBD / Advanced Jobs To Be Done

AJTBD treats the unit of analysis as the work a person or organization tries to get done in a specific situation.

Analyze:

- Main job: the central progress the user seeks.
- Related jobs: connected tasks that influence success.
- Functional jobs: practical tasks and operations.
- Emotional jobs: how the user wants to feel or avoid feeling.
- Social jobs: how the user wants to be perceived by others.
- Context: where, when, and under what constraints the job appears.
- Trigger: event or pressure that starts the job.
- Current alternatives: what the user hires today.
- Barriers: what blocks switching or adoption.
- Drivers: what pushes toward action.
- Desired outcomes: measurable improvements users want.
- Hiring criteria: why the user chooses a solution.
- Firing criteria: why the user abandons an alternative.

Job statement:

```text
Когда [ситуация], я хочу [выполнить работу], чтобы [получить прогресс / outcome].
```

## Job graph

A job graph shows how the job unfolds over time:

```text
Trigger → Pre-job → Main job → Sub-jobs → Decision point → Outcome → Follow-up job
```

For each node, identify:

- pain;
- uncertainty;
- current workaround;
- decision criteria;
- product insertion point;
- success metric.

## ABCDX segmentation

ABCDX is used to classify and prioritize segments.

- A: high potential, high pain, high willingness-to-pay, strong product fit.
- B: good potential but with meaningful constraint in channel, budget, maturity, frequency, or implementation.
- C: moderate value; can be served in standardized ways but should not be strategic focus.
- D: low priority because of weak pain, weak budget, weak fit, or high acquisition/servicing cost.
- X: unknown, unvalidated, or contradictory evidence; requires research before confident classification.

A segment should be defined by a meaningful cluster of context, job, pain, buying dynamics, and access path. Demographic labels are insufficient.

## RAT / Riskiest Assumption Test

RAT identifies assumptions that can kill the product if false. It should happen before expensive building.

Risk categories:

- problem risk;
- segment risk;
- value risk;
- willingness-to-pay risk;
- channel risk;
- solution risk;
- usability risk;
- operational risk;
- legal/compliance risk;
- technical risk.

A good RAT experiment is:

- minimal;
- fast;
- decision-oriented;
- measurable;
- connected to a specific assumption;
- designed to produce a continue/change/defer/kill decision.

## Product requirements

Requirements must translate validated or priority hypotheses into buildable details:

- user scenarios;
- user stories;
- functional requirements;
- non-functional requirements;
- UX requirements;
- data requirements;
- API/integration requirements;
- acceptance criteria;
- edge cases;
- analytics;
- release plan.

MVP scope should include only what is necessary to validate the main job and highest-risk value hypothesis.

## Evidence discipline

The agent must not treat model output as proof. A market, segment, pain, WTP, or market-size claim is a hypothesis until validated by:

- credible external source;
- primary interviews;
- behavioral analytics;
- paid or unpaid experiments;
- observed customer behavior;
- signed LOI, pre-order, payment, or usage.
