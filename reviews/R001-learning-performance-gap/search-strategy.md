# R001 search strategy

Last searched: 2026-11-02
Coverage status: targeted current-evidence update; not yet database-complete.

## Concept blocks

### Generative AI

`"generative AI" OR "large language model*" OR LLM OR ChatGPT OR "reasoning model*" OR "multimodal model*" OR "AI agent*" OR "AI tutor*" OR "AI companion*"`

### Learning intervention

`learn* OR teach* OR tutor* OR instruction OR feedback OR scaffold* OR practice OR education OR student*`

### Outcomes distinguishing learning from performance

`retention OR transfer OR "independent performance" OR "unaided performance" OR posttest OR "post-test" OR delayed OR achievement OR "learning outcome*" OR dependency OR overreliance`

### Comparative design filter for the causal subset

`random* OR trial OR experiment* OR control* OR compar* OR "difference-in-differences" OR regression`

## Seed combined query

```text
("generative AI" OR "large language model*" OR ChatGPT OR GPT-4 OR "AI tutor*")
AND (learn* OR tutor* OR instruction OR feedback OR scaffold* OR practice)
AND (retention OR transfer OR unaided OR independent OR posttest OR delayed OR "learning outcome*")
```

Do not apply the comparative filter to the broad scoping search; use it for a narrower causal map.

## Technology-current stratum

Run the broad query with a rolling 18-month publication filter first, then inspect model/system version and data-collection date manually. Add current model-family names only after verifying them from authoritative release records; hard-coded brand names age quickly. Classify each included empirical source using `research/technology-recency-policy.md`.

Older GenAI records remain eligible for the historical map, mechanism contrasts, stronger designs and citation chaining. They cannot be the sole basis of a current product recommendation.

## Sources to search

- ERIC
- PsycINFO
- Scopus or Web of Science
- Education Source
- ACM Digital Library
- IEEE Xplore
- PubMed where relevant
- arXiv for clearly labelled emerging preprints
- backward and forward citation chains around [S001], [S002], and [S003]
- trial registries and institutional working-paper series for publication-bias signals

Google Scholar and web search are discovery aids, not the reproducible database search.

## 2026-08-31 targeted update

- Native web query: `2025 2026 randomized controlled trial generative AI learning later unaided assessment retention students`
- arXiv/publisher resolution: *Experimental Evidence on the Learning Impact of Generative AI*, arXiv:2607.08849v1
- Decision: include as [S015] after full-text methods/results inspection because it randomizes AI access and measures both immediate and approximately one-week unaided outcomes.
- Boundary: this targeted update does not complete the reproducible database search or publication-bias assessment. The queue item remains active.

## 2026-09-01 targeted controlled-outcomes update

Question: which post-2025 controlled studies report an AI-supported activity and an outcome after substantive AI support is removed?

### Providers and exact queries

- Native current web, 2026-09-01: `2025 2026 randomized controlled trial generative AI learning later unassisted delayed test students study`
- Native current web, 2026-09-01: `2026 controlled GenAI assisted programming later unassisted retest learning study`
- Native current web, 2026-09-01: `2026 generative AI learning "unassisted" post-test controlled study`
- Native current web, 2026-09-01: `"Less stress, better scores, same learning" PDF`
- OpenAlex through the Atlas gateway, 2026-09-01: `generative AI learning retention delayed posttest randomized`, filters 2025–2026, limit 10. Result payload was inspected in the run transcript; selected identities were staged in `.harness/inbox/candidates/2026-09-01/`.
- Direct arXiv identity/full-text resolution for arXiv:2604.18538v1 and arXiv:2605.15850v3.
- Crossref/OpenAlex DOI resolution for `10.1016/j.caeai.2025.100537`, `10.1016/j.ssaho.2025.102287`, and `10.1080/0142159X.2026.2652061`.

### Admission decisions

- Include [S023] after full-text inspection: a counterbalanced 22-person programming study reports both a large Copilot-assisted advantage and individual one-week retest; the absolute retest difference is null/inconclusive.
- Include [S024] after full-text inspection: a controlled access-timing study reports learning-phase behaviour and an immediate unassisted test. Treat as high risk of bias because assignment was by workshop, zero scorers were excluded, gender was imbalanced and clustering was not modelled.
- Include [S025] after full-text inspection: a registered four-hospital South African RCT reports performance after a ChatGPT-permitted patient encounter and a later compulsory summative measure. Its strongest result is an authentic immediate null; the later randomized group contrast is underreported.
- Hold Bassner et al., DOI `10.1016/j.caeai.2025.100537`: the CC BY identity, abstract and public analysis dataset were verified, but publisher full text returned a robot challenge and the metadata API exposed no article body. Do not admit until the full methods are inspected.
- Hold Barcauí, DOI `10.1016/j.ssaho.2025.102287`: the 45-day randomized retention result is highly relevant, but lawful publisher and SSRN full text could not be inspected in this pass.

