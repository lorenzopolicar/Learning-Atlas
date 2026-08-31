---
{
  "id": "S015",
  "type": "source",
  "title": "Experimental Evidence on the Learning Impact of Generative AI",
  "citation_key": "contractor2026experimental",
  "source_kind": "preprint",
  "epistemic_roles": ["empirical-study"],
  "year": 2026,
  "url": "https://arxiv.org/abs/2607.08849",
  "status": "reviewed",
  "topics": ["learning-vs-performance", "ai-tutoring", "assessment-validity", "human-ai-collaboration"],
  "added": "2026-08-31",
  "last_reviewed": "2026-08-31",
  "access": "open"
}
---

# S015 — Experimental Evidence on the Learning Impact of Generative AI

## Why it matters

This is a rare controlled GenAI study that measures unaided performance both immediately and after a delay. It is an important positive counterweight to studies in which assisted output gains disappear or reverse once support is removed.

## Identity and provenance

- Canonical identifier: arXiv:2607.08849v1
- Version inspected: 9 July 2026 preprint by Zara Contractor and Germán Reyes
- Content inspected: full text, methods, main results, appendices relevant to treatment compliance and use classification
- Access and rights: publisher-open arXiv PDF; page declares CC BY 4.0
- Retrieval: gateway record `cand_aea65662c7ad1943`; PDF SHA-256 `d5ea73073c4400924a5e73d21399e54f80d279f0f75383b804df60b56fcfcc05`
- Locator convention: numbered section, table and appendix labels in v1

## Study

- Population and setting: 211 Middlebury College undergraduates in Spring 2025; 204 returned for session two. The sample was academically selective (mean GPA 3.68; mean SAT 1386) and more than 80% were already familiar with AI.
- Intervention and comparator: random assignment to generative-AI-allowed or AI-forbidden conditions during a 35-minute learning-and-writing phase. The AI condition received a logged-in GPT-4o account; the control retained ordinary web access.
- Task: learn one unfamiliar technical topic—blockchain, carbon capture, or CRISPR—and write an approximately 500-word analytical essay.
- Outcomes: unaided five-item knowledge test immediately after learning; unaided ten-item test and a new analytical essay about seven days later.
- Design: eight time slots with parallel treatment labs, randomized computers and topic/prompt assignments, proctor observation, platform logs and session fixed effects.

## Findings

- Assignment raised observed ChatGPT use by 67.3 percentage points. Immediate unaided knowledge was 6.7 points higher (0.27 SD, p=.034); one-week unaided retention was 5.1 points higher (0.27 SD, p=.027), about 76% of the immediate point estimate (sections 4.1, 4.2 and 5.1; tables 3 and 4).
- On the delayed essay, style/clarity improved by 0.30 SD and relevance by 0.26 SD; the 0.20 SD overall-quality estimate was imprecise (section 5.2; table 6).
- Total learning time did not change. Treated learners shifted about 5.3 percentage points away from writing and 4.4 points toward reading/searching, and reported 0.66/10 higher enjoyment (section 4.4; table 7).
- Test-rule violations rose by 12.6 percentage points. The authors estimate they could explain at most roughly one third of the immediate test effect under a deliberately conservative assumption (section 4.4; table 7).
- Conversation logs were classified after treatment: 49% of AI users as pure augmentation, 32% automation, 8% mixed and 11% other. Automation users' assisted essay advantage disappeared later, while augmentation users retained a positive but imprecise delayed test estimate (section 5.3; table 8).

## Limitations and boundary conditions

- Randomization identifies access to AI, not the causal effect of augmentation versus automation; those modes were chosen by students and classified post-treatment.
- The lab held time-on-task approximately fixed. In normal coursework, learners may use AI to save time and then reallocate it away from learning.
- The study covers one selective US institution, three unfamiliar topics, a short delay and near transfer. It does not establish long-horizon, far-transfer or population-wide effects.
- Four protocol variations occurred across early sessions; session fixed effects were used, but implementation was not perfectly uniform.
- Subgroup differences—especially smaller effects in the lowest GPA/SAT quartiles—are concerning but mostly imprecise.
- This is a preprint and has not yet supplied independent replication.

## Evidence profile

| Dimension | Rating | Reason |
|---|---|---|
| Internal validity | moderate-high | Random assignment, strong first stage and low attrition; some noncompliance, rule violations and protocol variations |
| Directness | high | Directly tests assisted learning followed by unaided immediate and delayed outcomes |
| Consistency | unclear | One study; it differs from several negative or null GenAI learning results |
| Replication | low | Preprint at one institution |
| Magnitude | moderate | 0.27 SD on both immediate and one-week tests |
| Duration | low-moderate | One-week retention only |
| Transfer | low | New questions and essay prompt, but the same topic and near task family |
| Ecological validity | moderate-low | Real students and ordinary AI, but a tightly timed paid laboratory task |

## Candidate claims

Supports provisional [C009](../../claims/C009-off-the-shelf-ai-can-improve-short-delay-learning.md). It qualifies—not overturns—[C001](../../claims/C001-assisted-performance-is-not-learning.md): assisted performance remains an invalid proxy, but the measured unaided outcome can be positive. The automation/augmentation pattern is a hypothesis-generating mechanism result, not a randomized comparison.
