# Command: product-requirements

## Goal

Write detailed product requirements that AI agents, designers, developers, QA engineers, product managers, and founders can use to implement an MVP or product version without losing the underlying job, value hypothesis, and validation logic.

## Input

```yaml
validated_or_priority_value_hypotheses: []
selected_segments: []
selected_jobs: []
product_concept: ""
platform: ""
business_model: ""
constraints: {}
non_goals: []
desired_output_depth: "brief | standard | deep | exhaustive"
language: "ru"
```

If hypotheses are not validated, label them as priority hypotheses and include risk/validation notes in the PRD.

## Required evidence behavior

- Do not claim that requirements are validated if they come only from model-generated research.
- Link each core requirement to a job and value hypothesis.
- Include assumptions and risks for all important unvalidated requirements.
- Keep MVP scope focused on testing the key job and main value hypothesis.

## Process

### Step 1. Formulate product brief

Output:

- what is being built;
- for whom;
- which job it supports;
- which pain it reduces;
- which desired outcome it enables;
- why now;
- constraints;
- evidence status;
- MVP validation objective.

### Step 2. Describe users and segments

For each segment:

- description;
- context;
- main job;
- related jobs;
- pains;
- desired outcomes;
- current alternatives;
- triggers;
- barriers;
- success criteria;
- confidence and validation status.

### Step 3. Describe scenarios

For each key scenario:

- scenario name;
- actor;
- trigger;
- preconditions;
- user goal;
- happy path;
- alternative paths;
- edge cases;
- failure states;
- recovery behavior;
- success metrics.

### Step 4. Write user stories

Use format:

```text
As a [user/segment],
I want to [action/job],
so that [outcome].
```

For each story include:

- priority: Must / Should / Could / Won’t;
- linked job;
- linked value hypothesis;
- acceptance criteria;
- analytics events;
- dependencies;
- risks.

### Step 5. Write functional requirements

For each feature or flow, specify:

- requirement ID;
- purpose;
- user problem;
- linked job;
- linked value hypothesis;
- behavior;
- inputs;
- outputs;
- system states;
- validation rules;
- permissions;
- errors;
- empty states;
- loading states;
- edge cases;
- admin behavior;
- logging;
- analytics.

### Step 6. Write non-functional requirements

Always include:

- performance;
- reliability;
- security;
- privacy;
- accessibility;
- localization;
- scalability;
- observability;
- maintainability;
- compliance;
- data retention;
- error handling.

### Step 7. Write UX requirements

For designers, include:

- information architecture;
- main screens;
- screen states;
- UX principles;
- onboarding;
- empty states;
- error states;
- confirmation states;
- user feedback;
- accessibility requirements;
- microcopy;
- CTAs;
- trust elements.

### Step 8. Write data requirements

Specify:

- entities;
- fields;
- relationships;
- analytics events;
- lifecycle statuses;
- data sources;
- data quality requirements;
- retention rules;
- access rights.

### Step 9. Write API / integration requirements

If applicable, specify:

- external APIs;
- internal APIs;
- webhooks;
- authentication;
- rate limits;
- retries;
- fallbacks;
- error codes;
- data mapping.

### Step 10. Write acceptance criteria

Use Given / When / Then:

```gherkin
Given [precondition]
When [action]
Then [expected result]
```

Acceptance criteria must be testable and tied to a requirement ID.

### Step 11. Write edge cases

For every key flow, include at minimum:

- user did not provide required data;
- user provided invalid data;
- no internet;
- server unavailable;
- API returned error;
- user interrupted scenario;
- user repeated action;
- user lacks permissions;
- data is stale;
- state conflict;
- limits exceeded;
- duplicate data;
- partial operation completion.

### Step 12. Write analytics requirements

Include:

- North Star Metric;
- activation metrics;
- engagement metrics;
- retention metrics;
- conversion metrics;
- monetization metrics;
- quality metrics;
- guardrail metrics;
- event taxonomy.

Event format:

```yaml
event_name: ""
trigger: ""
properties: []
user_id_required: true
purpose: ""
linked_requirement: ""
```

### Step 13. Write release plan

Separate:

- MVP;
- v1;
- v2;
- later;
- out of scope.

For MVP, include only what validates the key job and main value hypothesis.

## Output format

Use `templates/product-requirements-document.md`.

Required sections:

```markdown
# Product Requirements Document

## 1. Product Brief
## 2. Target Segments
## 3. Jobs To Be Done
## 4. Value Hypotheses
## 5. Scope
## 6. User Scenarios
## 7. User Stories
## 8. Functional Requirements
## 9. Non-Functional Requirements
## 10. UX Requirements
## 11. Data Requirements
## 12. API & Integration Requirements
## 13. Edge Cases
## 14. Analytics Requirements
## 15. Release Plan
## 16. Risks & Assumptions
## 17. Open Questions
## 18. Implementation Checklist
```
