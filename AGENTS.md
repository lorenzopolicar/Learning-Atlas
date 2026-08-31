# Learning Atlas agent instructions

## Mission

Build a rigorous, cumulative, and useful body of knowledge for AI-powered learning systems. Optimize for durable understanding, honest uncertainty, and product decisions that can be traced back to evidence.

## Before doing research or synthesis

1. Read `ontology/epistemic-policy.md` and `ontology/taxonomy.md`.
2. Read the relevant generated index in `indexes/`.
3. Query the atlas rather than loading the whole repository:
   `python3 scripts/atlas.py query "<question>" --type claim --type principle`.
4. For scheduled work, read `.harness/state/research-state.json` and the relevant runbook.

## Epistemic rules

- Keep source, claim, belief, principle, decision, and experiment as distinct artifact types.
- Use primary research and authoritative reports whenever possible. Record reviews as reviews.
- Never promote a claim from a search snippet, abstract alone, or an uncited model summary.
- State population, setting, intervention, comparator, outcome, duration, and key limitations when known.
- Record boundary conditions, contradicting evidence, and what would change a belief.
- Separate immediate assisted performance from independent, delayed, and transfer outcomes.
- Treat philosophical and critical perspectives as discourse unless they make empirically testable claims.
- Cite atlas IDs in synthesis and product work, for example `[C001]` and `[P005]`.
- Do not invent bibliographic details. Mark unknowns explicitly and queue them for verification.

## Change policy

- Agents may create draft artifacts and pull requests.
- Only a human-reviewed change may mark a claim `established`, a belief `adopted`, or a principle `active`.
- Automated runs admit at most three new sources. Prefer deepening an existing evidence chain over indiscriminate collection.
- Do not store copyrighted papers, private learner data, credentials, or identifiable research participants in this repository.
- Do not auto-merge research changes.

## Required checks

Run these before handing off any change:

```bash
python3 scripts/atlas.py index
python3 scripts/atlas.py export notebooklm
python3 scripts/atlas.py validate --strict
python3 scripts/atlas.py eval
python3 -m unittest discover -s tests -v
```

If generated files change, include them in the same commit.

## Repository map

- `sources/notes/` — one source record per work
- `reviews/` — protocols, search logs, extraction tables, and syntheses
- `claims/`, `beliefs/`, `principles/` — the core reasoning chain
- `decisions/`, `experiments/`, `questions/` — application and falsification
- `discourse/` — normative, critical, and historical perspectives
- `bridges/` — consumption guidance for projects such as Orqestra
- `.harness/` — specifications, runbooks, state, and evaluations
- `.agents/skills/` — shared Codex/Claude workflows
- `scripts/atlas.py` — deterministic validation, indexing, retrieval, and export

## Writing style

Prefer precise prose over academic performance. Make the strongest supportable claim, then show its limits. A useful atlas entry is concise enough for an agent to retrieve and rich enough for a human to contest.
