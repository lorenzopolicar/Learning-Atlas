# E001 implementation package

This package turns [E001](../E001-ai-mediated-stewardship-probe.md) into a reviewable research thin slice. It is intentionally not a production learner-profile design.

## Decision boundary

Implement E001 behind a research flag and in a dedicated pilot store. Do not add its fields to `CourseEnrollment`, reinterpret `AssessmentResult`, or derive a permanent person-level score. Promote nothing to a learner profile until the protocol's validity, accessibility, learner-understanding and decision-value gates pass.

## Pilot unit

Choose one low-stakes, bounded task family with:

- a versioned objective, task, form, rubric and controlled advice bank;
- defensible correct, incomplete and plausible-incorrect advice;
- pre-reviewed severity levels from 0 (no meaningful error) to 4 (potentially consequential misconception or action);
- at least two matched forms and a delayed near-transfer form;
- no safety-critical, credential, employment or disciplinary decision.

The recommended first candidate is suspicious-message triage because task authors can define evidence, escalation and common plausible errors. Domain and accessibility reviewers must still approve it.

## Conditions and sequence

Preserve each learner's access-restoring baseline in every condition.

1. **Measurement control:** self-first answer and confidence → controlled advice → final answer and confidence.
2. **Stewardship scaffold:** the same sequence plus provenance/uncertainty cues and a short acceptance, rejection, verification or escalation rationale.
3. **Order-reactivity subset:** advice-first on separately matched trials. Exclude these trials from RAIR/RSR and use them only to estimate procedure reactivity.
4. **Delayed outcome:** approximately seven days later, use a new near-transfer form with substantive generation unavailable while ordinary access support remains available.

Counterbalance advice state, severity, task form and condition. Keep access, briefing time and task exposure constant. Use authored advice for the first pilot so the experimental manipulation is versioned; live-model variability is a later study.

## Learner-facing review

The review surface must use observation language, not trait language:

> This record shows what happened on a small set of practice tasks. It does not establish your general mastery, intelligence, employability or a permanent ability to work with AI.

For every event, show the task and instrument versions, assistance lane, support classification and its basis, observed action, scored assertion and a **correct or contest this record** action. Show any derived inference separately with its evidence links, model version, uncertainty, review date and authorized use. A correction appends a new record that refers to the original; it never silently overwrites history.

After the last planted-error trial, debrief which advice was controlled, identify every planted error, explain the safer reasoning and offer misconception repair. Let a learner withdraw future use where the consent model permits it.

## Storage contract

[`event.schema.json`](event.schema.json) is JSON Schema draft 2020-12, version `0.2.0`; [`inference.schema.json`](inference.schema.json) is the separate versioned-inference contract. The fixtures demonstrate:

- an AI-assisted disagreement trial with provenance and pre/post judgments;
- a delayed accessible-independent outcome that retains a screen reader;
- an append-only learner-contested correction;
- a deliberately insufficient inference that links the events without rewriting them.

The observation contract distinguishes occurrence from recording time; tool permission, availability, declaration and observed use; learner-reported confidence from model uncertainty; and scoring assertions from raw responses. The inference contract separates model staleness review and use authorization from the event's retention deadline. The contracts deliberately store digests rather than response text by default. Any separately retained content needs its own purpose, encryption, access and deletion policy. `learnerRef` must be pilot-pseudonymous.

## Orqestra seam

The current product summary models are the wrong persistence seam:

| Current concept | Keep for | Do not use it to infer |
|---|---|---|
| `CourseEnrollment` pre/post score and learning gain | course completion and existing product summaries | assisted versus accessible-independent capability |
| `AssessmentResult` answer/correctness and Bloom/category aggregates | immediate assessment reporting | provenance, reliance, verification, recovery or durable learning |
| `maxBloomLevelAchieved` | explicitly coarse, non-gating descriptive roll-up | a stewardship trait or learner rank |

For the pilot, add separate append-only observation and scored-assertion records plus a versioned inference view or store. Index only the purpose-minimal fields needed for the pilot, including `tenantId`, `pilotId`, pseudonymous `learnerRef`, `eventId`, `eventType`, `occurredAt`, `recordedAt`, `evidenceLane`, `task.id`, and `governance.correctionOf`. Keep the identity lookup separately permissioned. Resolve correction chains without deleting originals.

## Delivery sequence

1. Co-design the support vocabulary, burden, review copy and contest flow with a varied learner advisory group that includes disabled learners.
2. Domain-review the task/rubric/advice bank and planted-error severity; pre-register exclusions, estimands, timing and minimum information thresholds.
3. Run schema fixtures through the implementation's chosen JSON Schema validator and keep the repository invariant tests green.
4. Instrument only the research-flag path and conduct an internal dry run with synthetic identities.
5. Conduct a small comprehension/usability pilot before collecting outcome evidence.
6. Run the powered pilot and publish both positive and null/negative results into the Atlas.
7. Decide whether to retire, revise or advance the construct using E001's stop rules.

Repository validation:

```bash
uvx check-jsonschema \
  --schemafile experiments/E001-ai-mediated-stewardship-probe/event.schema.json \
  experiments/E001-ai-mediated-stewardship-probe/fixtures/*.json
uvx check-jsonschema \
  --schemafile experiments/E001-ai-mediated-stewardship-probe/inference.schema.json \
  experiments/E001-ai-mediated-stewardship-probe/inference.fixture.json
python3 -m unittest tests.test_e001_contract -v
```

## Minimum analysis outputs

- assisted and delayed accessible-independent outcomes, never collapsed;
- RAIR and RSR separately, with eligible counts and uncertainty;
- severity-weighted error acceptance and repair;
- verification, escalation and unresolved-uncertainty events;
- order effects, missingness, interaction burden and subgroup/invariance diagnostics;
- incremental prediction over domain accuracy and domain accuracy plus raw confidence;
- contest rate, correction rate and learner comprehension of the record.

No analysis should produce a leaderboard, credential, employment signal, silent mastery update or diagnosis.

## Stop before implementation if

- a learner/domain/accessibility co-design group has not reviewed the task and event vocabulary;
- the product cannot preserve ordinary access supports across conditions;
- event visibility, correction, retention and prohibited-use enforcement are only policy text rather than testable behaviour;
- a controlled error could cause real-world harm or persist beyond debrief and repair;
- the team cannot separate pilot research data from operational learner scoring.
