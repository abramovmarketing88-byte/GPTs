# Product Requirements Document

## 0. Evidence Standard

> Requirements derived only from model-generated research are priority hypotheses, not validated facts. Mark validation status and risk for every core requirement.

| Requirement / Claim | Type | Evidence | Confidence | Validation Needed |
|---|---|---|---|---|
|  |  |  |  |  |

## 1. Product Brief

- Product:
- Platform:
- Target segment:
- Main job:
- Pain removed:
- Desired outcome:
- Value hypothesis:
- Why now:
- Business model:
- Constraints:
- MVP validation objective:

## 2. Target Segments

| Segment | Context | Main Job | Pains | Desired Outcomes | Current Alternatives | Triggers | Barriers | Success Criteria | Confidence |
|---|---|---|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |  |  |  |

## 3. Jobs To Be Done

| ID | Segment | Job Statement | Related Jobs | Functional Jobs | Emotional Jobs | Social Jobs | Desired Outcomes | Evidence Status |
|---|---|---|---|---|---|---|---|---|
| J-1 |  | Когда ..., я хочу ..., чтобы ... |  |  |  |  |  |  |

## 4. Value Hypotheses

| ID | Hypothesis | Segment | Job | Pain | Value Mechanism | Validation Status | Risk |
|---|---|---|---|---|---|---|---|
| VH-1 |  |  |  |  |  |  |  |

## 5. Scope

### In Scope

| Item | Why Included | Linked Job | Linked Hypothesis | MVP / v1 / v2 |
|---|---|---|---|---|
|  |  |  |  |  |

### Out of Scope

| Item | Reason | Revisit Trigger |
|---|---|---|
|  |  |  |

## 6. User Scenarios

| ID | Scenario | Actor | Trigger | Preconditions | User Goal | Happy Path | Alternative Paths | Edge Cases | Failure States | Recovery Behavior | Success Metrics |
|---|---|---|---|---|---|---|---|---|---|---|---|
| SC-1 |  |  |  |  |  |  |  |  |  |  |  |

## 7. User Stories

| ID | User Story | Priority | Job | Value Hypothesis | Acceptance Criteria | Analytics Events | Dependencies | Risks |
|---|---|---|---|---|---|---|---|---|
| US-1 | As a ..., I want to ..., so that ... | Must | J-1 | VH-1 |  |  |  |  |

## 8. Functional Requirements

For each requirement:

```yaml
id: FR-1
name: ""
purpose: ""
user_problem: ""
linked_job: "J-1"
linked_value_hypothesis: "VH-1"
behavior: ""
inputs: []
outputs: []
system_states: []
validation_rules: []
permissions: []
errors: []
empty_states: []
loading_states: []
edge_cases: []
admin_behavior: ""
logging: []
analytics: []
assumptions: []
```

## 9. Non-Functional Requirements

| Category | Requirement | Target / Standard | Rationale | Validation Method |
|---|---|---|---|---|
| Performance |  |  |  |  |
| Reliability |  |  |  |  |
| Security |  |  |  |  |
| Privacy |  |  |  |  |
| Accessibility |  |  |  |  |
| Localization |  |  |  |  |
| Scalability |  |  |  |  |
| Observability |  |  |  |  |
| Maintainability |  |  |  |  |
| Compliance |  |  |  |  |
| Data retention |  |  |  |  |
| Error handling |  |  |  |  |

## 10. UX Requirements

### Information Architecture

### Main Screens

| Screen | Purpose | Entry Point | Key Components | States | Empty State | Error State | CTA | Trust Elements |
|---|---|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |  |  |

### UX Principles

### Onboarding

### Microcopy

### Accessibility Requirements

## 11. Data Requirements

### Entities

| Entity | Purpose | Fields | Relationships | Lifecycle Statuses | Source | Quality Rules | Retention | Access Rights |
|---|---|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |  |  |

### Analytics Events

```yaml
event_name: ""
trigger: ""
properties: []
user_id_required: true
purpose: ""
linked_requirement: ""
```

## 12. API & Integration Requirements

| API / Integration | Purpose | Auth | Endpoints / Webhooks | Rate Limits | Retries | Fallbacks | Error Codes | Data Mapping | Risks |
|---|---|---|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |  |  |  |

## 13. Edge Cases

| Flow | Edge Case | Expected Behavior | Error / Recovery Message | Analytics Event | Requirement ID |
|---|---|---|---|---|---|
|  | User did not enter data |  |  |  |  |
|  | User entered invalid data |  |  |  |  |
|  | No internet |  |  |  |  |
|  | Server unavailable |  |  |  |  |
|  | API returned error |  |  |  |  |
|  | User interrupted scenario |  |  |  |  |
|  | User repeated action |  |  |  |  |
|  | User lacks permission |  |  |  |  |
|  | Data is stale |  |  |  |  |
|  | State conflict |  |  |  |  |
|  | Limits exceeded |  |  |  |  |
|  | Duplicate data |  |  |  |  |
|  | Partial operation completion |  |  |  |  |

## 14. Analytics Requirements

- North Star Metric:
- Activation metrics:
- Engagement metrics:
- Retention metrics:
- Conversion metrics:
- Monetization metrics:
- Quality metrics:
- Guardrail metrics:

### Event Taxonomy

| Event Name | Trigger | Properties | User ID Required | Purpose | Linked Requirement |
|---|---|---|---|---|---|
|  |  |  | true |  |  |

## 15. Release Plan

| Phase | Scope | Goal | Hypothesis Tested | Exit Criteria |
|---|---|---|---|---|
| MVP |  |  |  |  |
| v1 |  |  |  |  |
| v2 |  |  |  |  |
| Later |  |  |  |  |
| Out of scope |  |  |  |  |

## 16. Risks & Assumptions

| Risk / Assumption | Type | Linked Requirement | Severity | Confidence | Mitigation | Validation |
|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |

## 17. Open Questions

- 

## 18. Implementation Checklist

- [ ] Product brief reviewed.
- [ ] MVP scope tied to key job and value hypothesis.
- [ ] User stories have priorities and acceptance criteria.
- [ ] Functional requirements include states, validation, errors, permissions, and analytics.
- [ ] Non-functional requirements reviewed by engineering.
- [ ] UX requirements reviewed by design.
- [ ] Data model reviewed.
- [ ] API and integration risks reviewed.
- [ ] Edge cases covered.
- [ ] Analytics taxonomy implemented.
- [ ] Risks and assumptions have validation plan.
