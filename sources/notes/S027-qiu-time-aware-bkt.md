---
{
  "id": "S027",
  "type": "source",
  "title": "Does Time Matter? Modeling the Effect of Time with Bayesian Knowledge Tracing",
  "citation_key": "qiu2011time",
  "source_kind": "conference-paper",
  "epistemic_roles": ["empirical-study"],
  "year": 2011,
  "url": "https://files.eric.ed.gov/fulltext/ED537453.pdf",
  "status": "reviewed",
  "topics": ["learner-modelling", "knowledge-tracing", "forgetting", "assessment-validity"],
  "added": "2026-09-06",
  "last_reviewed": "2026-09-06",
  "technology_dependence": "model-independent",
  "access": "open"
}
---

# S027 — Time-aware Bayesian knowledge tracing

## Why it matters

This paper is a useful null and contradiction for any universal evidence-expiry rule. Adding elapsed-time functions to knowledge tracing produced context-dependent results rather than a generally better model.

## Identity and provenance

- Authors: Yumeng Qiu, Yingmei Qi, Hanyuan Lu, Zachary Pardos and Neil Heffernan.
- Publication: *Proceedings of the 4th International Conference on Educational Data Mining*, 2011, pp. 139–148. No DOI was located; DBLP key `conf/edm/QiuQLPH11` provides a stable bibliographic identity.
- Content inspected: complete paper inside the 390-page open ERIC proceedings.
- Retrieval: official EDM/ERIC proceedings PDF; SHA-256 `048f4f189ea558965b7580355ec2f9f87d838e882610593cfce23950dfd00192`.
- Locator convention: paper page and table.

## Study

The authors compared standard Bayesian Knowledge Tracing with variants whose forgetting or slip probabilities depended on elapsed time. They evaluated prediction on Cognitive Tutor and ASSISTments data, including new-day predictions.

## Findings

- Time-aware variants improved some Cognitive Tutor predictions.
- They did not improve the new-day prediction setting and underperformed standard BKT on the ASSISTments data.
- The result is evidence against treating elapsed time as a universally monotonic, portable decay rule. Whether time helps depends on the dataset, model form and prediction target.

## Limitations and boundary conditions

- The study is old, uses two tutoring-system datasets and evaluates predictive fit rather than learning, transfer or a general capability construct.
- Model comparisons do not establish an individual learner's true forgetting curve.
- A null or reversal in these settings does not show that elapsed time is never informative. It shows that the temporal policy must be estimated and validated for its context and decision.

## Candidate claims

Supports [C013](../../claims/C013-time-does-not-create-a-universal-evidence-expiry-rule.md): preserve observation time, but apply decay or staleness only in a versioned, validated inference.
