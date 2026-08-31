---
{
  "id": "P005",
  "type": "principle",
  "title": "Measure learning after assistance is removed",
  "statement": "Claims that an AI intervention improves learning should include independent outcomes after support is removed, with delay and transfer matched to the capability claim.",
  "status": "active",
  "confidence": "high",
  "topics": ["learning-vs-performance", "assessment-validity", "product-measurement"],
  "based_on": ["C001", "C004", "C005", "B001"],
  "applies_to": ["product evaluation", "experiments", "learner modelling", "assessment"],
  "exceptions": ["A product explicitly and only claims immediate performance support", "Safety or ethics prohibit withdrawing necessary support"],
  "falsifiers": ["Assisted measures are shown to predict the declared delayed independent capability with adequate calibration in the target context."],
  "last_reviewed": "2026-08-31"
}
---

# P005 — Measure learning after assistance is removed

## Principle

Every learning claim should define support state, delay, and transfer distance. Evaluate independently after enough time to distinguish durable learning from temporary fluency.

## Rationale

Assisted success can coexist with impaired unaided performance [C001]. Retrieval and spacing effects demonstrate why immediate experience and later availability can point in different directions [C004, C005].

## Product patterns

- telemetry schemas that record assistance conditions;
- immediate, delayed, and transfer checkpoints;
- predeclared primary learning outcomes;
- dashboards that display performance and learning separately;
- no silent mastery credit for generated work.

## Falsifiers and measures

Validate whether cheaper assisted proxies predict the delayed independent outcome. Where they do, use them within their calibrated boundary rather than universalizing the result.
