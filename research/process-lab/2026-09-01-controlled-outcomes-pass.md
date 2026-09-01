# Controlled outcomes pass — 2026-09-01

## Purpose

Exercise the full local-query → live discovery → lawful staging → full-text appraisal → claim revision path on the active R001 question, with particular attention to null results and the difference between assisted and later independent outcomes.

This was a human-directed supervised shadow cycle. It is not an actual scheduler execution.

## Route and decisions

1. Queried the Atlas first and stated the gap: post-2025 studies that observe both support conditions and performance after support removal.
2. Audited research capabilities. OpenAlex/Crossref, native web, Docling and PDF extraction were available; Unpaywall remained unconfigured.
3. Ran native current-web and gateway/OpenAlex searches, then followed exact titles, citation leads and DOI/arXiv identities.
4. Staged candidate envelopes and lawfully stored three full texts in the gitignored inbox with rights receipts and hashes.
5. Inspected methods, results, tables and limitations before admission. Admitted at most three sources and represented nulls, fragile positive evidence and an authentic context.
6. Updated R001 screening, extraction, synthesis, atomic claims, a principle, queue, briefing and state; regenerated and validated the corpus.

## What worked

- The exact assisted/independent question quickly found studies that broad “AI learning outcomes” searches bury.
- Treating publisher barriers as screening outcomes prevented abstract-only evidence from entering canonical claims.
- The three-source cap created a balanced portfolio rather than three similar positive tutor studies.
- Full-text inspection materially changed interpretation: S023's relative decline is much larger than its null absolute retest contrast; S024 is not individually randomized; S025 underreports its later randomized group contrast.
- An authentic South African trial broadened context and challenged the assumption that tool access automatically expresses collaborative capability.

## Friction and limitations

- OpenAlex anonymous search returned a temporary 429 after initial discovery. The run did not hammer or loop retries.
- Elsevier identified the Bassner paper as CC BY but its public page presented a robot challenge and its unauthenticated API returned metadata only. The in-app browser could not proceed without a CAPTCHA, so the study remains held.
- The Barcauí paper's publisher PDF returned 403 and SSRN exposed the abstract but not an inspectable lawful full text in this pass.
- Docling returned no rendered CLI result for the Saloojee PDF after roughly 30 seconds; deterministic `pdftotext` extraction succeeded. The gateway should expose extractor timeout/failure diagnostics rather than silently returning nothing.
- This was a targeted update, not a database-complete search or formal RoB 2 assessment.

## Process improvements

1. Add a `research_gateway diagnose-extraction` or explicit timeout/error receipt when Docling produces no result.
2. Configure `UNPAYWALL_EMAIL` to improve lawful-location resolution and reduce publisher dead ends.
3. Add a screening status specifically for `awaiting-lawful-full-text` so it is distinguishable from methodological exclusion.
4. For every assisted/independent study, extract three values separately: supported outcome, absolute independent outcome, and change from supported to independent.
5. Require a design audit before accepting “randomized”: record unit of assignment, unit of analysis, clustering, exclusions after assignment and preregistration.
6. Carry unresolved high-value candidates automatically into the next R001 search rather than rediscovering them.

## Skill decision

Do not create another skill yet. The stable design-audit checks belong in the existing `atlas-research` extraction instructions after one more varied controlled-study pass confirms the pattern. The silent Docling result is a gateway defect candidate, not a skill.
