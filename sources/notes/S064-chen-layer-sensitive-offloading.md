---
{
  "id": "S064",
  "type": "source",
  "title": "Layer-sensitive cognitive offloading in generative AI-assisted writing: supported performance and independent no-AI outcomes",
  "citation_key": "chen2026offloading",
  "source_kind": "quasi-experimental-study",
  "epistemic_roles": ["empirical-study"],
  "year": 2026,
  "url": "https://doi.org/10.3389/fpsyg.2026.1906199",
  "status": "reviewed",
  "topics": ["learning-vs-performance", "cognitive-offloading", "transfer", "scaffolding"],
  "added": "2026-11-15",
  "last_reviewed": "2026-11-15",
  "technology_dependence": "model-dependent",
  "technology_context": {
    "system": "OpenAI ChatGPT official browser interface",
    "version": "GPT-5.3",
    "study_period": "2026-03-02 to 2026-04-24; AI-supported tasks 2026-03-09 to 2026-04-17",
    "assessed_as_of": "2026-11-15",
    "temporal_relevance": "current-system",
    "review_due": "2027-05-15",
    "recency_note": "The study directly observes current-system assisted products and supervised no-AI near transfer, but its six-class quasi-experimental design makes the directional policy result fragile."
  },
  "access": "open"
}
---

# S064 — Layer-sensitive offloading in AI-assisted writing

## Why it matters

This study directly separates current-system supported writing from a supervised no-AI near-transfer task. The observed pattern favoured open collaboration while support was present and bundled bounded support plus reflection after removal, but only six intact classes prevent a strong causal or component claim.

## Identity and provenance

- Canonical identifiers: DOI `10.3389/fpsyg.2026.1906199`; OpenAlex `W7204495850`.
- Version inspected: 13-page published *Frontiers in Psychology* PDF, CC BY, dated 28 August 2026.
- Gateway provenance: staged candidate `cand_0b05d8ac25218326`; local lawful working copy SHA-256 `d57226bea371aee14c175c8e1e4df46d8f3f54891106bd20c0d2f7c2ba46706a`.
- Locators: design and conditions on pp. 3–4; measures and analysis on pp. 5–6; supported outcomes on p. 7; process analyses on pp. 7–9; independent outcomes in tables 10–11 on p. 10; limitations on p. 12.

## Study

- Population and setting: 180 Chinese L1 undergraduates in six intact English academic-writing classes at one university; 168 completed the prespecified records and Week 8 assessment.
- Design: quasi-experimental class allocation, two classes per condition and one class per instructor in each condition. Condition remained confounded with class, timetable and cohort.
- Conditions: no-AI writing; bounded AI support that prohibited ready-to-use substantive components and required a rationale for every AI-influenced change; and open AI collaboration for planning, drafting, argument development, revision and language polishing.
- Exposure: three intervention assignments using GPT-5.3. Open collaboration used more prompts, incorporated more AI text, generated less independent text and spent less active time drafting than bounded support.
- Outcome: a new same-course, same-genre English argument task in Week 8, immediately after the intervention. It was supervised for 60 minutes without GenAI, internet, previous writing, histories, notes, dictionaries or course materials.

## Findings

- Open collaboration had the highest aggregated observed supported-writing mean (`4.02/5`) versus bounded support (`3.83`) and no AI (`3.57`) (table 5).
- The class-clustered open-minus-bounded supported contrast was `+0.21`, 95% CI `[0.06, 0.36]`, exact wild-cluster `p=.064`; the observed ordering was stable, but inference was imprecise.
- On the Week 8 no-AI task, bounded support had the highest observed writing quality (`3.88`), higher-order thinking (`3.83`), argument depth (`3.86`) and independent revision quality (`3.88`) (table 10).
- Adjusted bounded-minus-open differences were `+0.27`, `+0.35`, `+0.42` and `+0.39`; exact wild-cluster p values ranged from `.050` to `.063` (table 11).
- Within the AI-exposed sample, deeper offloading and reduced self-generated text were associated with worse Week 8 higher-order thinking. These are associative decompositions, not causal mediation.

## Limitations and boundary conditions

- Six classes supply too little independent assignment information. The student count does not compensate for class-level confounding.
- Bounded support combined two interventions: delegation limits and compulsory reflection. Neither component was isolated.
- The no-AI assessment immediately followed the eight-week sequence. It is near transfer, not delayed, cross-genre or far transfer.
- AI-related topics could create demand characteristics and permit imperfect rater blinding.
- The offloading framework has initial structural, reliability and convergence evidence but no independent validation.
- Self-generated text and drafting time were reconstructed from available records rather than complete keystroke logging.
- One Chinese university and English L2 writing limit generalization; accessibility burden was not independently assessed.

## Evidence profile

| Dimension | Rating | Reason |
|---|---|---|
| Internal validity | low | Non-random class allocation, six clusters, bundled treatment and boundary-level exact inference |
| Directness | high | Separately observes supported products and a supervised no-AI new-topic writing task using a current system |
| Consistency | moderate-low | Fits a performance/learning divergence and configuration-sensitivity pattern but lacks independent replication |
| Replication | low | One course, institution and research team |
| Magnitude | unclear | Student-level differences are sizeable, but cluster-level uncertainty is fragile |
| Duration | low | Eight-week exposure but no delayed outcome after instruction ended |
| Transfer | moderate | New topic in the same course and genre; no cross-genre or delayed transfer |
| Ecological validity | moderate-high | Authentic classroom writing cycles with complete interaction histories |

## Candidate claims

Supports the measurement boundary in [C001](../../claims/C001-assisted-performance-is-not-learning.md) and the provisional configuration-sensitivity claim in [C002](../../claims/C002-pedagogical-structure-changes-ai-learning-outcomes.md). It does not establish that open AI harmed learning, that bounded support caused the observed advantage, or that reflection, delegation limits or reduced offloading was the active mechanism.

## Notes

A decisive test would randomize learners or many classes to independently varied delegation limits and reflection, match practice time, preserve access supports, and measure novel no-AI writing immediately and after one and four to six weeks.
