---
{
  "id": "S023",
  "type": "source",
  "title": "Fast and Forgettable: A Controlled Study of Novices' Performance, Learning, Workload, and Emotion in AI-Assisted and Human Pair Programming Paradigms",
  "citation_key": "gardella2026fast",
  "source_kind": "preprint",
  "epistemic_roles": ["empirical-study"],
  "year": 2026,
  "url": "https://arxiv.org/abs/2604.18538",
  "status": "reviewed",
  "topics": ["learning-vs-performance", "programming-education", "human-ai-collaboration", "cognitive-load"],
  "added": "2026-09-01",
  "last_reviewed": "2026-09-01",
  "access": "publisher-open"
}
---

# S023 — Fast and Forgettable

## Why it matters

This study measures exactly the divergence the Atlas is designed to preserve: performance on the same programming-task family while working with GitHub Copilot or a human peer, followed by individual performance without either teammate after one week. It also observes workload and affect, showing why a faster, easier interaction is not a sufficient learning signal.

## Identity and provenance

- Canonical identifier: arXiv:2604.18538v1
- Version inspected: 20 April 2026 preprint submitted to ACM
- Content inspected: complete PDF, including design, procedure, tables 1–3, discussion, threats to validity and linked supplement identity
- Access and rights: publisher-open arXiv PDF; abstract page links CC BY-NC-SA 4.0
- Retrieval: gateway candidate `cand_23d6408ebf85a9b0`; PDF SHA-256 `8ed0fe3361656d014d953626e3358504bd515bbf456af5d01d722727d7bab2b0`
- Locator convention: numbered section, table and page in v1

## Study

- Population and setting: 22 novice/intermediate Python programmers at a selective eastern-US research university; convenience recruitment; 16 men and 6 women; 4 participants reported a physical, cognitive or attentional impairment.
- Intervention and comparator: counterbalanced within-subject trials on different matched HumanEval task pools, once with GitHub Copilot/GPT-4.1 and once with a similarly skilled human partner.
- Outcomes and timing: 20-minute assisted team performance, workload and affect in session one; individual repetition of both task pools without Copilot or a human partner approximately one week later.
- Design: controlled within-subject laboratory study with 11 human pairs, task/order counterbalancing and clustered bootstrap inference. Participants were incentivized to balance productivity and understanding and knew a retention test would occur, but did not know it would repeat the same tasks.

## Findings

- Copilot raised session-one performance by 14.09 points on the 100-point speed/completion measure relative to a human partner (adjusted p<.001; Hedges' g=.99; table 1).
- One-week absolute individual retest performance was 4.79 points lower for task pools first completed with Copilot, but the estimate was imprecise and non-significant (95% CI -16.86 to 7.46; adjusted p=.529; g=-.27; table 2).
- The drop from assisted session-one performance to individual retest was 18.88 points larger after Copilot exposure (95% CI -32.87 to -5.01; unadjusted p=.015; multiplicity-adjusted p=.054; g=-1.13). This is a performance–learning divergence, not reliable evidence that Copilot caused worse absolute learning.
- Copilot reduced reported mental demand, temporal demand and effort by about 23–29 points on the NASA-TLX dimensions, with large effects. Human collaboration produced more positive and arousing affect.

## Limitations and boundary conditions

- Twenty-two self-selected volunteers provide little power for an absolute learning contrast and very limited population coverage.
- The comparator is a human peer, not unaided practice; both conditions contain assistance and social/task differences.
- Retest items repeat the same task pools, so this is retention/very-near transfer rather than novel programming capability.
- The fixed 20-minute session and reliable, simple HumanEval tasks may exaggerate the amount of spare study time available after Copilot completion.
- Participants knew a retention assessment would occur and had received a Copilot workshop, limiting transfer to ordinary use.
- The paper is a preprint. Several subgroup results are exploratory, and the main absolute independent-outcome contrast is null.

## Evidence profile

| Dimension | Rating | Reason |
|---|---|---|
| Internal validity | moderate | Within-person counterbalancing and robust clustered inference; small multi-level sample and peer comparator complicate inference |
| Directness | high | Measures supported performance and the same learners' one-week unassisted performance |
| Consistency | moderate | Aligns with a performance/learning gap, but the absolute retest contrast is inconclusive |
| Replication | low | One preprint and 22 participants |
| Magnitude | mixed | Large assisted gain and relative drop; small, imprecise absolute retest difference |
| Duration | moderate-low | Approximately one week |
| Transfer | low | Repeated task pools |
| Ecological validity | moderate-low | Real tools and plausible programming tasks in a tightly controlled laboratory |

## Candidate claims

Supports [C001](../../claims/C001-assisted-performance-is-not-learning.md): a large assisted advantage did not produce a reliable independent advantage one week later. It does not establish that Copilot reduces absolute learning.

## Notes

The study argues for keeping assisted score, absolute later score and change-from-assisted score separate. The last measure can become mechanically dramatic when the system inflates the starting point.
