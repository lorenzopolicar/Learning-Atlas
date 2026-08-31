---
name: consult-learning-atlas
description: Consult the Learning Atlas for evidence-backed AI learning-system design. Use when implementing or reviewing tutoring, learner modelling, feedback, assessment, personalization, learning measurement, AI literacy, or human-AI capability features—especially in Orqestra. Returns a bounded typed evidence chain with IDs, boundaries, epistemic roles, and a falsification plan rather than loading the entire knowledge base.
---

# Consult Learning Atlas

Use the atlas as a compact evidence layer for a concrete product decision.

## Locate and retrieve

Use `$LEARNING_ATLAS_ROOT` if set; otherwise use `/Users/lorenzo.policar/Projects/learning-atlas`.

Run:

```bash
atlas_root="${LEARNING_ATLAS_ROOT:-/Users/lorenzo.policar/Projects/learning-atlas}"
python3 "$atlas_root/scripts/atlas.py" query "<product question>" --type claim --type belief --type principle
```

The default result is bounded to 12 artifacts and 6,000 characters. Do not replace this with a whole-repository scan.

For questions about what is worth learning, AI literacy, institutional purpose, or the construct of human-AI capability, also include the relevant non-core lanes:

```bash
python3 "$atlas_root/scripts/atlas.py" query "<product question>" \
  --type claim --type belief --type principle \
  --type question --type discourse --type source
```

Use these lanes when the decision genuinely turns on contested purposes, source appraisal, or institutional frameworks; do not add them to a narrow implementation query by habit.

## Read and apply

1. Read `.harness/specs/atlas-consultant.md` and `ontology/epistemic-policy.md`.
2. Open only the selected artifact files and any source note needed to verify a decisive detail.
3. State whether the product goal is deliberate learning, assessment, or performance support.
4. Return:
   - recommendation;
   - evidence chain using atlas IDs;
   - boundary conditions and exceptions;
   - implementation implications;
   - measurement and falsification plan;
   - open questions.
   Keep causal evidence, institutional guidance, expert perspective, testimony, and normative argument visibly distinct. A discourse note can constrain product taste without becoming an empirical effect claim.
5. Cite atlas IDs in code comments, decision records, or implementation plans when they materially justify a choice.

## Feedback loop

If product evidence challenges the atlas, propose an experiment or research question in the atlas. Product telemetry is an observation in context, not automatic proof of a general learning claim.

Do not edit the atlas from another repository unless the user explicitly asks. Never copy private learner data into it.
