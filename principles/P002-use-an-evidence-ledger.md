---
{
  "id": "P002",
  "type": "principle",
  "title": "Use an evidence ledger for learner inferences",
  "statement": "Store learner observations separately from model inferences, with provenance, context, assistance state, time, uncertainty, and permitted use.",
  "status": "active",
  "confidence": "high",
  "topics": ["learner-modelling", "assessment-validity", "ethics-and-governance"],
  "based_on": ["C007", "C008", "B003", "B004"],
  "applies_to": ["learner profiles", "adaptive sequencing", "capability intelligence", "assessment evidence"],
  "exceptions": ["Ephemeral low-stakes personalization may retain no personal history when data minimization is preferable."],
  "falsifiers": ["The additional provenance does not improve calibration, contestability, debugging, or decision quality.", "Retention creates privacy risk greater than its learning value."],
  "last_reviewed": "2026-08-31"
}
---

# P002 — Use an evidence ledger for learner inferences

## Principle

Record the observation and the inference as different objects. Every consequential learner-state estimate should be answerable to: what happened, under which conditions, when, with what assistance, which model interpreted it, how certain is the estimate, and what may it be used for?

## Rationale

Learner models are probabilistic and construct-dependent [C007]. Trustworthy judgment requires a portfolio whose evidence remains interpretable [C008]. This infrastructure makes the learner model a compounding asset without converting it into unchallengeable surveillance [B003].

## Product patterns

- append-only observation events with correction records;
- versioned inferences and confidence;
- separate independent and AI-assisted evidence [B004];
- provenance links from recommendation back to observations;
- retention limits and user contestability;
- decision-specific permissions.

## Falsifiers and measures

Audit calibration, reversal after new evidence, explanation accuracy, user correction rates, privacy burden, and whether decisions improve against a simpler no-history baseline.
