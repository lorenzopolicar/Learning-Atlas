# R001 provisional risk-of-bias update

Appraisal date: 2026-11-09

Scope: the admitted S062 outcomes and a correction to the held Bassner package. This is an integrating-agent appraisal, not duplicate human adjudication.

## S062 result-level judgements

| Result | Tool | Judgement | Reason |
|---|---|---|---|
| Assignment to AI tutoring versus standard remediation on next-unit near transfer | RoB 2 | some concerns | Student-level within-class randomization, preregistration and recorded outcome are strengths; concealment details are limited in the developer report, all messages were human reviewed, and model routing changed during treatment |
| Assignment on a returning diagnostic question after more than seven days | RoB 2 | high | The analysis is explicitly exploratory, repeated-item availability is produced by platform activity, and no missingness or selection analysis for this outcome was reported |
| Assignment on endline Star Maths | RoB 2 | some concerns | Preregistered analysis and external administration/scoring are strengths; attrition handling and allocation concealment are not reported in enough detail here for low risk |

These judgements concern bias, not directness. The Star outcome is broader but not delayed after intervention withdrawal; the returning question is delayed but not novel.

## Held Bassner correction

Zenodo package v5 supersedes the v4 package inspected in the prior draft-PR stack. It changes analytic `N` from 275 to 283, corrects 48 exercise scores that used later submissions, and restores an accidentally excluded programming-experience category. Both AI arms still outperform no AI on the assisted exercise, while ChatGPT versus the IRIS scaffold is now nonsignificant (`p=.167`, `d=.27`). Immediate six-item knowledge gain still has no time-by-group interaction (`F(2,280)=.260`, `p=.771`).

Keep the source held and provisionally high risk: 37.4% of randomized participants were excluded, filtering differed by treatment, no preregistration was located, exact model snapshots are missing, and the accessible package does not establish the post-test assistance state. The version of record and corrigendum must be reconciled before admission.

## Integrating judgement

The evidence supports a high-confidence measurement boundary but not a high-confidence directional harm claim. Positive counterexamples make unrestricted, explicit-request and attempt-first policies competing hypotheses. A decisive trial must match instruction, practice opportunity, time and interface transition; preserve access-restoring accommodations; and assess novel independent performance immediately, at one week, and at four to six weeks.
