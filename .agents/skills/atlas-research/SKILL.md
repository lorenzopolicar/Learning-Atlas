---
name: atlas-research
description: Research and advance one Learning Atlas question end-to-end. Use for weekly scouting, adding or appraising sources, updating an active review, finding counterevidence, or producing a research briefing. Enforces primary-source verification, a three-source admission cap for autonomous runs, typed evidence artifacts, validation, and a human publication gate.
---

# Atlas research

Advance one question without turning the atlas into an indiscriminate link collection.

## Load

Read these completely before acting:

1. `AGENTS.md`
2. `ontology/epistemic-policy.md`
3. `.harness/runbooks/research-cycle.md`
4. `.harness/runbooks/source-intake.md`
5. `.harness/specs/research-scout.md`
6. `research/queue.md`
7. `.harness/state/research-state.json`

Then query the repository for the selected question. Do not load every artifact.

## Run

1. Select one unblocked queue item and state the existing evidence gap.
2. Search authoritative scholarly sources, favoring primary studies, systematic reviews, corrections, replications, nulls, and contrary findings.
3. Inspect the actual source. An abstract may screen relevance but is insufficient for a promoted claim.
4. Admit no more than three new sources in an autonomous run. Create source notes and bibliographic entries with verified metadata.
5. Update screening/extraction records if the question belongs to an active review.
6. Create or revise atomic claims. Preserve boundaries, contradicting evidence, and source type.
7. Write a dated weekly briefing and update research state.
8. Run the required checks in `AGENTS.md`.
9. Show the human the claim-level change and open a draft pull request when repository credentials and the task authorize it. Never merge it.

## Quality bar

- A negative result, corrected metadata record, or narrower boundary is valid progress.
- Never infer causality from engagement or supported output quality.
- Never commit copyrighted full text or identifiable learner data.
- Stop at `seed` when methods or outcomes remain inaccessible.
