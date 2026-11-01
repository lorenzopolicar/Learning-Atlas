---
{
  "id": "S061",
  "type": "source",
  "title": "Generative AI and the Temporary Upskilling of Knowledge Workers",
  "citation_key": "wiles2026upskilling",
  "source_kind": "randomized-controlled-trial",
  "epistemic_roles": ["empirical-study"],
  "year": 2026,
  "url": "https://doi.org/10.1038/s41562-026-02566-6",
  "status": "reviewed",
  "topics": ["learning-vs-performance", "human-ai-collaboration", "transfer", "assessment-validity"],
  "added": "2026-11-02",
  "last_reviewed": "2026-11-02",
  "technology_dependence": "model-dependent",
  "technology_context": {
    "system": "OpenAI ChatGPT",
    "version": "GPT-4 available in March-April 2024; exact snapshot not reported",
    "study_period": "late March to early April 2024",
    "assessed_as_of": "2026-11-02",
    "temporal_relevance": "historical-system",
    "review_due": "2027-05-02",
    "recency_note": "The assisted-versus-unaided measurement design transfers, but effect size and task feasibility require replication with current systems and a less selected analysis sample."
  },
  "access": "author-manuscript"
}
---

# S061 — Temporary upskilling of knowledge workers

## Why it matters

This preregistered workplace experiment shows an especially clear capability boundary: ChatGPT extended nontechnical consultants' assisted data-science performance, but the randomized groups did not differ on an immediate unaided technical-knowledge probe. The result is relevant to Orqestra's distinction between AI-assisted and accessible-independent capability.

## Identity and provenance

- Canonical identifier: DOI 10.1038/s41562-026-02566-6; OpenAlex W7223706382
- Version inspected: complete author-hosted working paper plus the 26 October 2026 *Nature Human Behaviour* landing page, final abstract, supplementary metadata and Crossmark status
- Content inspected: design, preregistration, recruitment, attrition, tasks, primary outcomes, unaided knowledge results, appendices and limitations in the author manuscript; final publication identity and abstract
- Version boundary: the final version of record is paywalled. The outcome used here is present in both the inspected author manuscript and final abstract, but final pagination and any unexposed textual changes were not verified.
- Access and rights: public author manuscript inspected for research; no full text committed; Atlas candidate `cand_5ad864ea82b933ce`
- Locator convention: working-paper sections 2.3 and 4.1–4.3; figure 3; table 1; appendix tables B1, B2, B7 and B14

## Study

- Population and setting: nontechnical consultants at Boston Consulting Group, all with at least bachelor's degrees; 986 registered workers were randomized and 487 submitted two assigned tasks for the main analysis.
- Intervention and comparator: 15–20 minutes of ChatGPT prompting training and GPT-4 access versus training in Google, Stack Overflow, Khan Academy and other ordinary web resources.
- Outcomes and timing: assisted performance on two of three 90-minute coding, statistical-understanding and prediction tasks; then five immediate technical questions completed without ChatGPT.
- Design: preregistered, individually randomized trial stratified by gender, location, role, coding skill, degree and prior ChatGPT-for-coding experience. Task pair and order were randomized.

## Findings

- Treatment improved assisted performance on all three technical tasks by 49, 20 and 17 percentage points relative to controls; neither arm reached the data-scientist benchmark on two of the three tasks.
- On five immediate technical questions without ChatGPT, the joint treatment test was null: `F(5,198)=0.83`, `p=.531`. Individual effects ranged from -7.7 to +4.8 percentage points; reported Bayes factors of .10, .18, .50, .13 and .62 ranged from moderate null evidence to weakly informative.
- The experiment therefore identifies an assisted capability gain without evidence of an immediate knowledge gain in the observed completer sample. It does not show knowledge loss or long-term deskilling.

## Limitations and boundary conditions

- Only 487 of 986 randomized workers completed both tasks, and question-specific unaided-outcome samples ranged from 151 to 323. Attrition counts and observed covariates were broadly balanced, but the knowledge result remains at high risk from missing outcome data.
- The paper's Lee-bound sensitivity checks protect the main assisted task results; they do not fully recover the missing post-experiment knowledge outcomes.
- Participants and analysts were not blinded. Technical questions followed immediately and sampled a small set of task-adjacent concepts.
- The highly educated consultant population, employer incentives, bespoke tasks and BCG/OpenAI involvement limit population and institutional transfer. Several authors were affiliated with BCG or OpenAI.
- GPT-4 from March–April 2024 is historical-system evidence. Current systems may change assisted performance, but a stronger model does not by itself establish learning.

## Evidence profile

| Dimension | Rating | Reason |
|---|---|---|
| Internal validity | low-moderate | Strong randomized and preregistered design, but roughly half the randomized sample and many question-level outcomes were missing |
| Directness | high | Separates assisted task performance from an unaided knowledge probe |
| Consistency | moderate | Aligns with several performance/learning dissociations, but the setting and outcome differ materially |
| Replication | low | One employer-based study |
| Magnitude | mixed | Large assisted gains; no credible immediate knowledge difference in the observed sample |
| Duration | low | The independent probe was immediate |
| Transfer | low-moderate | Technical questions were task-adjacent; authentic workplace performance beyond the experiment was not measured |
| Ecological validity | moderate | Real knowledge workers and realistic tools, but bespoke incentivized tasks in one firm |

## Candidate claims

Supports [C001](../../claims/C001-assisted-performance-is-not-learning.md) as a workplace assisted/unaided dissociation. It does not support a claim that AI caused learning loss.

## Notes

The most informative replication would retain every randomized participant for a delayed, novel unaided task and compare answer-ready access with transparent effort-preserving support.
