# Example Product Requirements Document

## Scenario

MVP: retention brief generator for small online schools. Evidence status: priority hypothesis, not validated.

## 1. Product Brief

- Build: web app that ingests course engagement data and generates a weekly learner retention brief.
- Segment: small online schools with paid cohort or self-paced programs.
- Main job: understand why learners disengage and what action to take next.
- Pain: fragmented analytics and manual diagnosis.
- Desired outcome: prioritized interventions that improve completion.
- MVP objective: validate whether teams find an AI-generated retention brief actionable enough to request repeated use or pay for a pilot.

## 2. Target Segments

| Segment | Context | Main Job | Pains | Desired Outcomes | Confidence |
|---|---|---|---|---|---|
| Small online schools | Paid programs with completion pressure | Diagnose disengagement | Manual analytics, unclear root causes | Actionable weekly recommendations | Low |

## 3. Jobs To Be Done

| ID | Job Statement | Desired Outcomes |
|---|---|---|
| J-1 | Когда completion падает, я хочу понять причины disengagement, чтобы улучшить программу и сохранить выручку. | Faster diagnosis, clearer priorities, measurable intervention |

## 4. Value Hypotheses

| ID | Hypothesis | Validation Status | Risk |
|---|---|---|---|
| VH-1 | Weekly retention brief helps teams choose interventions faster than LMS dashboards. | Priority hypothesis | Value risk |

## 5. Scope

### In Scope

- Manual CSV upload.
- Basic course/cohort selection.
- Retention brief generation.
- Recommendation explanation.
- Feedback capture.

### Out of Scope

- Native LMS integrations.
- Automated interventions.
- Multi-role enterprise permissions.

## 6. User Scenarios

| ID | Scenario | Actor | Trigger | Happy Path | Failure States | Success Metrics |
|---|---|---|---|---|---|---|
| SC-1 | Generate weekly brief | Program manager | Weekly review | Upload CSV → review detected drop-offs → generate brief → mark recommendations useful/not useful | Invalid CSV, generation failure | Brief generated, usefulness rating |

## 7. User Stories

| ID | User Story | Priority | Job | Acceptance Criteria |
|---|---|---|---|---|
| US-1 | As a program manager, I want to upload learner engagement data so that I can diagnose disengagement. | Must | J-1 | Given a valid CSV, when I upload it, then the system validates and stores the dataset. |
| US-2 | As a program manager, I want to receive a retention brief so that I know which interventions to prioritize. | Must | J-1 | Given validated data, when I generate a brief, then I see top drop-off points, likely causes, and recommended actions. |

## 8. Functional Requirements

```yaml
id: FR-1
name: "CSV upload and validation"
purpose: "Accept learner engagement data for analysis"
linked_job: "J-1"
linked_value_hypothesis: "VH-1"
inputs: ["csv_file"]
outputs: ["validated_dataset", "validation_errors"]
validation_rules:
  - "Required columns must be present"
  - "Rows with missing learner_id are rejected"
errors:
  - "invalid_file_type"
  - "missing_required_columns"
analytics:
  - "csv_upload_started"
  - "csv_upload_validated"
```

```yaml
id: FR-2
name: "Retention brief generation"
purpose: "Generate actionable summary and recommendations"
linked_job: "J-1"
linked_value_hypothesis: "VH-1"
outputs: ["dropoff_summary", "likely_causes", "recommended_interventions"]
edge_cases:
  - "dataset too small"
  - "no obvious drop-off point"
  - "model output confidence low"
analytics:
  - "brief_generation_started"
  - "brief_generated"
  - "brief_recommendation_rated"
```

## 9. Non-Functional Requirements

| Category | Requirement |
|---|---|
| Performance | Generate brief within 60 seconds for MVP-size datasets. |
| Privacy | Do not require personally identifiable student data for MVP. |
| Reliability | Preserve uploaded dataset and brief status across refresh. |
| Accessibility | Core flows must be keyboard accessible. |
| Observability | Log upload validation and generation failures. |

## 10. UX Requirements

- Onboarding explains what CSV columns are needed.
- Empty state offers sample CSV.
- Brief page shows evidence behind each recommendation.
- CTA: `Generate retention brief`.
- Trust element: confidence label and “why this recommendation” explanation.

## 11. Data Requirements

| Entity | Fields | Lifecycle |
|---|---|---|
| Dataset | id, organization_id, filename, uploaded_at, validation_status | uploaded → validated → analyzed |
| Brief | id, dataset_id, status, summary, recommendations, confidence | generating → ready → rated |

## 12. API & Integration Requirements

- No external LMS integration in MVP.
- Internal endpoint: `POST /datasets`, `POST /briefs`, `GET /briefs/{id}`.

## 13. Edge Cases

| Flow | Edge Case | Expected Behavior |
|---|---|---|
| Upload | Invalid CSV | Show validation errors and sample format. |
| Generate | Server unavailable | Preserve dataset and allow retry. |
| Generate | Low confidence output | Show low confidence warning and request more data. |

## 14. Analytics Requirements

- North Star Metric: number of briefs rated useful per active organization.
- Activation: valid CSV uploaded.
- Engagement: brief generated and viewed.
- Conversion: pilot request after useful brief.

```yaml
event_name: "brief_recommendation_rated"
trigger: "user rates recommendation"
properties: ["brief_id", "recommendation_id", "rating", "segment"]
user_id_required: true
purpose: "Measure perceived usefulness"
linked_requirement: "FR-2"
```

## 15. Release Plan

| Phase | Scope | Goal |
|---|---|---|
| MVP | Upload + brief + feedback | Validate value hypothesis |
| v1 | Saved cohorts + trend comparison | Improve repeated use |
| v2 | LMS integrations | Reduce upload friction |
| Later | Automated interventions | Close loop |

## 16. Risks & Assumptions

| Risk | Type | Mitigation |
|---|---|---|
| Brief is too generic | Value risk | Concierge review and feedback loop |
| Data is insufficient | Technical risk | Data requirements and low-confidence state |
| Users will not pay | WTP risk | Pricing and pilot test |

## 17. Open Questions

- Which CSV schema is most common?
- What recommendation format is trusted?
- What price point fits small schools?

## 18. Implementation Checklist

- [ ] Upload flow built.
- [ ] Validation errors implemented.
- [ ] Brief generation state implemented.
- [ ] Feedback event tracked.
- [ ] Edge cases tested.
