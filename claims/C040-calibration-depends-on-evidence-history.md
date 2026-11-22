---
{
  "id": "C040",
  "type": "claim",
  "title": "Aggregate learner-model calibration can conceal subgroup decision errors",
  "statement": "In one large knowledge-tracing comparison, strong aggregate probability calibration concealed systematic overprediction for lower-performing learners, stage-specific calibration errors, and higher simulated false-mastery rates, so model-level calibration metrics alone were insufficient for the threshold decision being made.",
  "status": "seed",
  "confidence": "low",
  "topics": ["learner-modelling", "assessment-validity", "product-measurement"],
  "supporting_sources": ["S066"],
  "contradicting_sources": [],
  "boundary_conditions": ["One conference paper using one Korean TOEIC dataset and performance-defined, not demographic, subgroups.", "Promotion decisions were simulated per interaction and reported false-mastery rates are upper bounds, not observed platform harms.", "Next-response calibration is not construct validity, learning, fairness, or decision utility."],
  "product_relevance": "Attach calibration to a versioned inference and decision threshold; report performance across relevant evidence stages and learner groups, then test false-decision rates against a transparent baseline before use.",
  "last_reviewed": "2026-11-22"
}
---

# C040 — Aggregate learner-model calibration can conceal subgroup decision errors

## Evidence and reasoning

[S066] found aggregate ECE below .025 for all six knowledge-tracing models, while every model overpredicted the lower-performing group and underpredicted the higher-performing group. Group-by-stage ECE reached .157 to .195 in the worst cells, and false-mastery rates differed by group, model, and threshold in the simulated decision layer.

## Boundary conditions

This is a useful falsifier of a single aggregate calibration flag, not proof of demographic unfairness or a production effect. The groups were defined from observed performance, the decision layer was simulated, and the work did not test whether subgroup recalibration improves learning or fairness.

## Product relevance

An inference record needs the evidence stage, calibration population, model and calibrator versions, metrics, decision threshold, and false-decision audit. Raw observation events should not carry model confidence, and aggregate ECE should not authorize a learner-level action.

