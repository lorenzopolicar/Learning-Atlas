---
{
  "id": "S059",
  "type": "source",
  "title": "Your Programming Students' Cognition with ChatGPT: Higher Performance, Lower Retention, and Reduced Ownership",
  "citation_key": "bergh2026cognition",
  "source_kind": "preprint",
  "epistemic_roles": ["empirical-study"],
  "year": 2026,
  "url": "https://arxiv.org/abs/2609.21194",
  "status": "reviewed",
  "topics": ["learning-vs-performance", "programming-education", "knowledge-retention", "human-ai-collaboration"],
  "added": "2026-10-25",
  "last_reviewed": "2026-10-25",
  "technology_dependence": "model-dependent",
  "technology_context": {
    "system": "OpenAI ChatGPT",
    "version": "ChatGPT-4.5 with memory disabled",
    "study_period": "not reported",
    "assessed_as_of": "2026-10-25",
    "temporal_relevance": "historical-system",
    "review_due": "2027-01-25",
    "recency_note": "The 48-hour authentic-task outcome is useful, but ChatGPT-4.5 and the uncontrolled usage modes require a current-system replication."
  },
  "access": "publisher-open"
}
---

# S059 — Programming cognition with ChatGPT

## Why it matters

This small authentic programming experiment reports the clearest inspected delayed signal in the current search: higher code-production scores with ChatGPT-4.5 but lower cued recall both immediately and 48 hours later. The stable gap, however, formed during the task and did not widen over the delay.

## Identity and provenance

- Canonical identifier: arXiv:2609.21194v1
- Version inspected: 18 September 2026
- Content inspected: complete PDF, methods, tables 2–4, results, discussion, limitations and funding statement
- Access and rights: publisher-open arXiv PDF
- Retrieval: gateway candidate `cand_975ec0ad114eebbd`; PDF SHA-256 `fedfae3936ad7c097a370a130460fff174e5dc46addcd1f3e0f0c50982a03bb6`
- Locator convention: numbered section, table and page in v1

## Study

- Population and setting: 59 first-year computer-science students at one Australian university; 55 were analyzed after physiological-quality and task-use exclusions.
- Intervention and comparator: gender-balanced pseudo-random assignment to ChatGPT-4.5 or conventional Google/web search with AI features disabled during three introductory C programming tasks in the familiar EdStem environment.
- Outcomes and timing: 30-minute coding score, self-report and physiology, followed by the same ten open-ended cued-recall questions immediately and 48 hours later without access to submitted code.
- Use heterogeneity: 15 of 29 AI participants copied task material and accepted generated responses; 14 primarily wrote code and used ChatGPT for validation or debugging. This was not randomized or prespecified.

## Findings

- ChatGPT-assisted coding performance was 89% versus 69% without AI (Hedges' g=1.24, Holm-adjusted p<.001).
- No-AI participants recalled more immediately: .53 versus .41 (g=.71, Holm-adjusted p=.011).
- The difference remained at 48 hours: .52 versus .39 (g=.77, Holm-adjusted p=.011).
- The group-by-time interaction was not significant (p=.391). The result is an acquisition/encoding gap that persisted for 48 hours, not evidence of faster forgetting.
- No-AI participants spent 24.1 minutes on average versus 16.4 minutes with AI; this exposure difference was descriptive and not experimentally equalized.

## Limitations and boundary conditions

- The small, self-selected, single-site cohort and pseudo-random allocation limit internal and external validity; no baseline knowledge test was reported.
- Assistance mode was uncontrolled and split between answer acceptance and validation/debugging, so the study cannot identify which interaction produced the gap.
- Time on task differed materially. The total treatment includes reduced exposure and cannot isolate cognitive offloading as a mechanism.
- Cued recall of code content is near-task retention, not delayed independent coding transfer.
- Task order was fixed, study dates were unreported, and ChatGPT-4.5 is now a historical system.
- The preprint reports Google.org grant support.

## Evidence profile

| Dimension | Rating | Reason |
|---|---|---|
| Internal validity | low-moderate | Controlled pseudo-random comparison; no baseline, unequal exposure and uncontrolled use |
| Directness | high | Authentic supported task plus immediate and 48-hour unsupported recall |
| Consistency | moderate | Aligns with performance–learning divergence; delayed current-system replication absent |
| Replication | low | One preprint and 55 analyzed participants |
| Magnitude | large | Assisted g=1.24 and recall gaps g=.71–.77 |
| Duration | moderate-low | 48 hours |
| Transfer | low | Cued recall of the same code/task content |
| Ecological validity | moderate | Real students and familiar environment; constrained laboratory session |

## Candidate claims

Supports [C001](../../claims/C001-assisted-performance-is-not-learning.md) as a delayed authentic-task signal. It does not establish a durable capability loss, accelerated forgetting, or a mechanism attributable to answer delegation.

## Notes

The most informative replication would randomize answer generation versus debugging/validation, equalize exposure, include a baseline, and test delayed novel coding performance rather than only recall.
