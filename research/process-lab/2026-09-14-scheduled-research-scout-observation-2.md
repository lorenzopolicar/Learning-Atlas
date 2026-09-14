# Scheduled research scout observation 2 — 2026-09-14

## Execution status

This was the second actual scheduler execution observed. The two earlier supervised shadow cycles remain excluded. After canonical research integration, `.harness/state/research-state.json` advances `actual_scheduled_runs_observed` from 1 to 2.

## Worktree and branch behaviour

- The source checkout was on user branch `assessment-revamp-research-2026-09` and was not edited.
- The run fetched `origin/main` at `651eadf` and created `/private/tmp/learning-atlas-weekly-20260914-EVZ6eG` on unique branch `atlas/research-q004-retry-evidence-20260914T000000Z`.
- Draft PR #1 remained open and CI-green at commit `0b155d5`, so its content was applied before today's work. Draft PR #2 uses the PR #1 head as its base, keeping today's diff independent while preserving scheduler state.
- Git signing was unavailable inside the sandbox during the cherry-pick. The identical commit content was created with per-command signing disabled; no repository signing setting changed.
- The first PR #2 push contained that equivalent tree as a distinct commit, so GitHub marked the divergent stack dirty and did not start CI. Tree hashes matched exactly. Today's commit was rebased onto the actual `0b155d5` parent and the new automation branch was updated with `--force-with-lease`; PR #2 then became clean and triggered CI.
- Canonical writes occurred only in the dedicated worktree. The current source checkout already contains unrelated, unmerged IDs S029–S041 and C014–C027, so this run reserved S042–S044 and C028–C029 to avoid cross-branch identity collision.

## Agent lanes, overlap and disagreements

Three project-scoped read-only lanes worked independently; the integrating agent owned all canonical writes and final judgments.

- `research_scout` searched progressive-hint, attempt-before-answer, Socratic, static-hint, null and worked-example lanes. It found no study isolating the full P001 sequence and preferred LearnLM/Eedi, a reflection-before-hint null and a historical worked-solution counterexample.
- `evidence_analyst` deeply reappraised S024. It found a binary direct-answer access gate rather than progressive hints, high clustering/exclusion risk, missing grant logs, a 43.2% versus 48.6% AI-use discrepancy and a sensitivity that could shrink the effect. It recommended no confidence promotion.
- `contrarian` surfaced expertise-reversal and worked-example-first evidence, pacing burden and answer-first diagnostic use. It preferred a conditional opportunity to attempt with immediate schema/accommodation exceptions and a fast reveal.

All lanes agreed that retry success is not delayed learning and that no current source isolates initial attempt, hint sequence, adaptive timing and reveal. Disagreement centred on the third admission: mechanism meta-analysis, historical worked-example counterexample, reflection-before-hint null or current-system strict-withholding falsifier. The integrating agent admitted S044 because its same-model current-system contrast changes the product policy most directly; the mechanism sources remain explicit boundaries.

## Candidate overlap, providers and parser failures

- Bounded Atlas retrieval and freshness audit preceded discovery. All lanes overlapped on S024/S001 and the absence of a delayed component trial.
- The CLI capability probe found OpenAlex, Crossref and Docling available; Unpaywall, Podcast Index, YouTube API and OpenAI transcription were unavailable. Exa was listed as a separate MCP but not callable. The intent-level Atlas MCP tools were absent, so the documented gateway CLI supplied staging, identity, lawful fetch and hashes.
- Sandbox DNS initially blocked OpenAlex; the approved rerun reached the provider. Two queries then returned HTTP 429, while a third produced a noisy result set.
- Docling returned no output on the 72-page NBER paper; `pdftotext` was the deterministic full-document fallback. Docling succeeded for a smaller arXiv candidate.
- SSRN returned HTTP 403 for the direct Socratic-versus-non-Socratic paper, which remained held.
- Podcast Index fallback used Apple Podcasts Search and publisher RSS/page. Public LinkedIn inspection preserved activity ID `7432447285814329346` and a content hash. Neither media/social candidate was admitted.

## Admissions and rejected candidates

The three-source cap was reached with S042 (large field RCT and one-week signal), S043 (static hint versus interactive post-error support) and S044 (current-system strict-withholding counterexample).

Held: Blasco/Charisi and Bassner direct nulls because full methods were unavailable. Rejected from admission: Heickal/Lan because its retry analyses are associative and lack independent outcomes; Choi because the activated sample is small and no delayed outcome was measured; the historical worked-solution paper because its technology and intervention are less direct; LinkedIn and podcast positions because they are perspectives/discovery leads rather than causal evidence.

## Validation, pull-request churn and human decisions

- `python3 scripts/atlas.py index` and `python3 scripts/atlas.py export notebooklm` regenerated the canonical views and NotebookLM pack.
- `python3 scripts/atlas.py validate --strict` passed with 66 artifacts, 0 errors and 0 warnings.
- `python3 scripts/atlas.py eval` passed all 6 retrieval contracts. The new progressive-assistance records initially displaced P004 from EV004's bounded result window, so the fixture query was sharpened to name both target principle phrases; its expected IDs and concepts were not relaxed.
- `python3 -m unittest discover -s tests -v` passed all 34 tests. The freshness expectation was updated from 7 to 10 model-dependent sources after S042–S044 entered the register.
- PR #1 was not modified, closed or merged. Draft PR #2 is deliberately stacked to avoid duplicating its content; its Atlas integrity check passed and it had no comments, reviews or unresolved threads at handoff. The repository exposed neither a `codex` nor a `codex-automation` label. Human reviewers must decide merge order and whether to accept the P001 wording change.
- Human review is requested on the friction-floor/friction-ceiling boundary, the legitimacy of worked-example-first exceptions, the required one-click reveal, and whether Orqestra should prioritize the proposed factorial. No product implementation or learner-data collection is authorized.

## Process lesson

Open research PRs are part of scheduler state even when `origin/main` has not advanced. The automation needs to reconcile live PR state with the main-branch queue before selecting work. ID reservation must also consider unrelated active branches, not just main, because permanent Atlas identities can otherwise collide before merge.
