# Scoring Reference

## Segment Score

Use 0–100 for each factor:

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

## Factor definitions

### Pain Intensity

How severe the problem is when it appears.

- 0–20: mild annoyance.
- 21–40: inconvenient but tolerable.
- 41–60: meaningful inefficiency or frustration.
- 61–80: costly, stressful, or operationally important.
- 81–100: urgent, expensive, compliance-critical, revenue-critical, or mission-critical.

### Frequency

How often the problem occurs.

- 0–20: rare.
- 21–40: occasional.
- 41–60: monthly / periodic.
- 61–80: weekly.
- 81–100: daily or embedded in core workflow.

### Willingness To Pay

Evidence or likelihood that the segment pays for solving the job.

- 0–20: no budget or no paid alternatives.
- 21–40: weak budget, mostly free alternatives.
- 41–60: some budget, unclear buyer.
- 61–80: existing paid alternatives and clear buyer.
- 81–100: urgent budget, high switching motivation, paid behavior already visible.

### Accessibility

How reachable the segment is through realistic channels.

- 0–20: fragmented, no clear channels.
- 21–40: reachable only through expensive channels.
- 41–60: some communities or channels exist.
- 61–80: clear channels and repeatable outreach.
- 81–100: highly concentrated channels, partnerships, or owned access.

### Market Size

Potential number of buyers/users and revenue pool.

Score high only when the market is large enough for the intended ambition and evidence is credible.

### Product Fit

How well the product idea can solve the job with available capabilities, constraints, and differentiation.

### Low Competition Advantage

High score means the product has a plausible wedge despite competition. Low score means crowded market, strong incumbents, or weak differentiation.

### Strategic Value

Strategic relevance for learning, brand, partnerships, expansion, data advantage, or long-term platform potential.

## ABCDX mapping

- A: score 75–100, strong evidence, few critical blockers.
- B: score 60–74, or high score with channel/budget/maturity constraint.
- C: score 45–59, moderate value, standardizable but not focus.
- D: score below 45, weak economics or fit.
- X: insufficient evidence or unresolved contradiction.

Confidence can override class. A high-scoring but unvalidated segment should be `X` or `B/X`, not `A`.

## RAT Priority

Use 0–100:

```text
RAT Priority = Kill Potential * 0.45 + Uncertainty * 0.30 + Test Urgency * 0.15 + Low Test Cost Advantage * 0.10
```

Prioritize the highest RAT scores first, especially if a cheap test can invalidate a major assumption before build.
