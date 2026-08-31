# Maintenance runbook

## Every change

- validate artifact schema and references;
- regenerate indexes, graph, and NotebookLM pack;
- run unit tests;
- inspect the diff for accidental generated noise.

## Monthly

- resolve stale or broken links;
- review new contradictions and null findings;
- verify retractions, corrections, and publication status for influential sources;
- review belief and principle confidence;
- check that generated retrieval returns boundary conditions and source links for key questions.

## Quarterly

- run a stale-artifact sweep;
- review taxonomy drift and merge near-duplicate tags;
- inspect citation graph orphans;
- evaluate automation precision using `.harness/evals/cases.json`;
- review schedule value, source admission rate, and human-review burden;
- archive or merge low-value research questions.

## Annually

Publish a state-of-the-atlas synthesis: what changed our mind, what remains uncertain, what product decisions were influenced, which predictions failed, and where the evidence portfolio is biased.
