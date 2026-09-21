# Scheduled research scout observation 3 — 2026-09-22

## Execution status

This was the third actual scheduler execution observed. The 2026-08-31 and 2026-09-01 supervised shadow cycles remain excluded. After canonical integration and validation, `.harness/state/research-state.json` advances `actual_scheduled_runs_observed` from 2 to 3, meeting the observation target.

## Worktree and branch behaviour

- The source checkout was clean on user branch `assessment-revamp-research-2026-09` and was not edited.
- The run fetched `origin/main` at `651eadf` and created `/private/tmp/learning-atlas-weekly-20260922-fqUEZJ` on unique branch `atlas/research-weekly-20260922T223247Z`.
- Draft PRs #1 and #2 remained open and CI-green. The worktree fast-forwarded to the verified PR #2 head `379758a`, preserving observations 1–2 and selecting the next ready queue item from the integrated stack.
- Today's draft PR is stacked on the PR #2 head so its diff remains independent. No prior PR was modified, closed or merged.
- Canonical writes occurred only in the dedicated worktree. Gitignored candidates and extracted PDFs stayed in `.harness/inbox/`; no full text enters Git.

## Agent lanes, overlap and disagreements

Three project-scoped read-only lanes worked independently; the integrating agent owned every canonical write and final judgment.

- `research_scout` searched validated agency/help measures and current observable GenAI reliance. It preferred Reeve and Tseng, Zheng et al. and Viberg et al. as a self-report/behaviour/qualitative portfolio.
- `evidence_analyst` audited psychometrics, samples and criterion validity. It supported the Reeve scale as a construct anchor but warned that current dependence/help measures rarely predict delayed independent outcomes.
- `contrarian` searched for invalidating cases. It preferred Chen et al., Roll et al. and Double/Birney because they break agency=independence, help-log=learning and confidence-prompt=neutral assumptions.

All lanes agreed against a composite score and against diagnosing dependence from use frequency. The key disagreement was whether to admit the best available measurement instruments or the sources that invalidate the measurement plan. The integrating agent chose the latter because each changes E001 and Orqestra inference immediately; the former remain explicit held candidates.

## Candidate overlap, providers and parser failures

- Bounded Atlas retrieval and freshness audit preceded discovery. Existing S021/C010 already covered metacognitive sensitivity, RAIR and RSR, so another generic calibration paper would duplicate rather than change the answer.
- The CLI capability probe found OpenAlex, Crossref and Docling available; Unpaywall, Podcast Index, YouTube API and OpenAI transcription were unavailable. Exa was listed as a separate MCP but not callable. The intent-level Atlas MCP tools were absent, so the documented gateway CLI supplied staging, identity, lawful locations and hashes.
- Full Chen and Double PDFs were lawfully staged in the gitignored inbox and inspected with deterministic extraction.
- The Roll gateway result was metadata-only and the author PDF presented an expired TLS certificate. DOI/author-host identity was independently verified; the PDF was streamed once with certificate verification disabled into `pdftotext`, not stored or committed.
- The Goh journal page returned HTTP 403, so the OSF-hosted author preprint was inspected. The Viberg publisher PDF endpoint returned HTTP 404. Neither was admitted.
- Public LinkedIn and podcast sources were sampled only as perspective/discovery leads. No engagement signal determined evidence weight and no media/social candidate was admitted.

## Admissions and rejected candidates

The three-source cap was reached with S045 (autonomy versus independence), S046 (help behaviour versus learning) and S047 (confidence-rating reactivity).

Held: Reeve and Tseng's agentic-engagement measure, Zheng's current reliance taxonomy, Viberg's LLM help-seeking process and Goh's bounded harm/dependency scale. Rejected for product inference: pathology-first cross-sectional dependence scales, text similarity as agency, and social/podcast arguments as effect evidence.

## Validation, pull-request churn and human decisions

- `python3 scripts/atlas.py index` and `python3 scripts/atlas.py export notebooklm` regenerated ten canonical views and the NotebookLM pack.
- Strict validation passed for 72 artifacts with 0 errors and 0 warnings. All 6 retrieval contracts and all 34 unit tests passed. The freshness audit still reports 10 explicitly classified model-dependent sources, and `git diff --check` passed.
- Draft PR #3 was opened against the PR #2 head. Its Atlas integrity check completed successfully; the stack was clean and it had no comments or reviews at first handoff. The repository again exposed neither a `codex` nor a `codex-automation` label, so neither could be applied.
- Human review is requested on the construct separation, the decision to admit falsifiers over candidate instruments, and the E001 confidence-prompt randomization. No auto-merge was enabled. No Orqestra implementation, learner scoring or merge is authorized.

## Process lesson

Lane diversity is not enough if every lane accepts the same construct mapping. The contrarian lane needs authority to replace apparently stronger psychometric candidates with sources that invalidate a proposed inference. This run also confirms that open PR heads must be reconciled as scheduler state before queue selection and ID allocation.
