---
{
  "id": "S053",
  "type": "source",
  "title": "Effectiveness of Adaptive Versus Non-Adaptive Intelligent Tutoring Systems in Early Primary Mathematics",
  "citation_key": "sibley2026adaptive",
  "source_kind": "journal-article",
  "epistemic_roles": ["empirical-study"],
  "year": 2026,
  "url": "https://doi.org/10.1016/j.caeo.2026.100420",
  "status": "reviewed",
  "topics": ["learner-modelling", "knowledge-tracing", "scaffolding", "mathematics"],
  "added": "2026-10-11",
  "last_reviewed": "2026-10-11",
  "technology_dependence": "model-independent",
  "access": "open"
}
---

# S053 — Isolated difficulty adaptation versus a matched fixed tutor

## Why it matters

This is a direct falsifier for any claim that adaptivity is inherently superior. The experiment held content, interface, feedback and graduated hints constant and changed only whether task difficulty followed a learner model or a textbook-like fixed sequence.

## Identity and provenance

- Authors: Leonie Sibley, Tobias Berner and Thomas Schmalfeldt.
- Publication: *Computers and Education Open*, 11, 100420; DOI `10.1016/j.caeo.2026.100420`.
- Version inspected: complete eight-page version of record from Zenodo record `22256219`.
- Access and rights: CC BY 4.0; no full text is stored in Git.
- Retrieval: gateway candidate `cand_0b08f775f6c0ab28`; PDF SHA-256 `a33ca478bee3a2da7d7ad5aa69c54d6c6f796aa9f358ea1ad4baadc835eb4359`.
- Locator convention: version-of-record page, table and appendix.

## Study

- Population and setting: 132 second-grade learners in 11 Swiss classes during ordinary mathematics instruction.
- Design: randomized two-group pretest–posttest field experiment; adaptive n = 65 and fixed n = 67.
- Intervention: CTAT's “Sequential Mastery Learning — Easier First” used default Bayesian Knowledge Tracing parameters to skip skills estimated as mastered and retain learners on unmastered skills.
- Comparator: the same tutor, arithmetic content, immediate feedback and graduated audio hints in a fixed textbook-like order across 13 skills.
- Outcome: an immediate 15-item parallel paper posttest after one 30-minute practice session.

## Findings

- Adaptive and fixed sequences did not differ on the primary posttest: adjusted F(1,124) = 0.32, p = .574, partial eta squared = .00; means were 10.30 and 9.98 of 15 (table 1; page 5).
- There was no condition effect on mental effort, subjective difficulty or enjoyment, and no learning-performance moderation by prior knowledge or the exploratory learner profiles.
- Fixed-sequence learners reached higher intervention-derived mastery probabilities, 0.67 versus 0.58, F(1,128) = 7.85, p = .006. An exploratory model controlling this post-treatment quantity favoured adaptation, but the authors correctly reject a causal interpretation.

## Limitations and boundary conditions

- Thirty minutes may be too short for a learner model to accumulate decision-useful evidence. The study has no delayed retention or transfer outcome.
- Default BKT parameters were not calibrated for this population. Mastery gating may have reduced curricular progression for the adaptive group.
- The sample is limited to young learners and structured arithmetic. A null here does not contradict long-horizon personalized spacing or richer sequencing policies.
- The fixed comparator was strong and structurally matched, making the null especially relevant to incremental-value claims.

## Evidence profile

| Dimension | Rating | Reason |
|---|---|---|
| Internal validity | high for the primary contrast | Randomized and matched except for task selection |
| Directness | high | Isolates adaptive difficulty selection from a transparent fixed sequence |
| Consistency | moderate-low | Direct null against positive long-horizon results [S051, S052] |
| Replication | low | One short field experiment |
| Magnitude | null | Partial eta squared was .00 |
| Duration | low | One 30-minute session and immediate posttest |
| Transfer | low | Parallel arithmetic test without delay |
| Ecological validity | moderate-high | Regular classrooms across 11 classes |

## Candidate claims

Supports [C034](../../claims/C034-short-difficulty-adaptation-can-add-no-value.md): isolated, short-horizon difficulty adaptation can add no learning value over a matched fixed sequence. It contradicts any unconditional reading of [C033](../../claims/C033-personalized-sequencing-can-beat-fixed-practice.md).
