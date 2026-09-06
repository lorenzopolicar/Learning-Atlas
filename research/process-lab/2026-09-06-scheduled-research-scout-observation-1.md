# Scheduled research scout observation 1 — 2026-09-06

## Execution status

This was the first actual scheduler execution observed. The two earlier supervised shadow cycles remain excluded. After the canonical research update was formed, `.harness/state/research-state.json` advanced `actual_scheduled_runs_observed` from 0 to 1.

## Worktree and branch behaviour

- The first queue inspection happened in an unrelated dirty checkout and exposed a stale branch-local queue. No file there was edited.
- The run fetched `origin/main` and created the dedicated worktree `/private/tmp/learning-atlas-q004-20260906T094221Z` at commit `651eadf`, on unique branch `atlas/research-q004-retry-validity-20260906T094221Z`.
- The branch name retained the stale queue label, but the integrating agent selected the actual highest ready item from fresh `origin/main`: Q002's capability-evidence event contract. Canonical writes occurred only in the dedicated worktree.
- No worktree collision, branch rewrite or pull-request churn occurred during research. One draft pull request is planned after all checks pass; it will not be merged by the automation.

## Agent lanes, overlap and disagreements

Three read-only project-scoped agents worked independently while one integrating agent owned every canonical write and final epistemic judgment.

- `research_scout` followed event-schema, knowledge-tracing, standards, public social and podcast lanes. It preferred Mislevy/Gorin-style evidence-centred design, Qiu's time-model contradiction and Caliper.
- `evidence_analyst` compared assessment architecture, learner-model calibration/recency studies and current standards. It preferred Mislevy, Gervet and xAPI 2.0, and wanted scored observables separated explicitly.
- `contrarian` red-teamed privacy, construct validity and false precision. It preferred Jacobs and Wallach, a 2025 forgetting-model comparison, and an Australian privacy or empirical privacy source; it argued for separate observation, assertion, inference and governance records.

All three converged on the central boundary: an observation is not a capability assertion, raw self-report is not model uncertainty, and evidence retention is not cognitive expiry. Their candidate overlap was strongest around evidence-centred design and event/inference separation. They disagreed on whether the third source should optimize interoperability, calibration, recency or privacy. The integrating choice admitted S026, S027 and S028 because together they supply architecture, a genuine empirical contradiction and deterministic event-provenance semantics. The contract also adopted the contrarian's assertion provenance and three-clock warning without claiming those sources proved an Orqestra effect.

## Discovery, providers and parser failures

- Bounded Atlas retrieval returned 12 relevant artifacts in 4,735 characters before web discovery. `atlas.py freshness` reported seven model-dependent sources: zero current, two recent, four historical and one unknown.
- The gateway capability audit found OpenAlex and Crossref available; Unpaywall, Podcast Index and OpenAI transcription were unavailable. Exa was advertised as a separate MCP lane but was not callable in this environment. Zotero's local API probe failed.
- Initial OpenAlex discovery failed under sandbox DNS. The approved network rerun succeeded.
- Broad evidence-centred-design discovery drifted into irrelevant AI-teaching results, so exact-title and official ETS/CRESST resolution replaced it.
- The gateway exact-title search missed Qiu; native title search, DBLP and official EDM/ERIC proceedings resolved the paper.
- Docling returned no usable result for inspected PDFs. Deterministic `pdftotext` extraction was the fallback.
- Podcast Index was unavailable, so Apple Search plus publisher RSS was used. The PSI/Kristen DiCerbo episode received a stable publisher URL, RSS GUID and duration, but no transcript was available and audio was not inspected.
- Public LinkedIn posts were sampled with stable activity IDs. Direct LinkedIn inspection redirected to sign-up for one post, so it remained a partial snapshot and discovery lead. Public X search yielded no stable, inspectable position that changed the answer.

## Admissions and rejected candidates

The autonomous three-source cap was fully used:

1. S026 — Mislevy, Almond and Lukas: foundational evidence-centred assessment architecture.
2. S027 — Qiu et al.: empirical gains, nulls and reversals for time-aware BKT.
3. S028 — 1EdTech Caliper 1.2: authoritative event and transport-provenance semantics.

Held or rejected candidates included the broad 2023 knowledge-tracing survey (less direct than the primary falsifier), W3C VC 2.0 (credential layer outside E001), Longin et al. on data-sharing context (valuable privacy evidence but indirect), xAPI 2.0 (strong next-pass comparator but less deterministic gateway access), Gervet/Galyardt/Settles (calibration or decay alternates), Jacobs/Wallach and privacy sources (important red-team lanes but outside the chosen narrow claim), LinkedIn posts and podcasts (context only), and the legacy open xAPI 1.0.3 text (not current authority).

## Validation and requested human decisions

- Both JSON Schemas and all synthetic fixtures passed `check-jsonschema`.
- Strict validation covered 61 artifacts with zero errors and zero warnings; all six retrieval evaluations passed; all 34 repository tests passed; indexes and the NotebookLM pack were regenerated and verified current.
- Human review is requested on the observation/assertion/inference boundary, the burden of required assistance provenance, and whether Q002 should stay active for co-design. No Orqestra implementation or credential use is authorized.

## Process lesson

Selecting from a freshly fetched worktree is not merely Git hygiene: it changed the research question. The three-source cap worked best when each admission had a distinct epistemic job. Future scheduled runs should preserve the agent disagreement matrix and promote a candidate only when it changes the claim, boundary or falsifier—not because a lane is fashionable or easy to access.
