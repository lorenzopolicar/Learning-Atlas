---
{
  "id": "C039",
  "type": "claim",
  "title": "Assistance function is a fallible classification, not a directly observed fact",
  "statement": "In authentic student–GenAI interaction logs, fine-grained assistance or process functions can be missing, selectively observed, and only moderately reproducible between annotators, so any assistance-function label should retain its taxonomy, classifier, uncertainty or disagreement, and correction status rather than enter a learner record as ground truth.",
  "status": "provisional",
  "confidence": "low",
  "topics": ["human-ai-collaboration", "assessment-validity", "learner-modelling", "product-measurement"],
  "supporting_sources": ["S065"],
  "contradicting_sources": [],
  "boundary_conditions": ["One observational study of argumentative writing in three university courses.", "Moderate reliability of one 35-category taxonomy does not establish the reliability of a simpler co-designed assistance vocabulary.", "Interaction logs may still add useful contextual evidence when their missingness and inference limits are explicit."],
  "product_relevance": "E001 should store declared or inferred assistance function as a versioned assertion with provenance, allow unknown and mixed states, measure agreement and missingness, and let the learner contest the label.",
  "last_reviewed": "2026-11-22"
}
---

# C039 — Assistance function is a fallible classification, not a directly observed fact

## Evidence and reasoning

In [S065], four annotators applied a 35-subcategory taxonomy to authentic student–GenAI logs. Mean pairwise kappa was .44, subcategory agreement varied widely, 33 of 103 reported users lacked a usable log, and making process quality part of grading may have reduced participation. The study's process/output correlation does not turn the categories into observed traits.

## Boundary conditions

The taxonomy was unusually detailed and domain-specific. A smaller vocabulary may be more reliable, especially when learners classify the function in context. That is a hypothesis to test, not a reason to treat the field as objective.

## Product relevance

Separate the interaction trace from the classification assertion. Preserve classification scheme/version, basis, classifier, time, confidence or disagreement, missingness, learner review, and correction chain. Compare the richer label with an `unknown`-tolerant minimal baseline on actual decision value.