### Coverage boundary

This was a deliberately bounded live update, not an exhaustive database search. It sampled null, adverse/inconclusive, positive-policy and authentic-performance results, admitted the three-source maximum, and preserved access failures. No meta-analysis, RoB 2 adjudication, trial-registry sweep or publication-bias assessment was completed.

## Required search log

For every database: platform, full query, filters, date searched, result count, export filename, and deduplication count. Store citation metadata in Zotero and screening decisions in `screening.csv`.

## 2026-11-02 delayed-outcome and risk-of-bias pass

Question: what changes when held delayed/null candidates are inspected and one named result per included comparative study receives a provisional formal bias appraisal?

### Providers and exact queries

- Atlas OpenAlex/Crossref discovery gateway, 2026-11-02: `generative AI learning delayed unassisted randomized retention transfer`, years 2025–2026, limit 10.
- Atlas OpenAlex/Crossref discovery gateway, 2026-11-02: `AI assisted learning independent performance after assistance removed randomized`, years 2025–2026, limit 10.
- Atlas OpenAlex/Crossref discovery gateway, 2026-11-02: `generative AI programming retention unassisted controlled experiment`, years 2025–2026, limit 10.
- Native web, 2026-11-02: `2025 2026 randomized generative AI learning delayed unassisted outcome` and exact-title/DOI resolution for Barcauí, Wiles and Bassner.
- Forward citation chains through OpenAlex for [S001] (`W4411627694`) and [S002] (`W4411505840`), 20 citing records inspected per seed.
- Public-discourse sampling: Hamsa Bastani's stable LinkedIn activity `7439636450142384128` and APA *Speaking of Psychology* episode 389 were used as perspective and discovery leads only; empirical claims were followed to original studies.

### Capability and fallback log

The project gateway exposed Crossref and OpenAlex resolution, candidate staging, lawful fetch and citation exploration. Unpaywall credentials, Podcast Index, YouTube and OpenAI transcription were unavailable; Exa was described as a separate connector but was not registered in this runtime. Zotero's local API was unavailable. Docling extraction timed out twice, so publisher HTML and `pdftotext` were used against lawfully fetched or author-hosted files. The APA episode identity was preserved by canonical episode number and publisher URL because feed/GUID resolution failed.

### Admission decisions

- Include [S060] after inspecting the published open article: a randomized 45-day adverse retention result, retained as a narrow low-confidence claim because 35 of 120 outcomes were missing and comparator compliance was unmonitored.
- Include [S061] after inspecting the complete author manuscript and final publication identity: large GPT-4-assisted gains with no immediate unaided knowledge advantage, bounded by high missing-outcome risk and a historical March–April 2024 system.
- Continue to hold Bassner et al., DOI `10.1016/j.caeai.2025.100537`: the lawful Zenodo v4 reproducibility package exposed tasks, data, exclusions and analysis code, but the version of record was blocked. The package shows 452 raw to 275 analytic participants, no delayed outcome, no located preregistration and no exact model identity. Those boundaries and 39.2% exclusions prevent admission from the package alone.
- Hold Kreijkes et al., DOI `10.1016/j.compedu.2025.105514`, as a future three-day school-outcome lead; its GPT-3.5 intervention is historical and full-text access was not resolved in this pass.
- Hold Liu et al., DOI `10.26300/y3f8-vh05`, for a later institutional-transfer update; low tutor uptake and section-level allocation do not answer the present assisted-versus-independent outcome question cleanly.
- Reject Alam et al. from canonical admission in this pass: the small `N=13` exploratory sample is too fragile to change the answer.
- Do not duplicate current-system sources already admitted on open draft PR #7. The branch separation is a publication-state boundary, not evidence that those records do not exist.

### Coverage boundary

This was a bounded update with three gateway searches, two seed citation chains, targeted full-text resolution and provisional result-level appraisal. It did not complete ERIC, PsycINFO, Scopus/Web of Science, trial-registry or publication-bias searches. Two of the three staged scholarly candidates were admitted; a third source was not manufactured to fill the cap.
