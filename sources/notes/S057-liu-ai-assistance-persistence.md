---
{
  "id": "S057",
  "type": "source",
  "title": "AI Assistance Reduces Persistence and Hurts Independent Performance",
  "citation_key": "liu2026assistance",
  "source_kind": "conference-paper",
  "epistemic_roles": ["empirical-study"],
  "year": 2026,
  "url": "https://arxiv.org/abs/2604.04721",
  "status": "reviewed",
  "topics": ["learning-vs-performance", "cognitive-offloading", "assessment-validity", "human-ai-collaboration"],
  "added": "2026-10-25",
  "last_reviewed": "2026-10-25",
  "technology_dependence": "model-dependent",
  "technology_context": {
    "system": "OpenAI GPT-5",
    "version": "GPT-5 snapshot not reported",
    "study_period": "not reported; UCLA protocol IRB-25-2012",
    "assessed_as_of": "2026-10-25",
    "temporal_relevance": "current-system",
    "review_due": "2027-04-25",
    "recency_note": "Current-generation direct-answer assistance, but the exact snapshot and study dates are missing and the intervention was maximally answer-ready."
  },
  "access": "publisher-open"
}
---

# S057 — AI assistance reduces persistence and independent performance

## Why it matters

This is the strongest current-generation causal evidence in the review that assisted success can reverse immediately after support is removed. Three randomized experiments used GPT-5 during brief arithmetic or reading tasks and then tested the same outcome family without AI.

## Identity and provenance

- Canonical identifiers: arXiv:2604.04721v6; DOI 10.48550/arXiv.2604.04721; COLM 2026 conference paper
- Version inspected: 13 October 2026
- Content inspected: complete PDF, experiments 1–3, appendices relevant to assignment and attrition, conclusion and limitations
- Access and rights: publisher-open arXiv PDF
- Retrieval: gateway candidate `cand_a0445cb4aa5eeb75`; PDF SHA-256 `6025a4b27ad25f12056da64f756b6d626a500420618575de762fc3a45eb415e9`
- Locator convention: numbered experiment/section, figure and page in v6

## Study

- Population and setting: 1,222 US Prolific adults recruited across three short online experiments; analyzed samples were 305, 585 and 168 after exclusions.
- Intervention and comparator: GPT-5 was preloaded with each problem and solution and could return a complete answer from a minimal prompt; controls completed the same items without AI.
- Outcomes and timing: learning-phase solve/skip rates followed by three immediate independent problems after the sidebar was removed without warning.
- Design: individually randomized experiments on fraction arithmetic and SAT-style reading comprehension. Experiment 2 added a pretest and matched the sidebar-removal interface transition to address experiment 1's selective-exclusion and interface confounds.

## Findings

- AI improved assisted solve rates and reduced skipping during the learning phase in the fraction experiments.
- Experiment 1 independent fraction performance was lower with prior AI access: solve rate .57 versus .74 (d=-.45, p<.001); skip rate .20 versus .11 (d=.27, p=.020). Its post-randomization exclusion could selectively retain lower-skill AI users.
- Experiment 2 preserved the independent solve-rate penalty after pretest-based exclusions and a matched interface shift: .71 versus .77 (d=-.20, p=.019). The aggregate skip-rate difference was not significant.
- Experiment 3 replicated the withdrawal pattern in reading: solve rate .76 versus .89 (d=-.42, p=.007); skip rate .08 versus .01 (d=.42, p=.008).
- Usage-category contrasts, including the poorer outcomes of self-reported direct-answer users, are post-treatment and cannot identify a causal mechanism.

## Limitations and boundary conditions

- Exposure lasted only about 10–15 minutes and the independent test followed immediately; the paper cannot establish retained learning loss, durable deskilling or cumulative harm.
- The assistant was maximally helpful and answer-ready, and support disappeared without warning. Effects may partly reflect acute withdrawal, changed expectations or the specific direct-answer interaction.
- Each independent outcome contained only three items, and online adult microtasks have limited educational and ecological coverage.
- Study dates and the exact GPT-5 snapshot were not reported.
- Persistence was operationalized as skipping despite no penalty for an incorrect answer. It is consequential behaviour, but not a stable motivational trait.

## Evidence profile

| Dimension | Rating | Reason |
|---|---|---|
| Internal validity | moderate-high | Three randomized experiments; the latter two address major exclusion and interface confounds |
| Directness | high | Manipulates AI availability and measures performance after removal |
| Consistency | moderate-high | Direction replicates across arithmetic and reading, with a mixed persistence result |
| Replication | moderate-low | Internal replication only; one research programme |
| Magnitude | small-moderate | Independent-performance effects d=-.20 to -.45 |
| Duration | low | Immediate withdrawal only |
| Transfer | low | New items in the same task families |
| Ecological validity | low | Brief Prolific microtasks with an unusually answer-ready assistant |

## Candidate claims

Supports [C001](../../claims/C001-assisted-performance-is-not-learning.md): strong assisted performance is not evidence of independent capability. The narrow inference is an immediate post-removal penalty under answer-ready GPT-5 assistance, not durable deskilling.

## Notes

A decisive replication would randomize answer-ready versus hint-first assistance, match time and interface transitions, and add delayed novel independent tasks over multiple sessions.
