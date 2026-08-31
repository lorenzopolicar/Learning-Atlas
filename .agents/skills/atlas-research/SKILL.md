---
name: atlas-research
description: Research and advance one Learning Atlas question across papers, books, reports, datasets, podcasts, interviews, lectures, videos, newsletters, standards, and practitioner discourse. Use for weekly scouting, source appraisal, active reviews, citation chaining, counterevidence, multimedia research, or research briefings. Routes Codex or Claude through native web/Exa discovery and the Atlas research MCP for verification, lawful extraction, timestamped provenance, staging, typed evidence artifacts, a three-source autonomous admission cap, validation, and a human publication gate.
---

# Atlas research

Advance one question without turning the atlas into an indiscriminate link collection.

## Load

Read these completely before acting:

1. `AGENTS.md`
2. `ontology/epistemic-policy.md`
3. `.harness/runbooks/research-cycle.md`
4. `.harness/runbooks/source-intake.md`
5. `.harness/specs/research-scout.md`
6. `research/queue.md`
7. `.harness/state/research-state.json`
8. `references/tool-routing.md`

Read `references/multimedia-provenance.md` when a source is audio, video, an interview, a talk, or a transcript.

Then query the repository for the selected question. Do not load every artifact.

## Run

1. Select one unblocked queue item and state the existing evidence gap.
2. Call `research_capabilities`. Choose source lanes because they can change the question—not to satisfy a media quota.
3. Search broadly with native web and Exa, then use the Atlas research MCP to resolve identity, citation context, lawful access, content hashes, pages/timestamps, and transcript provenance.
4. Stage promising normalized candidates. Staging is a reversible inbox action, not atlas admission.
5. Inspect the actual source. An abstract screens a paper; a transcript navigates media. Neither alone is enough for a promoted empirical claim.
6. Assign epistemic role before extracting conclusions. Follow every consequential “research shows” statement to the original work.
7. Admit no more than three new sources in an autonomous run. Use the closest source profile and verified bibliographic metadata.
8. Update screening/extraction records if the question belongs to an active review.
9. Create or revise the artifact the source warrants: atomic claim, belief, discourse tension, question, decision implication, or experiment. Preserve boundaries and contradictions.
10. Write a dated briefing, include the source-portfolio effect, and update research state.
11. Run the required checks in `AGENTS.md`.
12. Show the human the claim-level or belief-level change and open a draft pull request when authorized. Never merge it.

## Quality bar

- A negative result, corrected metadata record, or narrower boundary is valid progress.
- Never infer causality from engagement or supported output quality.
- Never commit copyrighted full text or identifiable learner data.
- Never commit full podcast/video transcripts or media. Keep bounded excerpts and precise timestamps in Git; keep lawful working copies in the local inbox or approved private storage.
- Treat expert perspective and firsthand testimony as valuable in their own right. Do not call them weak papers; do not call them experiments.
- Record access failure, missing credentials, automatic-transcript uncertainty, and provider fallback explicitly.
- Stop at `seed` when methods or outcomes remain inaccessible.

## Return

Report the question and existing gap, source lanes searched, exact provider fallbacks, candidates rejected/staged/admitted, locators and provenance, epistemic changes, product implications, limitations, and the next falsification step.
