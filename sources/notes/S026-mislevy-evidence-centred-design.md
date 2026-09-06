---
{
  "id": "S026",
  "type": "source",
  "title": "A Brief Introduction to Evidence-Centered Design",
  "citation_key": "mislevy2003ecd",
  "source_kind": "report",
  "epistemic_roles": ["theoretical-argument"],
  "year": 2003,
  "url": "https://doi.org/10.1002/j.2333-8504.2003.tb01908.x",
  "status": "reviewed",
  "topics": ["assessment-validity", "learner-modelling", "evidence-centred-design"],
  "added": "2026-09-06",
  "last_reviewed": "2026-09-06",
  "technology_dependence": "model-independent",
  "access": "open"
}
---

# S026 — Evidence-centred design

## Why it matters

Evidence-centred design provides the clearest inspected foundation for keeping what a learner did, how that work was interpreted, and the resulting learner-state estimate distinct. It makes task conditions part of the evidentiary argument rather than decoration around a score.

## Identity and provenance

- Canonical identifier: DOI 10.1002/j.2333-8504.2003.tb01908.x; ETS Research Report RR-03-16.
- Version inspected: the 2004 CRESST reissue, *CSE Report 632*, 33 pages; the canonical report is 2003.
- Content inspected: complete PDF, including the assessment argument, conceptual assessment framework and four-process architecture.
- Access and rights: public CRESST report; ERIC ED483399.
- Retrieval: gateway candidate `cand_3e95e3d1af71775e`; PDF SHA-256 `33021d4d020c70c70a3661fc731ec2ed533edf0c95b4e4e98a549c520c0525b7`.
- Locator convention: printed report page.

## Argument

- Pages 1–5 frame assessment as reasoning from the things learners say, do or make to claims about what they know or can do. The assessment argument coordinates the claims, observations and situations needed to support them.
- Pages 6–10 separate the student, evidence and task models. In the four-process architecture, a work product is processed into observable evidence, which then updates beliefs represented in the student model.
- The student-model variables are not directly observed and are represented probabilistically. Evidence rules identify observable features; a measurement model accumulates those features into distributions over learner-model variables.

## Implication for the Atlas

A captured task event should preserve the task, conditions, work-product reference and provenance. Rubric or scorer judgments should remain identifiable as response-processing assertions. A capability estimate should be a separately versioned inference linked back to those records. Assistance conditions belong with the task context; they do not themselves establish capability.

## Limitations and boundary conditions

- This is a foundational design framework, not a causal evaluation of any event schema or learner model.
- It does not determine an AI-assistance taxonomy, privacy policy, confidence scale or expiry period.
- The framework can make an inference chain explicit without making the inference valid; empirical validity evidence is still required for the intended use.

## Candidate claims

Strengthens [C007](../../claims/C007-learner-models-are-probabilistic-inferences.md) and the observation–inference boundary in [P002](../../principles/P002-use-an-evidence-ledger.md).
