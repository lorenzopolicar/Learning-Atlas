# R001 provisional risk-of-bias appraisal

Appraisal date: 2026-11-02

Scope: one prespecified learning-relevant result per included comparative study

Status: integrating-agent pilot; not an independent duplicate appraisal

## Method

Randomized parallel trials use the current RoB 2 framework; cluster and crossover designs use the corresponding RoB 2 variants and design-specific considerations. Non-randomized intervention studies use the November 2025 draft ROBINS-I V2. Judgements concern the named result, not the paper as a whole, and do not combine directness, imprecision, technology age or external validity with bias.

This first pass is intentionally conservative. `High` and `serious` results can still be informative, but they cannot carry a mature causal synthesis. A second reviewer should independently answer the official signalling questions and resolve disagreements before meta-analysis, claim promotion or review completion.

## Result-level judgements

| Source | Result and estimand | Design/tool | Overall judgement | Main reasons |
|---|---|---|---|---|
| [S001](../../sources/notes/S001-bastani-generative-ai-guardrails.md) | Effect of classroom assignment on the immediate unassisted mathematics exam | Cluster RoB 2 | some concerns | Preregistered classroom allocation, ITT analysis, independent rubric-based grading, no differential attendance attrition and clustered inference; stochastic arm assignment and concealment are not explicit enough to close domain 1 |
| [S002](../../sources/notes/S002-kestin-ai-tutoring-rct.md) | Effect of assigned lesson format on immediate post-lesson physics knowledge | Cluster/crossover RoB 2 | high | 194 of 233 enrolled learners were retained only after consent, both-condition participation and all pre/post tests; sequence and period handling are incompletely reported, and no preregistered outcome/analysis plan was located |
| [S005](../../sources/notes/S005-world-bank-nigeria-chatbot-rct.md) | Effect of programme assignment on the endline combined assessment | RoB 2 | some concerns | Individual randomization and ITT with Lee bounds/IPW support robustness, but attrition differed by arm, control contamination occurred and no preregistration was located |
| [S015](../../sources/notes/S015-contractor-reyes-experimental-evidence.md) | Effect of AI access assignment on the one-week unaided knowledge test | RoB 2 | some concerns | Randomization, strong first stage and low loss to follow-up; treatment/control rule violations, protocol variation and no located preregistered analysis plan leave residual concern |
| [S023](../../sources/notes/S023-gardella-fast-and-forgettable.md) | Effect of prior Copilot versus human-peer condition on one-week absolute individual retest | ROBINS-I V2 | moderate | Small self-selected sample and partner/task/order effects remain, but within-person rotation of all eight permutations and complete follow-up reduce confounding and missing-data risk. The absolute contrast is also very imprecise, which is not itself bias |
| [S024](../../sources/notes/S024-rotter-access-timing.md) | Effect of assigned access-timing policy on the immediate unassisted test | ROBINS-I V2 | serious | Workshop-level non-random assignment, baseline imbalance, post-assignment zero-score exclusions and unmodelled session clustering materially threaten the causal contrast |
| [S025](../../sources/notes/S025-saloojee-ai-at-bedside.md) | Effect of ChatGPT permission on blinded immediate bedside performance | RoB 2 | some concerns | Registered individual randomization, blinded assessors and ITT; post-allocation withdrawal and high uncalibrated assessor variance remain. The underreported later summative result is separately `high` and should not support a durable null |
| [S060](../../sources/notes/S060-barcaui-cognitive-crutch.md) | Effect of unrestricted ChatGPT study assignment on 45-day retention | RoB 2 | high | 35 of 120 randomized learners lacked the outcome, comparator AI non-use was unmonitored and no preregistration was located; objective scoring and balanced completer counts do not remove missing-outcome uncertainty |
| [S061](../../sources/notes/S061-wiles-temporary-upskilling.md) | Effect of ChatGPT assignment on immediate unaided technical knowledge | RoB 2 | high | Only 487 of 986 allocated workers completed both tasks and question-level samples fell to 151–323; preregistration and stratified randomization protect selection of results but not the missing outcome data |

## Consequence for the synthesis

The measurement claim in [C001] survives: assisted success cannot establish independent learning. The effect claim in [C002] remains provisional because most positive and negative contrasts bundle access, interaction policy, exposure, teacher role, interface and incentives. [C036] is kept narrow and low confidence despite its 45-day horizon.

No pooled effect is warranted. Even the strongest direct performance/learning contrast [S001] retains some concerns for its allocation domain. Several randomized results have material concerns; the non-randomized studies are moderate [S023] and serious [S024] risk. Technology-current evidence added in the open PR stack is complementary but does not repair these design limitations on this independent branch.

## Required adjudication

1. Duplicate the official signalling-question assessments independently.
2. Obtain allocation, missingness and analysis-plan details from authors where reports are insufficient.
3. Keep the estimand as assignment to the policy; do not reinterpret post-treatment usage groups as randomized mechanisms.
4. Re-run the appraisal when current-system delayed novel-transfer trials become available.

## Independent disagreements and integrating judgements

- **S001 domain 1:** the initial integrating draft was low risk; the evidence analyst required explicit confirmation that the integer-program assignment contained a stochastic element and that allocation was concealed. The final integrating judgement adopts `some concerns`.
- **S023 overall:** the initial integrating draft was serious; the evidence analyst judged moderate because the within-person design rotated all eight task/order/condition permutations and had complete follow-up. The final judgement adopts `moderate`, keeping small-sample imprecision separate from bias.

The disagreement history remains auditable. A formal duplicate signalling-question adjudication may still revise the final pilot labels.
