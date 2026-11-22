---
{
  "id": "D002",
  "type": "decision",
  "title": "Pilot task-level AI-mediated stewardship without a composite score",
  "status": "active",
  "date": "2026-08-31",
  "topics": ["human-ai-collaboration", "assessment-validity", "learner-modelling", "product-measurement", "ethics-and-governance"],
  "principles": ["P002", "P005", "P006"],
  "related_claims": ["C007", "C008", "C010", "C039", "C040"],
  "supersedes": []
}
---

# D002 — Pilot task-level AI-mediated stewardship without a composite score

## Context

Orqestra needs a way to reason about capability when learners use AI. The phrase “capability sovereignty” is attractive but not a validated learner construct; it combines appropriate reliance, metacognition, agency, authorship, resilience, meaningful human control, justice and contestability [N001]. Current Orqestra summaries do not preserve the observation context needed to separate these inferences.

## Decision

Use **capability sovereignty** only as a normative design lens. Use **AI-mediated task stewardship** as the provisional operational language for observable task evidence.

Run [E001] before adding a durable learner-model field. The pilot will keep accessible independent, AI-assisted and supervisory/recovery evidence separate; record assistance function; and expose a reviewable evidence portfolio. It will not create a `capabilitySovereigntyScore`, overload Bloom taxonomy, update a high-stakes mastery estimate, or infer dependence from tool presence or frequency.

The full design brief is [Orqestra design brief — AI-mediated task stewardship](../bridges/orqestra-ai-mediated-stewardship.md).

## Evidence and principles

- Final outcomes alone hide the distinction between correct adoption and correct resistance [C010].
- Capability estimates must retain provenance, context, uncertainty and permitted use [C007, P002].
- Trustworthy judgments require multiple construct-relevant channels [C008, P006].
- Learning claims require delayed performance after substantive assistance is removed, while necessary access support remains [P005].
- Disabled learners report both meaningful access/autonomy benefits and overreliance concerns, so assistance function is indispensable [S022].
- Assistance function is itself an assertion: authentic GenAI-log categories showed moderate average rater agreement and selective missingness [S065, C039].
- A model can look calibrated overall while producing materially different decision reliability by evidence stage and learner group [S066, C040].
- The ledger must earn its collection cost through a defined purpose, minimum necessary fields, learner access/correction, and bounded retention [S067].

## Alternatives considered

- **One capability-sovereignty score:** simple to display but lacks construct validity, hides trade-offs, invites ranking and turns a normative relationship into a person trait.
- **Tool-use disclosure only:** cannot distinguish access restoration, harmless representation and substantive delegation.
- **Artifact quality plus Bloom level:** readily available but cannot establish assistance state, judgment, recovery, delayed learning or supervisory behaviour.
- **No independent evidence:** authentic for some work but inadequate where learners must verify, recover during failure, or acquire foundational understanding.
- **No-tool assessment for everyone:** easy to administer but can remove accessibility support and introduce irrelevant variance.

## Consequences and revisit trigger

The pilot adds task and telemetry burden, must be co-designed, and cannot support high-stakes claims. Revisit the decision after [E001], especially if assistance classifications cannot be reproduced or understood, records are selectively missing, measures fail to add decision value, collection changes participation, creates inequitable burden, is highly reactive to ordering, or does not predict delayed or authentic outcomes. A future composite should be considered only after a public construct model, independent validation, subgroup and threshold calibration, fairness evidence and a legitimate decision use exist.
