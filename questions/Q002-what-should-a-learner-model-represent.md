---
{
  "id": "Q002",
  "type": "question",
  "title": "What should a trustworthy learner model represent?",
  "question": "Which representation of capability, evidence, uncertainty, assistance, time, and context best supports useful learning decisions without creating false precision or unacceptable surveillance?",
  "status": "open",
  "priority": "high",
  "topics": ["learner-modelling", "assessment-validity", "ethics-and-governance"],
  "related_claims": ["C007", "C008", "C013"],
  "last_reviewed": "2026-09-06"
}
---

# Q002 — What should a trustworthy learner model represent?

## Why this matters

The learner model is a candidate core asset for the Orqestra learning engine, but it can also become a scalable source of invalid inference and surveillance.

## Scope and definitions

Compare knowledge tracing, cognitive diagnosis, competency/evidence models, longitudinal portfolios, self-regulation and motivation models, and human-AI capability representations. Evaluate validity, calibration, contestability, usefulness, equity, privacy, and cost.

## What would answer it

An architectural synthesis plus product experiments comparing transparent baselines with increasingly complex models on actual intervention and decision quality.

## Current synthesis

The first architecture pass supports separate observation, scored-observable and learner-state-inference records [S026, P002]. Observation events should retain purpose-minimal task, assistance and provenance context [S028]. Self-reported confidence is an observation with scale provenance; model uncertainty belongs to the inference. Retention, authorized use and inference review are separate clocks, and elapsed time should affect an estimate only through a validated policy [C013].

## Next search

Test the proposed boundary against current xAPI 2.0 and learner-model calibration work, then co-design assistance and contestability semantics with learners. Seek evidence on classification reliability, privacy burden, missingness, and whether the richer ledger improves decisions over a purpose-minimal no-history baseline.
