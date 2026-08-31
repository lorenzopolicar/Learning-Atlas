# Research cycle runbook

## Purpose

Convert a live research question into a small, reviewable improvement to the atlas. The cycle is deliberately rate-limited: cumulative knowledge requires selection and revision, not maximal collection.

## Weekly scout

1. Read `AGENTS.md`, the epistemic policy, `research/queue.md`, and `.harness/state/research-state.json`.
2. Select one ready question. Prefer an existing claim whose boundary or confidence could materially change.
3. Query the atlas for existing work. State the gap before searching externally.
4. Search across the source lanes the question warrants: scholarly literature, citation chains, authoritative reports, books, standards, datasets, podcasts/interviews, talks, and practitioner discourse. Record exact queries, providers, dates, and result paths for an active review.
5. Call `research_capabilities`; use native web and Exa for discovery, then the Atlas research gateway for identity, provenance, locators, extraction, and local staging.
6. Inspect the actual source. Admit at most three sources, emphasizing nulls, contradictions, replications, underrepresented contexts, and useful non-empirical challenges.
7. Create or revise atomic claims, beliefs, discourse tensions, or questions according to source role. Never promote from snippets, metadata, abstracts, or automatic transcripts alone.
8. Write a weekly briefing: signal, evidence change, contradictions, product implication, source-portfolio effect, and next question.
9. Update research state, regenerate derived files, validate, and test.
10. Open a draft pull request. Do not merge it.

## Monthly synthesis

1. Review all changes since `last_monthly_synthesis` in state.
2. Group evidence by claim and outcome—not by author or paper.
3. Seek the strongest counterposition and contradictory sources.
4. Propose belief and principle revisions with old/new wording and explicit reasons.
5. Identify which Orqestra decisions or experiments may be affected.
6. Assess portfolio balance across empirical, architectural, normative, critical, and institutional work.
7. Run a source-lane audit. Identify whether convenient papers and web pages are crowding out books, datasets, practitioner testimony, historical/critical work, or voices outside dominant institutions.
8. Produce a synthesis briefing and draft pull request; do not self-approve maturity changes.

## Quarterly direction review

Assess whether the agenda still serves the north-star inquiry. Retire low-value questions, refresh stale artifacts, and review whether the atlas has become biased toward convenient outcomes, populations, disciplines, or optimistic AI results.

Use `research/agenda-ledger.md` to record agenda changes and their signals. Programmes provide continuity; queue items, methods, source lanes, and priority weights should evolve whenever evidence gaps, product decisions, field changes, or falsification opportunities justify it.

## Stop conditions

Stop and report rather than filling gaps with inference when:

- full text or essential methods cannot be inspected;
- bibliographic metadata conflicts across authoritative records;
- the question requires personal/identifiable learner data;
- a proposed belief change rests on one fragile study;
- generated files or validation cannot be made clean;
- existing human edits conflict with the automated branch.
