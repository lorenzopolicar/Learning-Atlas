---
{
  "id": "S052",
  "type": "source",
  "title": "Improving Students' Long-Term Knowledge Retention Through Personalized Review",
  "citation_key": "lindsey2014review",
  "source_kind": "journal-article",
  "epistemic_roles": ["empirical-study"],
  "year": 2014,
  "url": "https://doi.org/10.1177/0956797613504302",
  "status": "reviewed",
  "topics": ["learner-modelling", "spacing", "retrieval-practice", "retention"],
  "added": "2026-10-11",
  "last_reviewed": "2026-10-11",
  "technology_dependence": "model-independent",
  "access": "author-manuscript"
}
---

# S052 — Personalized review over a semester

## Why it matters

This study directly compares a learner-by-item memory scheduler with a strong generic spaced schedule while holding review opportunities constant, then measures retention in two proctored exams. It tests whether personalization adds value beyond spacing itself.

## Identity and provenance

- Authors: Robert V. Lindsey, Jeff D. Shroyer, Harold Pashler and Michael C. Mozer.
- Publication: *Psychological Science*, 25(3), 639–647; DOI `10.1177/0956797613504302`.
- Version inspected: complete 30-page author manuscript dated 16 August 2013, including supplementary methods and analyses.
- Access and rights: lawful author manuscript; no full text is stored in Git.
- Retrieval: gateway candidate `cand_646289600c60178b`; PDF SHA-256 `54c06870d177afc25dcd3fad0ba052bb03cde1e6e979ff61606d3b20a0f58a22`.
- Locator convention: author-manuscript page, figure and supplement section.

## Study

- Population and setting: 179 eighth-grade learners in third-semester Spanish at one suburban US middle school.
- Design: within-student random assignment of one third of each chapter's items to each scheduler. Every scheduler received the same number of review trials and each item had equal opportunity for selection.
- Intervention: DASH, a Bayesian learner-by-item memory model, scheduled review using inferred ability, item difficulty and study history.
- Comparators: a transparent one-week generic spaced schedule and a massed current-chapter schedule.
- Outcomes: two proctored cumulative translation exams, one at semester end and one 28 days later, each covering a randomized half of the material without corrective feedback.

## Findings

- On the semester-end exam, personalized review exceeded generic spacing by 8.3 percentage points (d = 1.05) and massed review by 12.4 points (d = 1.38).
- On the exam 28 days later, personalized review exceeded generic spacing by 10.0 points (d = 0.88) and massed review by 16.5 points (d = 1.42).
- The result shows incremental value over a credible fixed spacing rule, not merely the familiar spacing advantage over massing.

## Limitations and boundary conditions

- The task was vocabulary and short-sentence translation in one school; transfer to complex skills is untested.
- Each learner experienced all three schedules, so cross-condition study habits or interference may have reduced independence among comparisons.
- Personalization altered both learner-item targeting and the temporal distribution of review, so their separate contributions are not identified.
- The system is historical and non-generative. Its relevance is mechanism-oriented, not evidence about current LLM quality.

## Evidence profile

| Dimension | Rating | Reason |
|---|---|---|
| Internal validity | moderate-high | Randomized within learner and time/opportunity matched; possible cross-condition contamination |
| Directness | high for personalized review | Direct model-based versus generic spaced and massed schedules |
| Consistency | moderate | Supports [S051] over a long horizon; short isolated adaptation is null in [S053] |
| Replication | low-moderate | One school, but aligned with broader spacing and adaptive-practice mechanisms |
| Magnitude | large | 8.3–10.0 percentage-point advantage over generic spacing |
| Duration | high | Semester-long intervention and 28-day follow-up |
| Transfer | low | Tested the practiced language items |
| Ecological validity | moderate-high | Embedded in a real course with proctored exams |

## Candidate claims

Supports [C033](../../claims/C033-personalized-sequencing-can-beat-fixed-practice.md): repeated learner-item evidence can improve long-term retention over a strong transparent schedule.
