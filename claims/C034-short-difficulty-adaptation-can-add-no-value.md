---
{
  "id": "C034",
  "type": "claim",
  "title": "Short-horizon difficulty adaptation can add no learning value",
  "statement": "In one matched classroom experiment, 30 minutes of default-parameter learner-model difficulty adaptation produced no learning advantage over a transparent fixed sequence with the same content, feedback and hints.",
  "status": "provisional",
  "confidence": "moderate",
  "topics": ["learner-modelling", "knowledge-tracing", "scaffolding", "product-measurement"],
  "supporting_sources": ["S053"],
  "contradicting_sources": ["S051", "S052"],
  "boundary_conditions": ["One 132-learner early-primary mathematics experiment.", "The intervention lasted 30 minutes and measured only an immediate parallel posttest.", "BKT parameters were defaults rather than locally calibrated.", "The adaptive mastery gate may have reduced curriculum progression."],
  "product_relevance": "Do not infer value from the presence of a learner model. Predefine a warm-up horizon, calibrate its decision thresholds, monitor content coverage, and retain the fixed policy when adaptation does not clear a meaningful-effect threshold.",
  "last_reviewed": "2026-10-11"
}
---

# C034 — Short-horizon difficulty adaptation can add no value

## Claim

Adaptivity is a policy to test, not a property that makes instruction better by definition. A learner model may lack enough evidence to improve a decision, and mastery gating can change coverage in harmful ways.

## Evidence and reasoning

[S053] randomized second-grade learners between two otherwise identical tutors. Adaptive task selection had a primary posttest effect of partial eta squared .00, while fixed-sequence learners progressed further by the platform's own mastery measure. The study therefore passes the strong-comparator test but fails to show incremental learning value.

## Boundary conditions

The result does not show that adaptation never works. [S051] and [S052] report positive independent or delayed outcomes after months of learner evidence. The direct conclusion is narrower: short, uncalibrated difficulty adaptation cannot be presumed to outperform a transparent sequence.

## Counterevidence and uncertainty

The experiment had no delayed outcome and may have been too brief for BKT to converge. Its null could reflect implementation choices rather than an inherent limit of learner modelling. That possibility strengthens the need for calibration and ablation rather than rescuing the policy by assumption.

## Product relevance

Use a transparent policy until the learner model has enough validated evidence to change a consequential decision. Compare fixed, learner-model adaptive and learner-controlled policies with predefined equivalence bounds and coverage checks.
