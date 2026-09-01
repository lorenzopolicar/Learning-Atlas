---
{
  "id": "E001",
  "type": "experiment",
  "title": "Low-stakes AI-mediated task stewardship probe",
  "status": "draft",
  "date": "2026-09-01",
  "topics": ["human-ai-collaboration", "assessment-validity", "metacognition", "product-measurement", "ethics-and-governance"],
  "tests_claims": ["C010", "C011"],
  "tests_beliefs": ["B004"],
  "tests_principles": ["P001", "P002", "P005", "P006"]
}
---

# E001 — Low-stakes AI-mediated task stewardship probe

**Implementation readiness:** contract-ready for learner/domain/accessibility co-design; not approved for product deployment. See the [implementation package](E001-ai-mediated-stewardship-probe/pilot-package.md), [event schema](E001-ai-mediated-stewardship-probe/event.schema.json), and synthetic [fixtures](E001-ai-mediated-stewardship-probe/fixtures/).

## Evidence rationale

[S024] provides fragile, same-session evidence that requiring early performance before AI access can outperform always-on access, so E001 uses a transparent self-first sequence as the main measurement baseline rather than beginning with an opaque adaptive policy [C011, P001]. It also randomizes order on matched tasks because eliciting an initial judgment may itself change the construct.

[S023] found a large supported programming advantage but an inconclusive absolute one-week retest contrast, while [S025] found high perceived helpfulness without improved unaided bedside performance. Neither validates stewardship as a construct. Together they strengthen the requirement to separate supported output, later accessible-independent performance, perceived usefulness and process evidence [C001, C012, P005].

## Hypotheses

Primary: on bounded tasks with defensible correctness and the same self-first measurement sequence, adding uncertainty/provenance cues and a brief justification prompt improves correct resistance to plausible AI errors without reducing correct adoption of useful advice.

Validity: a portfolio of initial/final decisions, confidence discrimination, verification, repair and escalation adds incremental prediction of delayed accessible-independent and near-transfer performance beyond domain accuracy and raw confidence alone.

## Context and participants

Use one low-stakes Orqestra learning domain whose task authors can define correct, incomplete and subtly incorrect advice without safety risk. Recruit learners voluntarily. Co-design support classifications, interaction burden, result explanations and contest paths with a varied learner advisory group that includes disabled learners.

Predeclare the target construct and a minimum sample/trial calculation before recruitment. Do not infer a stable person trait from the exploratory run.

## Intervention and comparator

Use matched task forms and preserve every learner's access-restoring support in all conditions.

- **Measurement control:** learner gives an initial answer and confidence, sees controlled advice without extra stewardship cues, and may revise the answer.
- **Stewardship scaffold:** learner follows the same sequence but receives provenance/uncertainty cues and gives a short acceptance, rejection, verification or escalation rationale.
- **Order-reactivity subset:** randomize self-first versus advice-first ordering on separate matched tasks to estimate how much the measurement procedure changes performance and later learning. Do not compute RAIR/RSR for advice-first trials.

Across repeated bounded trials, counterbalance correct, incomplete and plausible incorrect advice and error severity. Add one open-ended transfer task as a qualitative boundary check; do not compute RAIR/RSR for it unless a defensible scoring model exists.

## Primary outcomes and timing

- Report correct adoption (RAIR) and correct resistance (RSR) separately, with numerators, eligible denominators and uncertainty.
- Use severity-weighted detection and repair for consequential AI errors.
- Record verification actions, human/tool escalation, recovery, and unresolved uncertainty.
- Estimate confidence discrimination only when there are enough labelled correct and incorrect trials; do not substitute mean confidence.
- Measure accessible delayed independent performance after substantive AI generation is removed, plus near transfer, approximately one week later.
- Collect learner-reported autonomy, workload, accessibility, psychological safety and contestability.

Secondary analyses compare assisted gain, final output quality, time, and subgroup patterns. They must not convert descriptive disability or accommodation data into a learner score.

## Guardrails and ethics

- Formative, voluntary and low stakes; no ranking, credential, employment decision or silent mastery update.
- Never remove screen readers, transcription, alternative expression or other access-restoring support merely to create an “independent” condition.
- Warn participants that some advice may be imperfect; debrief every planted error and repair any misconception.
- Minimize retained text, hash or redact sensitive content, set expiry and permitted-use fields, and let learners inspect, correct and contest their record.
- Review error severity and exclusions with domain and accessibility experts before deployment.

## Analysis plan

Pre-register task exclusions, missing-data handling and the estimand for each outcome. Use hierarchical models or participant-level uncertainty appropriate to repeated trials. Model RAIR and RSR separately; inspect their trade-off rather than optimizing agreement. Compare the richer portfolio against baselines using domain accuracy alone and domain accuracy plus raw confidence.

Audit ordering effects, denominator stability, measurement invariance, differential burden and missingness. Treat post-hoc subgroup results as exploratory unless powered and predeclared.

## Falsification and stop rules

The operational approach should be rejected or narrowed if any of the following holds:

- the portfolio adds no useful prediction or decision quality beyond domain accuracy and raw confidence;
- self-first ordering materially changes the construct being inferred;
- RAIR/RSR denominators are too sparse or unstable at an acceptable task burden;
- the measures do not predict delayed accessible-independent or authentic outcomes;
- accessibility or invariance audits reveal construct-irrelevant group penalties;
- learners cannot understand, correct or contest the evidence;
- privacy, anxiety or interaction costs exceed the product value.

## Result and interpretation

Not run. This document is a falsifiable protocol draft, not evidence that AI-mediated task stewardship is a valid construct or teachable capability.
