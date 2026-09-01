# Orqestra design brief — AI-mediated task stewardship

**Status:** evidence-backed proposal for product discovery and a low-stakes pilot, not an implementation instruction or validated learner score

**Atlas basis:** [C001], [C002], [C007], [C008], [C010], [C011], [C012], [B004], [P001], [P002], [P005], [P006], [N001], [D002], [E001]

**Repository snapshot inspected:** `/Users/lorenzo.policar/Developer/emtech-noema`, branch `learning-upgrade`, 1 September 2026. The checkout had substantial user-owned changes; both inspections were read-only.

**Implementation package:** [E001 pilot package](../experiments/E001-ai-mediated-stewardship-probe/pilot-package.md), JSON Schema `0.1.0`, synthetic fixtures and invariant tests.

## Product decision in one sentence

Orqestra should represent **AI-mediated task stewardship** as transparent, task-level evidence alongside accessible independent domain capability—not as a `capabilitySovereigntyScore`, a Bloom level, or a hidden trait inferred from tool use.

## Why this matters

A learner may produce the same final answer through very different processes: independent knowledge, correct uptake of AI advice, uncritical acceptance of an error, careful verification, or access-restoring support. Final output quality collapses these states [C008, C010]. Conversely, a no-tool condition may remove a screen reader, transcription, alternative expression, pain-reducing support or executive support and introduce construct-irrelevant difficulty [S022].

The product therefore needs two distinctions:

1. **Evidence lane:** accessible independent, declared AI-assisted, or supervisory/recovery performance.
2. **Assistance function:** access restoration, representation, expression, executive support, substantive cognitive delegation, or mixed.

These are descriptions of an observation, not moral rankings. The intended construct and decision stakes determine what each observation can support.

## Current-system gap

The current Noema schema contains useful course and assessment summaries but cannot support this validity argument:

- `CourseEnrollment` records course version, pre/post scores, attempts, learning gain and a maximum Bloom level.
- `AssessmentResult` records slide index/type/attempt, total and maximum score, pass state, category and Bloom summaries, and answers.
- The current scoring path can return 100 when a course contains no genuinely scored slides after auto-completed slides are excluded.
- `deriveMaxBloomLevelAchieved` is explicitly documented as coarse, noisy, ceiling-confounded and non-monotonic.
- Work-profile extraction describes completion as “verified learning” and uses maximum Bloom and immediate gain as quality evidence.

Those fields do not preserve objective/task/form versions, initial judgment, advice state, assistance function, AI provenance, confidence, verification, disagreement, recovery, accessibility conditions, permitted inference, or model version. They should not be stretched into a stewardship measure. Existing summaries can remain product metrics while a future evidence ledger is evaluated separately.

The inspected implementation seams were `packages/noema-db/src/schema.ts`, `apps/noema/lib/learn/assessment-scoring.ts`, and `apps/noema/lib/actions/learn/assessment-actions.ts`. E001 should not modify them during construct discovery. Use a research-flagged, append-only store with separately permissioned identity mapping; promote only after the delivery gates below pass.

## Proposed evidence contract

Create append-only observations with corrections rather than mutating a learner trait. The names below are conceptual; implementation should follow Noema conventions after a separate architecture review.

| Field group | Minimum content | Why |
|---|---|---|
| identity and version | event ID, learner/pseudonymous actor, objective ID/version, task/form ID/version, timestamp | prevents evidence from floating free of the construct and instrument |
| intended inference | target capability, stakes, purpose, permitted uses, expiry/retention | constrains downstream claims [C007, P002] |
| evidence lane | `accessible-independent`, `ai-assisted`, `supervisory-recovery` | prevents assisted output from silently becoming independent mastery [B004] |
| assistance envelope | tools allowed/used, assistance function, accessible baseline, substantive-generation state | distinguishes access restoration from delegation [S022] |
| system provenance | provider/model/version, prompt or advice version, retrieval/source provenance, known uncertainty | makes changing AI conditions interpretable |
| pre-advice state | initial response or decision, confidence, rationale when proportionate | enables two-sided reliance measures [C010] |
| intervention | advice content/hash, correctness or rubric state where defensible, ordering, explanation/provenance cues | records what the learner actually encountered |
| post-advice state | final response, confidence, rationale, accepted/rejected/edited elements | distinguishes outcome and decision process |
| stewardship actions | verification, source checks, repair, tool switching, human escalation, uncertainty escalation, contest action | captures responsible recovery beyond solitary completion |
| outcome and delay | correctness/rubric with severity, immediate result, delayed accessible independent result, transfer distance | separates performance from learning [P005] |
| inference record | model/version, estimate, uncertainty, boundary, evidence links, correction/supersession | keeps inference separate and revisable [P002] |

Do not record a disability diagnosis merely to classify an assistance function. Let learners retain ordinary access supports, declare what support did in context, and review or contest classifications.

## Derived views, not permanent person scores

For a sufficiently repeated, objectively scored task family, a review surface may derive:

- accessible independent accuracy and delayed transfer;
- assisted gain or loss relative to the relevant baseline;
- correct adoption of correct AI advice and correct resistance to incorrect advice, each with denominator and uncertainty [C010];
- overreliance and underreliance cases, separated by error severity;
- confidence discrimination (for example AUROC2) only with enough labelled trials [S021];
- verification, repair and escalation patterns;
- coverage gaps and evidence expiry.

Every view should expose the supporting events and say what it cannot establish. Do not rank learners, issue credentials, trigger employment action, or update an overall mastery score from the pilot.

## First thin slice

Implement [E001] as research instrumentation before a durable profile:

1. Select one low-stakes, bounded domain where correct and subtly incorrect advice can be authored safely.
2. Co-design task wording, support categories and burden checks with learners, including disabled learners.
3. Preserve access-restoring support in every condition. Vary substantive AI advice, not accessibility.
4. Record an initial judgment before controlled advice for the measurement condition, while randomizing order in a subset to estimate measurement reactivity.
5. Add delayed accessible-independent and near-transfer tasks.
6. Return evidence to the learner as a reviewable portfolio, not a label.

The executable contract and delivery sequence now live in the [E001 implementation package](../experiments/E001-ai-mediated-stewardship-probe/pilot-package.md). Its fixtures make three validity requirements concrete: ordinary access support remains present in a delayed independent lane; substantive generation and its provenance are explicit in the assisted lane; and a learner contest creates a correction event rather than overwriting the observation.

## Delivery gates

Proceed from research pilot to product capability only if:

- the measures add decision value beyond domain accuracy and raw confidence;
- results predict a declared delayed or authentic outcome;
- ordering effects and trial burden are acceptable;
- accessibility and measurement-invariance audits do not reveal systematic construct-irrelevant penalties;
- learners can understand and successfully contest the record;
- the marginal value justifies privacy and implementation cost.

If these gates fail, retain the conceptual distinction between evidence lanes and assistance functions but do not persist a stewardship inference.

## Open design questions

- How should stewardship be evaluated when truth is plural, delayed or normative?
- How much domain knowledge is necessary for reliable oversight, and does that threshold transfer?
- Which recovery obligations belong to the learner, the product or the institution?
- Does eliciting confidence create accessibility, anxiety or anchoring burdens?
- Can compact authentic traces predict the same outcomes as repeated artificial disagreement trials?
- Which product decisions, if any, are legitimate uses of this evidence?
