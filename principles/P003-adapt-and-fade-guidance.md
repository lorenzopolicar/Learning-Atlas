---
{
  "id": "P003",
  "type": "principle",
  "title": "Adapt and fade guidance with evidence",
  "statement": "Vary examples, hints, explanations, and autonomy using domain-specific evidence of learner state, and fade scaffolds as independent capability becomes credible.",
  "status": "active",
  "confidence": "moderate",
  "topics": ["scaffolding", "learner-modelling", "ai-tutoring"],
  "based_on": ["C003", "C007", "B005"],
  "applies_to": ["worked examples", "hint policies", "adaptive pathways", "practice"],
  "exceptions": ["Stable accessibility support", "Safety procedures that require persistent checks", "Learner-requested reference material"],
  "falsifiers": ["Adaptive fading does not outperform a strong fixed scaffold on independent outcomes.", "Learner-state errors systematically withdraw support from those who need it."],
  "last_reviewed": "2026-08-31"
}
---

# P003 — Adapt and fade guidance with evidence

## Principle

Make scaffolding conditional on the target knowledge component, demonstrated performance, assistance history, confidence, and recentness. Fade one dimension at a time and verify independent success.

## Rationale

Guidance can reverse in value as expertise develops [C003], but the state used to adapt is uncertain [C007]. Personalization must therefore beat a transparent default rather than merely sound individualized [B005].

## Product patterns

- worked example → completion problem → independent problem;
- assistance budgets per capability;
- confidence-aware fallback when state evidence is weak;
- learner override and reason for adaptation;
- periodic unscaffolded probes.

## Falsifiers and measures

Evaluate independent learning, calibration, help misuse, frustration, fairness across groups, and the incremental effect over a well-designed fixed sequence.
