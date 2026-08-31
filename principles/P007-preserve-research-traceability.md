---
{
  "id": "P007",
  "type": "principle",
  "title": "Preserve traceability from source to decision",
  "statement": "Every consequential learning-system principle and decision should be traceable through explicit reasoning to bounded claims and inspected sources, while contradictions and normative choices remain visible.",
  "status": "active",
  "confidence": "high",
  "topics": ["ethics-and-governance", "product-measurement", "institutional-design"],
  "based_on": ["C007", "C008", "B003"],
  "applies_to": ["research synthesis", "product design", "agent retrieval", "governance"],
  "exceptions": ["Exploratory ideas may remain explicitly labelled hypotheses before an evidence chain exists."],
  "falsifiers": ["Traceability adds no meaningful reproducibility, review, correction, or decision value relative to its maintenance cost."],
  "last_reviewed": "2026-08-31"
}
---

# P007 — Preserve traceability from source to decision

## Principle

Do not collapse sources, claims, beliefs, and design advice into an authoritative-sounding paragraph. Link them so a person or agent can inspect what supports a decision, where it might fail, and which part is normative judgment.

## Rationale

Inference without provenance becomes brittle authority [C007]. Multiple evidence channels help only when their meaning is preserved [C008]. An evidence-backed learner and product model compounds value through inspectability [B003].

## Product patterns

- stable IDs and typed relations;
- boundary conditions at retrieval time;
- decision records that cite principles and claims;
- source appraisal before claim promotion;
- explicit tensions and falsifiers;
- versioned changes rather than silent overwrites.

## Falsifiers and measures

Measure time to audit or correct a claim, rate of broken references, reviewer comprehension, decision reversibility, and retrieval usefulness to coding agents.
