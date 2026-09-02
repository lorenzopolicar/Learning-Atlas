---
{
  "id": "S020",
  "type": "source",
  "title": "Appropriate Reliance on AI Advice: Conceptualization and the Effect of Explanations",
  "citation_key": "schemmer2023appropriate",
  "source_kind": "conference-paper",
  "epistemic_roles": ["empirical-study", "theoretical-argument"],
  "year": 2023,
  "url": "https://doi.org/10.1145/3581641.3584066",
  "status": "reviewed",
  "topics": ["human-ai-collaboration", "assessment-validity", "product-measurement", "metacognition"],
  "added": "2026-08-31",
  "last_reviewed": "2026-08-31",
  "technology_dependence": "mechanism-oriented",
  "access": "open"
}
---

# S020 — Appropriate Reliance on AI Advice

## Why it matters

The paper separates two behaviours that a final accuracy score collapses: correctly adopting AI advice after an initially wrong judgment and correctly resisting AI advice after an initially correct judgment. This is a useful measurement primitive for bounded supervisory tasks, not a complete measure of learning or agency.

## Identity and provenance

- DOI: 10.1145/3581641.3584066; IUI 2023 conference paper
- Version inspected: complete author-hosted arXiv preprint, arXiv:2302.02187
- Content inspected: full text, measures, hypotheses, results, discussion and appendices relevant to the experiment
- Retrieval: gateway record `cand_aabb11b83b1fbfb4`; PDF SHA-256 `3238886354f687e7893898ff8d3f6fcdc93f0f1e5ab3f09b116a1e2546dab161`
- Locator convention: numbered sections, equations, figures and tables in the inspected preprint

## Study

- Population and setting: 200 Prolific participants; one was excluded. Mean age was 27.5. Participants classified hotel reviews as genuine or deceptive.
- Intervention and comparator: participants first made a classification and reported confidence, then saw AI advice either with or without a LIME explanation, and could revise both.
- Task and model: 16 experimental trials. The underlying support-vector machine was 86% accurate, but the experiment deliberately sampled equal numbers of correct and incorrect AI recommendations.
- Design: between-participant explanation condition with repeated sequential decisions. The task creates observable human–AI disagreement cases and known correctness.

## Findings

- Relative AI reliance (RAIR) was defined as switching from an initially wrong human answer to correct AI advice. Relative self-reliance (RSR) was defined as retaining an initially correct human answer when AI advice was wrong.
- Mean RAIR was 29.59% without explanations and 38.87% with explanations (`p = .05`). Mean RSR was 71.87% and 69.45%, respectively (`p = .54`). The explanation therefore affected one reliance component but not the other.
- Relative to the initial human decision, final accuracy changed by -1.56 percentage points in the control condition and +2.45 points in the explanation condition (`p = .02` for the difference). Neither condition produced complementary performance above both the human and AI baselines.
- Trust or agreement alone would not reveal whether a participant accepted correct advice or accepted incorrect advice. The initial judgment and the correctness of both parties are necessary for the two-sided interpretation.

## Limitations and boundary conditions

- The task was short, artificial, binary and objectively scored. Participants were crowd workers whose initial accuracy was close to chance, not learners developing a consequential domain capability.
- A self-first sequence can anchor the participant and makes the measurement procedure part of the intervention. No feedback, delayed outcome, transfer measure or longitudinal learning outcome was included.
- RAIR and RSR require enough initial-error/AI-correct and initial-correct/AI-error cases. They are undefined or unstable with few disagreements and do not directly apply where truth is plural or delayed.
- LIME explanations and one classifier do not represent contemporary open-ended generative collaboration. Improved RAIR did not establish better resistance, authorship, responsibility or durable learning.

## Evidence profile

| Dimension | Rating | Reason |
|---|---|---|
| Internal validity | moderate | Controlled experiment with known correctness; sequential design and near-chance human performance shape behaviour |
| Directness | moderate | Direct for observable advice-taking, indirect for educational capability |
| Consistency | unclear | One experiment and one explanation format |
| Replication | low | No independent replication assessed in this pass |
| Magnitude | low-moderate | Explanation shifted RAIR by about nine points but not RSR |
| Duration | low | Sixteen trials, no delay |
| Transfer | low | No transfer outcome |
| Ecological validity | low | Artificial hotel-review classification by crowd workers |

## Candidate claims

Supports [C010](../../claims/C010-appropriate-reliance-has-distinct-components.md). It supplies task-level evidence for [C008](../../claims/C008-trustworthy-assessment-needs-multiple-evidence-channels.md), but it does not validate an overall human–AI capability score.
