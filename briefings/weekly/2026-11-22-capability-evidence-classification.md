# Weekly research briefing — 2026-11-22

## Question and prior gap

This pass advances [Q002]: how should a capability-evidence event represent assistance, context, confidence and expiry without creating false precision or disproportionate surveillance?

The fresh `origin/main` gap was that [D002] and [E001] treated assistance function as a field to record and model uncertainty as a boundary to expose, but did not say how reliable the assistance classification must be or how calibration should be tied to a learner group, evidence stage and decision threshold. Draft PR #1 already proposes observation/assertion/inference separation using evidence-centred design, time-aware BKT and Caliper; this run avoids duplicating those sources and asks whether the richer contract earns its fields.

## Search and source lanes

The source lanes were chosen because each could change the contract:

- **Empirical interaction classification:** `AI assistance function classification inter-rater reliability learners support accessibility generative AI study`; `human AI assistance taxonomy interrater reliability education classification study`; exact-title and DOI resolution for Oliveira et al.
- **Learner-model calibration and decision error:** `learner model uncertainty calibration empirical study knowledge tracing calibration reliability 2025`; `learner model richer features no improvement simple baseline knowledge tracing replication empirical study`; exact-title/DOI search and citation exploration for subgroup calibration.
- **Standards and governance:** `site:opensource.ieee.org xAPI 2.0 specification statement context result confidence timestamp authority official`; `learning analytics data minimization privacy official guidance student event logs education`.
- **Critical and public discourse:** public LinkedIn activity `7487371655967612928` linked to the original 2026 Frontiers LMS-privacy analysis; the 2026 Getting Smart episode *Are Schools Collecting Too Much Data?* supplied a publisher transcript and consent/ownership counterposition. Neither was used as empirical authority.

OpenAlex and Crossref supplied identity and citation-chain metadata. The original publisher or author-hosted works supplied methods and results. The calibration citation chain was checked against probability-calibration, multicalibration and knowledge-tracing foundations; no later cited-by record existed at retrieval. DRIVE's cited theory helped interpret its taxonomy, but the admission rests on the inspected study itself.

## Capabilities and fallbacks

`research_capabilities` through the repository gateway reported OpenAlex, Crossref and Docling available. Unpaywall, Podcast Index and OpenAI transcription were unavailable; `UNPAYWALL_EMAIL` and `OPENAI_API_KEY` were unset. Exa was described as a separate MCP but no intent-level Atlas MCP or Exa tool was callable, so native web plus the repository gateway supplied discovery and deterministic provenance.

The IEEE xAPI 2.0 web host returned 418 to the browser, so the official tagged repository was cloned at tag `2.0.0`, commit `134afd8`; the content standard SHA-256 is `c3363a1c59937cec4a1737b0be85f465f90fda7eed5549aa4996d8098d66b291`. Research Square's DOI resolver produced a malformed gateway URL, so the publisher page supplied the lawful versioned PDF URL. PDF inspection used `pdftotext` because it produced stable bounded text; no full paper, transcript or media entered Git. The IEEE calibration paper had no open locator in OpenAlex; the complete author-posted rendering was inspected, but its rights remain unclear and no local full text was retained.

## Admissions

The autonomous three-source cap is fully used:

1. **[S065] Oliveira et al. (2025), DRIVE.** In three authentic university writing courses, 33 of 103 reported GenAI users lacked usable logs. On a 33-log, 772-annotation reliability subset, mean pairwise kappa for the 35-category taxonomy was .44, with wide per-category variation. The study also reports that grading interactions may have reduced GenAI adoption. This supports new low-confidence [C039]: assistance function is a fallible, reactive classification, not an observed fact.
2. **[S066] Nurmukhambet and Meirmanova (2026).** Across six knowledge-tracing models and 5.89 million EdNet interactions, aggregate ECE below .025 concealed systematic overprediction for lower-performing learners, subgroup-stage ECE up to .195, and threshold-dependent simulated false-mastery gaps. This supports seed [C040]: aggregate calibration cannot authorize learner-level decisions by itself.
3. **[S067] Jisc learning-analytics code, updated 2026.** The current institutional guidance requires a defined use, minimum necessary data, validation of incomplete records, learner access and correction, bounded retention and explicit governance for AI-enabled decisions. It constrains the ledger's collection burden without pretending to prove an effect.

## Held and rejected candidates

