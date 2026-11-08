---
{
  "id": "S062",
  "type": "source",
  "title": "Measuring the impact of AI tutoring, from near transfer to standardised tests: An expanded RCT in UK mathematics classrooms",
  "citation_key": "learnlm2026expanded",
  "source_kind": "randomized-controlled-trial",
  "epistemic_roles": ["empirical-study"],
  "year": 2026,
  "url": "https://services.google.com/fh/files/misc/learnlm_oct26.pdf",
  "status": "reviewed",
  "topics": ["ai-tutoring", "learning-vs-performance", "transfer", "scaffolding"],
  "added": "2026-11-09",
  "last_reviewed": "2026-11-09",
  "technology_dependence": "model-dependent",
  "technology_context": {
    "system": "Eedi tutor using Gemini models with expert review",
    "version": "Gemini 3.1 Pro, Gemini 3 Flash, then Gemini 3.5 Flash",
    "study_period": "2026-04-13 to 2026-07-07, after a preparatory test beginning 2026-03-23",
    "assessed_as_of": "2026-11-09",
    "temporal_relevance": "current-system",
    "review_due": "2027-02-09",
    "recency_note": "The trial used current Gemini generations, but model rotation and mandatory human review prevent attribution to one stable model endpoint."
  },
  "access": "open"
}
---

# S062 — Expanded Eedi AI-tutoring RCT

## Why it matters

This preregistered classroom RCT traces one current-system intervention from immediate near transfer through a repeated-item delay and a broad standardized assessment. The positive proximal and null broad outcomes constrain claims that short-horizon tutoring gains necessarily accumulate into general attainment.

## Identity and provenance

- Canonical identity: LearnLM Team, Google and Eedi technical report, 29 October 2026; AEA RCT Registry `AEARCTR-0018079`, DOI `10.1257/rct.18079-1.1`.
- Version inspected: 22-page publisher PDF created 29 October 2026; SHA-256 `c0aa30c31f65c99cab4f0368d5b68cd51ded93f857f56e533c084ab27207aa7f`.
- Gateway provenance: candidate `cand_3e523124aab35f7c`; the registry was separately resolved as `cand_e75ac81eeb1e9c8f`.
- Locators: trial and assistance state on pp. 2–5; proximal and delayed outcomes on pp. 7–8; broad outcome on pp. 8–9; dates and model routing on pp. 15–16.

## Study

- Population and setting: 1,179 students aged roughly 12–15 in 58 classes across 10 UK state-funded secondary schools already using Eedi.
- Design: student-level four-arm randomization for seven to ten instructional weeks within a 12-calendar-week window. The report states that the design, hypotheses and analysis plan were preregistered.
- Conditions: standard Eedi remediation; expert human tutoring; Gemini tutoring with question context; and Gemini tutoring with additional learning-history context.
- Intervention fidelity: an expert tutor had to approve, regenerate or rewrite every AI draft before delivery. Tutors approved 94.7% of 94,385 reviewed drafts unchanged.
- Technology: routing changed from Gemini 3.1 Pro to Gemini 3 Flash on 21 April, then to Gemini 3.5 Flash on 21 May. A bug prevented prior-chat summaries from reaching the personalized condition.
- Outcomes: every named learning outcome was completed without concurrent AI or tutor help. Outcomes included immediate mistake correction, next-unit near transfer, an eight-question midtrial curriculum quiz, returning diagnostic questions after more than seven days, and externally administered Star Maths at baseline and endline.

## Findings

- Next-unit near-transfer accuracy was 58.4% and 58.3% in the two AI arms versus 50.5% under standard remediation; each directional posterior probability exceeded 99.9% (p. 7).
- On an exploratory return of the same diagnostic question after more than seven days, accuracy was 59.9% and 59.0% versus 47.6%; this is delayed retention of a repeated item, not delayed novel transfer (pp. 7–8).
- The midtrial curriculum quiz showed a small positive signal, strongest for personalized-context tutoring: 63.5% versus 59.6%, with 97.1% posterior probability of an advantage. The other tutor contrasts were weaker (p. 8).
- The preregistered broad Star Maths contrast was null: question-context AI was `-0.01 SD` with 95% credible interval `[-0.15, +0.14]`, and personalized-context AI was `+0.02 SD [-0.12, +0.16]` relative to standard remediation (pp. 8–9).
- Tutored learners covered fewer study units and constructs than standard-remediation learners. This plausible time/coverage explanation was exploratory and does not identify a causal mechanism for the broad null.

## Limitations and boundary conditions

- Google and Eedi developed and evaluated the intervention; the technical report is not peer reviewed and no independent replication was located.
- The model changed twice during treatment, human supervisors reviewed every draft, and an implementation bug weakened the intended personalization contrast.
- Standard remediation was a strong active comparator, not no instruction. All arms could request live help except while answering the second diagnostic question.
- The delayed measure repeats an earlier diagnostic item. Near transfer occurs at the next unit, and the broad test occurs at endline rather than after a post-intervention withdrawal delay. The trial therefore does not close the delayed novel-transfer gap.
- The report uses Bayesian directional probabilities. The Atlas preserves the reported estimands and does not translate them into frequentist significance claims.

## Evidence profile

| Dimension | Rating | Reason |
|---|---|---|
| Internal validity | moderate | Preregistered within-class randomization and independently scored broad outcome; developer report, exploratory delayed analysis, model rotation and incomplete implementation lower confidence |
| Directness | high | Separates unaided proximal, delayed repeated-item and broad outcomes for an AI-tutoring policy |
| Consistency | moderate | Positive proximal and null broad outcomes fit the wider heterogeneous record without resolving its moderators |
| Replication | low | One developer-led implementation with no independent replication located |
| Magnitude | outcome-specific | Clear proximal differences; small intermediate signal; broad effects centered near zero |
| Duration | low-moderate | Seven to ten instructional weeks; only the repeated-item outcome explicitly exceeds seven days |
| Transfer | moderate | Includes next-unit and broad standardized measures, but no delayed novel post-withdrawal endpoint |
| Ecological validity | high | Authentic weekly mathematics lessons across 10 schools using an established platform |

## Candidate claims

Supports [C037](../../claims/C037-current-ai-tutoring-improved-proximal-outcomes.md) and [C038](../../claims/C038-proximal-ai-tutoring-gains-did-not-improve-broad-attainment.md). It also strengthens the measurement boundaries in [C001](../../claims/C001-assisted-performance-is-not-learning.md) and the provisional, bundled-policy evidence in [C002](../../claims/C002-pedagogical-structure-changes-ai-learning-outcomes.md).

## Notes

The decisive next study would keep model and supervision provenance stable, match instructional time and coverage, and measure novel independent tasks immediately and after one and four to six weeks without withdrawing access-restoring support.
