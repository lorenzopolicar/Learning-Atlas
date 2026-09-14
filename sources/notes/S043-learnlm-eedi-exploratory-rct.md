---
{
  "id": "S043",
  "type": "source",
  "title": "AI tutoring can safely and effectively support students: An exploratory RCT in UK classrooms",
  "citation_key": "learnlm2025rct",
  "source_kind": "preprint",
  "epistemic_roles": ["empirical-study", "product-claim"],
  "year": 2025,
  "url": "https://arxiv.org/abs/2512.23633",
  "status": "reviewed",
  "topics": ["ai-tutoring", "scaffolding", "feedback", "transfer", "learning-vs-performance"],
  "added": "2026-09-14",
  "last_reviewed": "2026-09-14",
  "technology_dependence": "model-dependent",
  "technology_context": {
    "system": "LearnLM",
    "version": "most recent trial version fine-tuned from Gemini 2.0 Flash",
    "study_period": "13 May to 30 June 2025",
    "assessed_as_of": "2026-09-14",
    "temporal_relevance": "recent-system",
    "review_due": "2027-03-14",
    "recency_note": "The system is inside the rolling 18-month window but predates newer Gemini generations; every model message was supervised by a human tutor, limiting transfer to autonomous deployment."
  },
  "access": "publisher-open"
}
---

# S043 — LearnLM/Eedi exploratory RCT

## Why it matters

This trial compares a static hint with interactive tutoring after a learner's first wrong answer, then randomizes interactive sessions between a human tutor and a human-supervised pedagogical model. It is close to the progressive-assistance question, but every condition already required an attempt and the AI was not autonomous.

## Identity and provenance

- Canonical identifier: arXiv:2512.23633v1; title-page short link `goo.gle/LearnLM-Nov25`.
- Version inspected: 29 December 2025 preprint, 31-page publisher PDF.
- Content inspected: complete PDF, including design, figures 1–3, model description, exact prompt, statistical appendix, safety audit and tutor interviews.
- Access and rights: publisher-open arXiv PDF linked as CC BY 4.0; no full text is stored in Git.
- Retrieval: gateway candidate `cand_d2b1e128d78bbc89`; PDF SHA-256 `a0ee40ce7e3b52a75f8a36c665badfb738ae49593c604b60229e7ffa9de04d50`.
- Locator convention: page, figure, table and appendix in v1.

## Study

- Population and setting: 165 Year 9–10 students aged 13–15 across five UK secondary schools, using Eedi over seven weeks; 17 expert human tutors delivered or supervised interactive support.
- Intervention and comparator: students who answered a study unit's diagnostic item incorrectly were randomized to a static misconception-specific hint or interactive tutoring. Tutoring sessions were separately randomized to a human tutor or LearnLM with human review of every drafted message.
- Model and pedagogy: the trial used the then-current LearnLM fine-tuned from Gemini 2.0 Flash and instructed to use Socratic dialogue, guide learners to identify their mistake and avoid revealing the answer.
- Outcomes: correctness on the next attempt, resolution within two attempts on the same topic, and correctness on the first item in the next topic. These are immediate and near-transfer outcomes, not delayed independent assessments.

## Findings

- Estimated next-attempt correctness was 65.4% after a static hint, 91.2% after human tutoring and 93.0% after supervised LearnLM tutoring (figure 3; appendix table B1).
- Same-topic misconception resolution was 86.8%, 94.9% and 95.4%, respectively. Interactive tutoring outperformed static hints; LearnLM and human tutoring were not meaningfully separated on this measure.
- On the next topic's first item, adjusted success was 56.2% after a static hint, 60.7% after human tutoring and 66.2% after supervised LearnLM. The LearnLM–human difference was 5.5 points with a 95% interval from -1.4 to 12.4, so superiority over a human tutor is uncertain.
- Human supervisors changed 25.6% of model drafts. Pacing was the largest edit category, 44.3% of edits, commonly because continued Socratic questioning risked exasperating a learner (pages 5–6; appendix E).

## Limitations and boundary conditions

- All conditions followed an incorrect attempt, so the study cannot estimate attempt-before-help versus immediate help.
- Interactive tutoring bundles dialogue, personalization, time and relationship; it does not isolate hint granularity or escalation order.
- Human review of every message is both a safety strength and a major boundary for autonomous product use.
- The next-topic item is near transfer in the same platform, not delayed retention or external performance.
- Session-level crossover may have transferred lessons from model-supervised sessions into tutors' human-only sessions.
- The report is authored by the teams building LearnLM and Eedi and is a preprint; product incentives require explicit consideration.

## Evidence profile

| Dimension | Rating | Reason |
|---|---|---|
| Internal validity | moderate-high | Two-stage randomization and baseline adjustment; session crossover and intervention cancellation complicate estimates |
| Directness | high for post-error support | Direct static-hint comparison after a real error; no attempt-first or autonomous-AI contrast |
| Consistency | moderate | Supports interactive repair but documents a pacing boundary consistent with disengagement evidence |
| Replication | low | One product-team preprint |
| Magnitude | moderate | Large immediate remediation advantage; smaller and uncertain next-topic advantage over humans |
| Duration | low | Outcomes occur in the same or next platform unit |
| Transfer | moderate-low | A distinct next topic, but within one mathematics platform and no delay |
| Ecological validity | moderate-high | Seven-week deployment in five schools with real tutors and platform use |
| Technology directness | moderate | Recent model family, but human supervision and newer generations limit autonomous-product transfer |

## Candidate claims

Supports [C028](../../claims/C028-post-error-support-outpaces-delayed-evidence.md): interactive support after an error improves immediate repair more clearly than it establishes delayed independent learning. Its pacing edits also constrain [P001](../../principles/P001-progressive-assistance.md).

## Notes

The correct product inference is not that a model should withhold indefinitely. Human supervisors added value mainly by knowing when to stop asking questions, adjust tone, or let the learner move on.
