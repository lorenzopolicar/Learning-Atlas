# Scheduled observation counter reconciliation — 2026-10-26

## Why this note exists

The branch was correctly created from the latest `origin/main`, where `.harness/state/research-state.json` still reported zero actual scheduled observations. The open draft research PR stack contains the three required dated observation records and the corresponding counter at 3/3:

- 2026-09-06 — scheduled observation 1;
- 2026-09-14 — scheduled observation 2;
- 2026-09-22 — scheduled observation 3.

Those runs were real scheduler executions. The 2026-08-31 and 2026-09-01 supervised cycles remain excluded. Repeating a fourth observation because the draft stack has not merged would misstate the process and violate the three-run limit.

## Decision

Reconcile the counter on this independent branch to 3/3 and preserve the dates in the state note. Do not count the 2026-10-26 scout as another observation. The detailed first-three observation files remain reviewable in the open draft PR stack; this note makes the main-base staleness and the reconciliation auditable without copying unrelated research changes into this branch.

## Current-run process lesson

Independent branches from `origin/main` need a preflight against open research PRs for both identifier allocation and process state. This run reserved S057–S059 after auditing the draft stack through S056. Future automation should obtain an explicit source-ID reservation and read operational observation state from merged history plus open draft research heads before making canonical writes.