- **xAPI 2.0:** inspected completely and compared, but held from admission because draft PR #1 already admits Caliper for event/envelope provenance and xAPI adds no native assistance, calibrated confidence, privacy or expiry semantics. The standard supports distinct event/stored time, authenticated authority, typed contextual agents and voiding; it does not guarantee a complete immutable evidence envelope or make voiding equivalent to E001's learner correction. A future export needs controlled IRIs and an explicit mapping; the current JSON Schema remains normative.
- **Jin (2026), sparse/noisy KT calibration:** actual three-day-old simulation preprint inspected and staged. It is a useful falsifier for truncated-history calibration, but the real-log subgroup study was more direct and mature for this run's one calibration slot.
- **Ait Chabane et al. (2026), KT-DUSL:** held. Explicit uncertainty improved some next-response metrics under sparse mono-concept data, while domain propagation added almost nothing in multi-concept Eedi. It does not test decision utility, construct validity or governance.
- **Badiuzzaman and Rahman (2026):** current qualitative document analysis of Moodle, Canvas and Blackboard inspected. Held in favour of Jisc's more direct current governance requirements; its privacy-harm mapping remains corroboration.
- **Double et al. confidence-rating reactivity:** not re-admitted because it is already S047 in draft PR #3. It remains an important warning that confidence elicitation is an intervention, not passive metadata.
- **Khalid et al. (2025):** held as a small simulated teacher-decision preprint; richer or more interpretable representations did not clearly change decisions, but N=12 is too fragile for admission here.
- **LinkedIn and podcast positions:** sampled for discovery and a strong learner-ownership counterposition. The stable LinkedIn post was followed to the original Frontiers paper; the Getting Smart publisher transcript was inspected. Neither changes the empirical admissions or receives evidence weight from reach.

## Agent comparison and integrating judgment

All three read-only agents converged on DRIVE and on the boundary that an assistance label is an assertion. They disagreed on the second and third slots:

- the scout preferred DRIVE plus the real-log subgroup-calibration study and would admit xAPI only if typed contextual actors changed the contract;
- the analyst preferred xAPI plus a new synthetic calibration study because those sources expose export and truncated-history edge cases;
- the contrarian preferred DRIVE plus Jisc, warning that standards conformance can launder event transport into validity and that confidence collection itself can react on learning.

The integrating decision admits DRIVE, the real-log subgroup study and Jisc. That portfolio provides one empirical classification constraint, one empirical calibration/decision constraint and one current governance boundary. xAPI is recorded as an inspected comparator rather than consuming a slot for overlapping transport semantics.

## Claim and product change

New [C039] makes assistance function explicitly fallible, versioned and correctable. New [C040] makes calibration conditional on the population, evidence stage and threshold-level decision audit. [C007] and [C008] are narrowed without maturity promotion.

For Orqestra, this changes the next move from schema expansion to falsification. E001 should first double-code a small co-designed vocabulary, preserve `unknown`, `mixed` and `disputed`, measure missing/unusable traces and learner corrections, and test whether logging changes participation. Any model inference should expose its calibration population, evidence stage, threshold and false-decision audit. The richer ledger must beat a purpose-minimal baseline on a declared intervention or review decision, not merely prediction fit.

No current Orqestra schema change or product deployment is authorized. Draft PR #1's separate observation/assertion/inference direction survives, but this run deliberately leaves its JSON Schema untouched until the open research stack is consolidated and the new reliability gate is reviewed.

## Uncertainty and next falsification

The classification evidence is one domain-specific observational study. The calibration study uses one TOEIC dataset, performance-defined subgroups and simulated promotion decisions; it does not establish demographic unfairness or observed learning harm. Jisc is guidance, not causal evidence. No source establishes a universal agreement threshold, retention period or assistance taxonomy.

Next: co-design the smallest useful assistance vocabulary with learner, domain and accessibility reviewers; double-code it prospectively; report per-label agreement, missingness, learner corrections and participation effects; and compare the rich ledger with a purpose-minimal no-history baseline. Predeclare stage-, group- and threshold-level calibration and false-decision checks.

## Process lesson and human decisions

The first queue read accidentally came from the unrelated assessment checkout and pointed to Q005. Re-reading the queue inside the fresh worktree corrected selection to Q002 before any canonical write. Worktree-local policy reads should be the first verification step after branch creation, not merely an assumed consequence of using a worktree.

Human review is requested on three choices: whether the evidence justifies keeping Q002 active; whether assistance-function reliability and minimal-data comparison should precede any schema revision; and how to consolidate draft PRs #1–#12 before merging another independent `main`-based research branch.

## Checks

- `python3 scripts/atlas.py index`: updated 10 generated files.
- `python3 scripts/atlas.py export notebooklm`: updated the research pack.
- `python3 scripts/atlas.py validate --strict`: 62 artifacts, 0 errors, 0 warnings.
- `python3 scripts/atlas.py eval`: 7 of 7 retrieval cases passed, including new Q002 case EV007.
- `python3 -m unittest discover -s tests -v`: 31 tests passed.
- `python3 scripts/atlas.py freshness`: 7 model-dependent sources classified; 0 current-system, 2 recent-system and 5 historical-system. S002's stale Fall 2023 GPT-4 metadata was corrected and its review moved to 2027-05-15; no evidential claim changed.
- JSON parsing passed for evaluation cases, research state and the generated graph; `git diff --check` passed.

