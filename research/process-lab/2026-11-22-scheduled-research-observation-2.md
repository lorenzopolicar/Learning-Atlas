# Scheduled research scout observation 2 — 2026-11-22

## Execution status

This is the second actual scheduler execution observed. The live scheduler record names the 14 November run as the previous execution; draft PR #12 preserves observation 1. The older proving and controlled-outcomes cycles remain supervised shadows. After this run's canonical update, `actual_scheduled_runs_observed` advances to 2 of 3; this file is not a fourth observation derived from historical automation notes.

## Worktree and branch behaviour

- Fetched exact `origin/main` `651eadf5f6683653982dbf4b86d0c9c746d325c8` and created `/private/tmp/learning-atlas-weekly-20261122T052614Z-egx4wB` on unique branch `atlas/research-weekly-20261122T052614Z`.
- The unrelated checkout remained on `assessment-revamp-research-2026-09` and was not edited.
- An initial absolute-path queue read came from that checkout and suggested Q005. The integrating lane compared it with `git show origin/main:research/queue.md`, caught that Q005 is absent from the canonical base, stopped all three agent lanes, and restarted them on Q002 before any write.
- Open draft PRs #1–#12 were audited. IDs S065–S067 and C039–C040 were reserved beyond every open branch to avoid collision; no open branch was rewritten or force-pushed.

## Agent lanes, overlap and disagreements

Three independent project-scoped, read-only lanes ran after the correction; one integrating lane owned every canonical write and final judgment.

- `research_scout` prioritised DRIVE and a real-log subgroup-calibration comparison. It would admit xAPI only if typed contextual actors changed the contract.
- `evidence_analyst` prioritised the exact xAPI 2.0 mapping boundary and a synthetic sparse/noisy-history calibration study.
- `contrarian` prioritised DRIVE and Jisc, rejected standards conformance as validity evidence, and surfaced an already-admitted confidence-rating reactivity trial plus a small teacher-decision null.

All lanes overlapped on DRIVE and on treating assistance function as a versioned assertion. The integrating lane admitted DRIVE, the real-log calibration study and Jisc: classification reliability, decision calibration and purpose/minimisation each have a distinct epistemic job. xAPI was inspected and held as an overlapping comparator; the synthetic calibration study was held behind the more direct real-log study.

## Candidate overlap and admission decisions

- Admitted: S065 Oliveira et al.; S066 Nurmukhambet and Meirmanova; S067 Jisc.
- Held after full inspection: xAPI 2.0, Jin's sparse/noisy-history preprint, KT-DUSL, and the Frontiers LMS-privacy analysis.
- Held or rejected after bounded inspection: an already-admitted confidence-rating study, a 12-teacher simulated decision preprint, a public LinkedIn summary, and a publisher-transcript podcast perspective.
- Social reach and speaker identity affected sampling only. The LinkedIn activity's empirical link was followed to the original work; neither the post nor podcast was treated as effect evidence.

## Provider and parser behaviour

- Repository capabilities: OpenAlex, Crossref and Docling available; Unpaywall, Podcast Index and OpenAI transcription unavailable; Exa advertised but no callable intent-level Atlas/Exa surface existed.
- OpenAlex/Crossref supplied deterministic identity and citation metadata. Native web and lawful publisher/author copies supplied actual inspection.
- IEEE GitLab returned HTTP 418 to browser access; cloning official tag 2.0.0 succeeded. The standard was hashed and inspected locally.
- Research Square's DOI normalization produced a malformed canonical URL; the publisher page exposed the lawful versioned PDF URL.
- `pdftotext` supplied stable bounded extraction. No full text, transcript or media was committed.
- The IEEE calibration paper had no open locator in OpenAlex; a complete author-posted rendering was inspected, with rights recorded as unclear and no local copy retained.

## Validation and pull-request churn

Index and NotebookLM generation completed. Strict validation passed across 62 artifacts with no errors or warnings; all 7 retrieval evaluations and 31 unit tests passed; freshness classified 7 model-dependent sources; JSON parsing and `git diff --check` passed. The branch intentionally leaves the E001 JSON Schema unchanged: draft PR #1 already revises that contract, and another independent schema edit would create avoidable semantic and merge churn before the new reliability gate is reviewed.

The repository's many clean but unmerged draft PRs continue to make IDs, state and research context diverge from `main`. This run remains an independent draft against `main` and requests human consolidation rather than silently stacking or importing unrelated changes.

## Requested human decisions

1. Confirm that assistance-function reliability, missingness and participation effects should gate any E001 schema expansion.
2. Confirm that subgroup/stage/threshold decision calibration is the correct next falsification, without interpreting performance-defined groups as demographic fairness evidence.
3. Consolidate or sequence draft PRs #1–#12 so scheduled work can stop re-reserving IDs and reconciling stale research state.

## Process lesson

A worktree does not protect question selection if policy files are still read through absolute paths to another checkout. Resolve all repository-relative instructions from the new worktree before selecting a queue item or dispatching agents. The correction cost was small because no canonical write had begun; after admission it would have created a false research branch.

