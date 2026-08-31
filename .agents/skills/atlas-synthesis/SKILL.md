---
name: atlas-synthesis
description: Synthesize recent Learning Atlas evidence into claim, belief, and design-principle revisions. Use for monthly synthesis, contradiction review, confidence changes, product implications, research portfolio review, or a state-of-the-atlas briefing. Keeps empirical evidence, normative judgment, and product advice separate and requires falsifiers and human review.
---

# Atlas synthesis

Turn accumulated evidence into explicit judgment while preserving uncertainty and disagreement.

## Load

Read:

1. `AGENTS.md`
2. `ontology/epistemic-policy.md`
3. `.harness/runbooks/synthesis.md`
4. `.harness/specs/synthesis-editor.md`
5. `.harness/state/research-state.json`
6. the Git diff since `last_monthly_synthesis`

Use `python3 scripts/atlas.py query` to retrieve the affected claims, beliefs, and principles. Open source notes and originals only where the synthesis turns on their details.

## Run

1. Summarize material claim-level changes, including nulls and contradictions.
2. Compare evidence profiles and explain heterogeneity rather than counting papers.
3. Steel-man the strongest counterposition.
4. Propose the smallest justified belief or principle change: wording, scope, confidence, status, or no change.
5. Ensure every adopted belief has counterarguments and revision criteria and every active principle has exceptions and falsifiers.
6. Identify affected Orqestra questions and experiments without editing that repository automatically.
7. Write a dated synthesis briefing, update state, regenerate views, validate, and test.
8. Open a draft pull request when authorized. Human review is required for maturity transitions and merge.

## Quality bar

Prefer “confidence unchanged because evidence is indirect” over forced novelty. A synthesis should make it easier to disagree precisely and to design a decisive next experiment.
