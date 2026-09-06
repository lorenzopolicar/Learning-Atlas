---
{
  "id": "C013",
  "type": "claim",
  "title": "Elapsed time does not create a universal evidence-expiry rule",
  "statement": "Time-aware knowledge-tracing variants have produced dataset- and prediction-specific gains, nulls, and reversals, so an observation timestamp should inform a validated inference policy rather than trigger a universal capability-evidence expiry rule.",
  "status": "provisional",
  "confidence": "low",
  "topics": ["learner-modelling", "knowledge-tracing", "assessment-validity"],
  "supporting_sources": ["S027"],
  "contradicting_sources": [],
  "boundary_conditions": ["The inspected comparison covers two historical tutoring-system datasets and Bayesian knowledge-tracing variants.", "Elapsed time can still be predictive in a validated domain-specific model.", "Retention, inference review, and credential validity are separate policy questions."],
  "product_relevance": "Keep observation time immutable; recompute or mark a versioned learner-state inference stale according to an empirically validated model and decision use rather than deleting or expiring the event.",
  "last_reviewed": "2026-09-06"
}
---

# C013 — Elapsed time does not create a universal evidence-expiry rule

## Evidence and reasoning

Qiu et al. compared standard Bayesian Knowledge Tracing with time-aware forgetting and slip variants [S027]. Time-aware models helped some Cognitive Tutor predictions, did not improve new-day prediction, and underperformed standard BKT on ASSISTments. This mixed result contradicts a portable rule in which evidence loses validity monotonically after a fixed duration.

The warranted claim is narrow: record when an observation occurred, then let a separately versioned and validated inference policy decide whether and how recency changes its weight. Historical observations remain part of the audit trail even when an inference is superseded or no longer appropriate for a decision.

## Boundary conditions

The evidence does not show that time is irrelevant. It does not estimate decay for broad capabilities, credentials or modern AI-mediated work. Other models and domains may find elapsed time, opportunity order or intervention history predictive.

## Product relevance

Separate three clocks: `retentionUntil` for governance, `reviewAfter` or `doNotUseAfter` for an inference, and any learned decay function used by a particular model. Do not label the underlying observation as expired capability.
