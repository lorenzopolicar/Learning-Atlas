---
{
  "id": "P002",
  "type": "principle",
  "title": "Use an evidence ledger for learner inferences",
  "statement": "Keep learner observations, scored assertions, and model inferences as linked but separate records; preserve purpose-minimal provenance and context while giving inference validity, authorized use, and retention distinct controls.",
  "status": "active",
  "confidence": "high",
  "topics": ["learner-modelling", "assessment-validity", "ethics-and-governance"],
  "based_on": ["C007", "C008", "C013", "B003", "B004"],
  "applies_to": ["learner profiles", "adaptive sequencing", "capability intelligence", "assessment evidence"],
  "exceptions": ["Ephemeral low-stakes personalization may retain no personal history when data minimization is preferable."],
  "falsifiers": ["The additional provenance does not improve calibration, contestability, debugging, or decision quality.", "Retention creates privacy risk greater than its learning value."],
  "last_reviewed": "2026-09-06"
}
---

# P002 — Use an evidence ledger for learner inferences

## Principle

Record the observation, any scored assertion about it, and the learner-state inference as different objects. Every consequential estimate should be answerable to: what happened, which observer or rule asserted an observable, under which task and assistance conditions, which model interpreted it, how certain the estimate is, and what decision may use it?

## Rationale

Learner models are probabilistic and construct-dependent [C007]. Evidence-centred design separates work products, observables and student-model variables [S026], while time-aware knowledge tracing does not support a universal expiry rule [C013]. Trustworthy judgment requires a portfolio whose evidence remains interpretable [C008]. This infrastructure makes the learner model a compounding asset without converting it into unchallengeable surveillance [B003].

## Product patterns

- append-only observation events with occurrence time, recorded time and observer or sensor provenance [S028];
- typed, correctable scoring assertions with rubric or evidence-rule provenance;
- versioned inferences with model identity, evidence links, typed uncertainty, calibration boundary and supersession;
- separate accessible-independent, AI-assisted and supervisory/recovery evidence, including assistance function [B004];
- assistance permission, declaration, observation and classification basis kept distinct;
- provenance links from recommendation back to observations;
- optional self-reported confidence with scale and elicitation provenance, never confused with model uncertainty;
- distinct controls for inference review or staleness, authorized use, and record retention;
- purpose-minimal collection, decision-specific permissions and user contestability.

## Falsifiers and measures

Audit calibration, reversal after new evidence, explanation accuracy, scorer and assistance-classification disagreement, user correction rates, privacy burden, and whether decisions improve against a simpler no-history baseline. Drop fields whose marginal decision value does not justify their measurement or privacy cost.
