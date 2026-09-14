---
{
  "id": "S044",
  "type": "source",
  "title": "Socrates went Nuclear: Comparing Interaction Strategies for AI systems in a Learning Context using Brain Sensing",
  "citation_key": "deffarges2026socrates",
  "source_kind": "preprint",
  "epistemic_roles": ["empirical-study"],
  "year": 2026,
  "url": "https://arxiv.org/abs/2609.00584",
  "status": "reviewed",
  "topics": ["ai-tutoring", "scaffolding", "learning-vs-performance", "motivation-and-agency"],
  "added": "2026-09-14",
  "last_reviewed": "2026-09-14",
  "technology_dependence": "model-dependent",
  "technology_context": {
    "system": "OpenAI",
    "version": "GPT-5.2",
    "study_period": "not reported",
    "assessed_as_of": "2026-09-14",
    "temporal_relevance": "current-system",
    "review_due": "2027-03-14",
    "recency_note": "The study uses a current-generation model and directly manipulates answer withholding, but only in a small exploratory laboratory task with an immediate model-graded outcome."
  },
  "access": "publisher-open"
}
---

# S044 — Socrates went Nuclear

## Why it matters

This is a direct current-generation counterexample to universal answer withholding. With the same chatbot interface and model, a strict Socratic policy that never supplied the final answer produced lower immediate gains and more abandonment than unrestricted access.

## Identity and provenance

- Canonical identifier: arXiv:2609.00584v1; proceedings DOI `10.1145/3841580.3841620` for HAI 2026.
- Version inspected: 1 September 2026 preprint, 11-page complete PDF.
- Content inspected: design, conditions, prompt appendix, tables 1–3, interaction analysis, results and limitations.
- Access and rights: publisher-open arXiv PDF, CC BY-NC-ND 4.0; no full text is stored in Git.
- Retrieval: gateway candidate `cand_69640316b57e80c9`; PDF SHA-256 `b0118b5d9c9f4902edd89a5b2fdb372b774dd563e7a5022c72f15465f2f6ec01`.
- Locator convention: section, table and page in v1.

## Study

- Population and setting: 50 adults allocated sequentially across unrestricted chatbot (`n=17`), Socratic chatbot (`n=17`) and adaptive non-conversational tutor (`n=16`) conditions in a laboratory nuclear-safety lesson.
- Intervention and comparator: the unrestricted and Socratic conditions used the same interface and GPT-5.2. The unrestricted bot could answer directly. The Socratic prompt never gave a final answer and instead used questions, targeted hints and restatement. The third condition added EEG-adaptive subquestions and visual feedback.
- Outcomes and timing: pretest, ten open-ended assisted assessment questions, immediate post-test, EEG engagement, interaction strategies, perceived learning, difficulty and helpfulness.
- Grading: GPT-5.2 graded answers against a fixed rubric; informal human spot checks were not retained as independent ratings.

## Findings

- Mean pre-to-post gain was 20.12 in the unrestricted condition, 10.52 in Socratic and 11.20 in adaptive. Unrestricted outperformed Socratic (`p=.025`, `d=.80`) and adaptive (`p=.021`, `d=.85`); Socratic and adaptive did not differ (table 1; section 5.2).
- Socratic learners' chatbot and EEG engagement declined later in the session. Fifty-eight percent of their exercises that abandoned dialogue did not reach the platform's 80% threshold (sections 5.3–5.4).
- Learners rated unrestricted support more helpful than Socratic support, 8.62 versus 5.67 out of 10 (`p<.0001`, `d=1.75`).
- The authors explicitly warn that the immediate test can reward recently viewed complete answers and does not establish deeper or long-term learning.

## Limitations and boundary conditions

- Fifty participants across three cells provide exploratory evidence only; allocation was sequential rather than clearly concealed randomization.
- The post-test was immediate and closely matched to the lesson. There was no delayed retention or transfer assessment.
- Model-generated grading has no recorded human inter-rater reliability.
- The Socratic policy was absolute: it could not reveal an answer or flexibly exit. The result challenges rigid withholding, not calibrated progressive help with a learner-controlled reveal.
- Topic interest was low and the task was a short artificial nuclear-safety lesson.
- The proceedings event occurs after this review date; the inspected artifact is a preprint.

## Evidence profile

| Dimension | Rating | Reason |
|---|---|---|
| Internal validity | moderate-low | Same model/interface for the main contrast, but small sequential groups and unvalidated model grading |
| Directness | high | Directly compares unrestricted answers with strict question-and-hint withholding |
| Consistency | low-moderate | Aligns with pacing concerns in S043 but conflicts with simple productive-struggle predictions |
| Replication | low | One exploratory preprint |
| Magnitude | moderate | Large immediate performance and helpfulness differences in a small sample |
| Duration | low | Immediate post-test only |
| Transfer | low | Closely matched task and content |
| Ecological validity | low | Artificial topic, laboratory interface and short exposure |
| Technology directness | moderate-high | Current-generation model, but not an Orqestra deployment and exact study dates are unreported |

## Candidate claims

Supports [C029](../../claims/C029-rigid-answer-withholding-can-backfire.md) and challenges overgeneralization from [C011](../../claims/C011-delayed-access-can-beat-always-on.md). It does not establish that answer-first support improves durable learning.

## Notes

The useful contradiction is policy-shaped: an escape hatch and pacing logic may be constitutive parts of progressive assistance, not optional usability polish.
