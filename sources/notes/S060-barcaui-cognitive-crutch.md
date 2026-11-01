---
{
  "id": "S060",
  "type": "source",
  "title": "ChatGPT as a Cognitive Crutch: Evidence from a Randomized Controlled Trial on Knowledge Retention",
  "citation_key": "barcaui2025crutch",
  "source_kind": "randomized-controlled-trial",
  "epistemic_roles": ["empirical-study"],
  "year": 2025,
  "url": "https://doi.org/10.1016/j.ssaho.2025.102287",
  "status": "reviewed",
  "topics": ["learning-vs-performance", "transfer", "ai-tutoring", "cognitive-offloading"],
  "added": "2026-11-02",
  "last_reviewed": "2026-11-02",
  "technology_dependence": "model-dependent",
  "technology_context": {
    "system": "OpenAI ChatGPT web interface",
    "version": "GPT-4 label reported; exact snapshot not reported",
    "study_period": "not reported in the inspected article",
    "assessed_as_of": "2026-11-02",
    "temporal_relevance": "historical-system",
    "review_due": "2027-05-02",
    "recency_note": "The 45-day independent outcome remains directly relevant, but the GPT-4 intervention and unrecorded exposure need current-system replication."
  },
  "access": "open"
}
---

# S060 — ChatGPT as a cognitive crutch

## Why it matters

This is a rare randomized study with a surprise independent outcome after 45 days. Its direction challenges the positive one-week result in [S015], while its missing outcomes and unmonitored control compliance prevent a general causal verdict about unrestricted AI study.

## Identity and provenance

- Canonical identifiers: DOI 10.1016/j.ssaho.2025.102287; OpenAlex W4416818356; SSRN 5353041
- Version inspected: published *Social Sciences & Humanities Open* article, volume 12, article 102287
- Content inspected: published methods, conditions/materials, outcome, fidelity, results, limitations and appendices exposed through the publisher's open full-text page
- Access and rights: publisher open access, CC BY-NC-ND 4.0; Atlas candidate `cand_bb02de15a31548dd`
- Locator convention: sections 8.3, 8.5 and 8.6; tables 1 and 2; figure 5

## Study

- Population and setting: 120 Portuguese-speaking business-administration undergraduates aged 18–24 at one Brazilian university; 60 allocated per condition.
- Intervention and comparator: unrestricted ChatGPT study using the free GPT-4-labelled web interface versus non-AI study using course materials, library databases, ordinary search, textbooks and articles.
- Outcomes and timing: a proctored surprise conceptual-retention test about 45 days later; the 20-item instrument was machine scored and reported on a ten-point scale.
- Design: individually randomized two-arm study. Topic assignment was block-randomized by difficulty band. The primary analysis used the 85 learners who completed the follow-up test.

## Findings

- Forty-three AI-assisted and 42 traditional-study learners completed the delayed test. Mean scores were 5.75 and 6.85 respectively; `t(83)=-3.19`, `p=.002`, reported Cohen's `d=.68`, 95% CI `[.24, 1.12]` (table 2).
- Learners reported less study time in the AI condition, about 3.2 versus 5.8 hours. A covariate-adjusted analysis retained a smaller condition difference, but study time is post-treatment and cannot identify cognitive offloading as the mediator.
- Prior AI familiarity did not show a reliable association with retention. This null moderator result is underpowered and does not establish invariance across expertise.

## Limitations and boundary conditions

- Thirty-five of 120 randomized learners had no primary outcome. Completion counts were balanced by arm, but reasons and outcomes for non-completers were unavailable; the outcome-level RoB 2 judgement is high.
- Control-group AI non-use was not directly monitored, and the study did not report a preregistered analysis plan.
- Time-on-task and study behaviour were self-reported. The experiment randomized access policy, not equal exposure, effort or a cognitive-offloading mechanism.
- One institution, one course, familiar AI users and one conceptual test limit population and task generality. The test measured retention/near application, not far transfer or authentic capability.
- The intervention used a historical GPT-4-labelled web interface and did not report the study dates or exact model snapshot.

## Evidence profile

| Dimension | Rating | Reason |
|---|---|---|
| Internal validity | low-moderate | Random allocation and objective scoring, but 29% missing outcomes, unmonitored control compliance and no located preregistration |
| Directness | high | AI study access was manipulated and the outcome was independently proctored after 45 days |
| Consistency | low | Direction differs from the bounded positive one-week result in S015 and lacks independent replication |
| Replication | low | One trial at one institution |
| Magnitude | moderate | Reported standardized difference was `d=.68`, with substantial uncertainty from missing outcomes |
| Duration | moderate | Forty-five days is unusually long for current GenAI learning research |
| Transfer | low-moderate | Items tested conceptual application but stayed within the studied topic set |
| Ecological validity | moderate | Ordinary study resources and a natural delay, but a controlled single-course protocol |

## Candidate claims

Supports low-confidence [C036](../../claims/C036-unrestricted-chatgpt-study-lowered-retention.md). It also supports [C001](../../claims/C001-assisted-performance-is-not-learning.md) only as a delayed negative access-policy result; it does not establish cognitive offloading as the mechanism.

## Notes

A decisive replication would use a current system, record both arms' exposure, preserve accessible study options, minimize and explain loss to follow-up, and test delayed novel transfer.
