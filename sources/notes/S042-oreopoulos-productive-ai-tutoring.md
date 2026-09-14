---
{
  "id": "S042",
  "type": "source",
  "title": "Making AI Tutoring Productive: Evidence from a Mastery-Based Math Practice Experiment",
  "citation_key": "oreopoulos2026productive",
  "source_kind": "working-paper",
  "epistemic_roles": ["empirical-study"],
  "year": 2026,
  "url": "https://doi.org/10.3386/w35621",
  "status": "reviewed",
  "topics": ["ai-tutoring", "scaffolding", "feedback", "retrieval-and-spacing", "learning-vs-performance"],
  "added": "2026-09-14",
  "last_reviewed": "2026-09-14",
  "technology_dependence": "model-dependent",
  "technology_context": {
    "system": "NUMI guard-railed LLM tutor",
    "version": "not reported",
    "study_period": "23 March to 3 April 2026",
    "assessed_as_of": "2026-09-14",
    "temporal_relevance": "unknown",
    "review_due": "2026-12-14",
    "recency_note": "The field deployment is recent, but the model and snapshot are not reported. Treat the workflow evidence as current-context and the model-specific transfer to Orqestra as unresolved."
  },
  "access": "publisher-open"
}
---

# S042 — Making AI Tutoring Productive

## Why it matters

This large randomized field experiment tests a mastery rule, a guard-railed LLM tutor and their interaction in ordinary middle-school mathematics. It directly separates next-attempt recovery from a brief one-week assessment and shows that a platform-defined streak is not equivalent to delayed learning.

## Identity and provenance

- Canonical identifier: NBER Working Paper 35621; DOI `10.3386/w35621`; trial `AEARCTR-0018678`.
- Version inspected: August 2026 working paper, 72-page publisher PDF.
- Content inspected: complete PDF, including design, tables 1–9, implementation appendix, tutor prompts, robustness analyses and limitations.
- Access and rights: publisher-open NBER working-paper PDF; no full text is stored in Git.
- Retrieval: gateway candidate `cand_27108bd6986bc001`; PDF SHA-256 `c49eea71b7a24936f7cab34a231c0ddfa8e0bbc8a6727ef49e06401301730ca2`.
- Locator convention: numbered section and table in the August 2026 working paper.

## Study

- Population and setting: 6,997 grade 6–8 students who logged into NUMI across 20 Hamilton County, Tennessee schools and just under 100 teachers; about 90% took the assessment one week later.
- Intervention and comparator: individual 2 × 2 × 2 randomization to one of two topic bundles, AI or CAL-only support, and mastery or non-mastery progression. CAL-only supplied videos, practice, correctness feedback and worked solutions. The AI bundle added a first-step reasoning prompt, post-error walkthroughs and step explanations while withholding final answers.
- Mastery manipulation: three correct answers in a row before progression versus a learner choice to continue or move on after three attempts.
- Outcomes and timing: platform progression, practice accuracy and time, post-mistake recovery, and four unassisted assessment items approximately one week later covering practiced and unpracticed topic types.

## Findings

- Mastery raised the probability of three correct answers in a row on Exercise 1 by 28.7 percentage points and increased practice, but did not itself improve any delayed outcome (sections 4.3–4.4; table 5).
- Among mastery students who made an observed error, assignment to AI increased next-attempt correctness by 8.5 percentage points, reduced attempts to the next correct answer by 0.96, and increased elapsed time by 2.88 minutes (section 5.3; table 8). Because the analysis conditions on post-treatment mistakes, this is mechanism evidence rather than the primary causal learning estimate.
- Among mastery students, practiced Exercise 1 correctness one week later was 40.2% with AI versus 37.0% with CAL-only, a 3.2-point estimate with `p=.065`; the corresponding unpracticed item was essentially unchanged (section 5.5; table 9). The brief, noisy outcome and marginal precision support a signal, not a deployment claim.
- AI slowed progress and reduced exposure to later questions. The study therefore identifies a pace–quality trade-off rather than a uniformly superior workflow.
- No demographic subgroup interaction was statistically distinguishable. This does not establish equal impact because subgroup estimates were exploratory and often imprecise (appendix table A3).

## Limitations and boundary conditions

- The tutor is a bundle: first-step prompts, post-error walkthroughs, worked-solution review, guardrails and quality control are not independently randomized.
- The exact LLM and snapshot are not reported, blocking model-specific technology directness.
- The intervention is one class period and the delayed measure has only four items, one per exercise/topic cell.
- Treatment changes time and exposure; Exercise 2 comparisons are especially selected and difficult to interpret.
- The CAL comparator already supplies worked solutions, so the estimate is value added over structured software rather than over answer-first generic AI.
- The working paper is preregistered but not yet peer reviewed.

## Evidence profile

| Dimension | Rating | Reason |
|---|---|---|
| Internal validity | high | Individual factorial randomization and preregistration; mechanism analyses condition on treatment-affected mistakes |
| Directness | high | Tests structured post-error support and an unassisted one-week outcome in a real classroom workflow |
| Consistency | moderate | Aligns with structured-tutoring evidence, while strict withholding and mastery-only results are mixed |
| Replication | low | One working paper; components are not isolated |
| Magnitude | low-moderate | Large immediate recovery differences but only a 3.2-point marginal delayed signal |
| Duration | moderate-low | Approximately one week after a single session |
| Transfer | low | Novel items of practiced types; no far transfer |
| Ecological validity | high | Twenty schools, ordinary class periods and a large heterogeneous district sample |
| Technology directness | unclear | Recent deployment, but model/version is unreported |

## Candidate claims

Supports [C028](../../claims/C028-post-error-support-outpaces-delayed-evidence.md): structured AI can improve recovery after errors, but its delayed value is modest, bundled and time-costly. It does not isolate an attempt-before-answer rule or a progressive hint ladder.

## Notes

The study's most durable warning is measurement-related: forcing three correct answers in a row raised platform mastery without raising delayed learning. Orqestra should never treat a retry streak as durable capability without a later independent check.
