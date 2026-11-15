# R001 search strategy

Last searched: 2026-09-01
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

## 2026-11-15 delayed-transfer and current-system update

Question: which controlled studies materially change the answer about assisted performance, immediate independent performance and delayed novel independent transfer?

### Capabilities and bounded starting point

`research_capabilities` reported OpenAlex, Crossref and Docling available. Unpaywall lacked `UNPAYWALL_EMAIL`; Podcast Index, YouTube and OpenAI transcription credentials were absent; Zotero remained a runtime probe. OpenAlex OA, Apple Podcasts/RSS, native web, publisher pages and `pdftotext` were the declared fallbacks. Exa was reported as a separately configured MCP but was not exposed in the integrating lane.

Bounded Atlas queries retrieved [C001], [C002], [C009], [C011], [P001] and [P005]. The existing gap was stated before external search: no canonical current-system study combined separately scored assisted performance, immediate independent performance and delayed novel independent post-withdrawal transfer.

### Exact discovery queries

Native web, searched 2026-11-15 AEST:

- `2026 randomized controlled trial generative AI learning delayed unassisted posttest students GPT-5`
- `2026 generative AI tutoring independent learning post-withdrawal delayed transfer randomized study`
- `2025 2026 ChatGPT learning retention unaided test randomized trial corrected preprint`
- `site:osf.io OR site:aspredicted.org generative AI tutoring delayed transfer randomized preregistration 2026`
- `2026 randomized controlled generative AI learning delayed unaided independent test transfer students GPT-5`
- `site:arxiv.org 2026 generative AI assisted learning delayed retention unaided transfer randomized trial`
- `"generative AI" learning "delayed" "unaided" experiment 2025 2026`
- `"ChatGPT" "delayed post-test" learning randomized 2025 2026`

OpenAlex through `discover_sources`, filters 2025–2026:

- `generative AI assisted performance unaided retention delayed transfer randomized learning`
- `generative AI independent no-AI outcomes post-intervention learning transfer`
- `generative AI learning delayed retention unaided transfer randomized`
- `independent performance after generative AI assistance controlled trial`
- `ChatGPT delayed posttest learning retention transfer`

Crossref/OpenAlex identity resolution was run for `10.3389/fpsyg.2026.2029407`, `10.3389/fpsyg.2026.1906199`, `10.3390/app16188949` and `10.1080/00220485.2026.2695361`. The Syromiatnykov citation chain linked the current candidate to [S001], structured-tutoring work and active-learning/ICAP mechanisms; its forward citation path was still sparse.

### Social and podcast sampling

The future-facing debate was sampled for arguments and leads, not authority:

- LinkedIn activity `7491531674393079808` amplified the immediate Kestin result as “twice as much learning”; public replies correctly noted the absent delayed outcome and bundled hand-built intervention. The empirical link resolves to [S002].
- LinkedIn activity `7444752880089354241` framed unpractised AI capability as “borrowed competence” and linked to the Barcaui trial. The original DOI, not the post, supplied the empirical lead.
- X status `2063923537803354242` argued that deploying poorly understood AI tutors to disadvantaged learners was irresponsible. This is a governance position, not effect evidence.
- Sillage episode 17, Apple show `1896883763`, episode `1000786970936`, published 2026-08-31, distinguished production from practice and selective from indiscriminate dependence. The publisher page was hashed, but no verified timestamped transcript or original empirical result justified admission.

### Decisions

- Include [S063]: the publisher full text reports supervised unfamiliar immediate and delayed transfer after a 16-week attempt-first, compare-and-verify workflow. Treat as historical-system, nonrandomized configuration-level evidence.
- Include [S064]: the full open PDF directly separates current GPT-5.3 supported writing from supervised no-AI near transfer. Treat as fragile six-class quasi-experimental boundary evidence.
- Hold Wei, DOI `10.3389/fpsyg.2026.2029407`: useful outcome-state taxonomy and targeted Web of Science search map, but a purposive non-systematic review that missed [S063] cannot establish absence or completeness.
- Hold Bassner, DOI `10.1016/j.caeai.2025.100537`: Zenodo v6 record `23598858` supersedes v5 and changes analytic N to 281. Version-of-record/corrigendum identity, posttest assistance state, exact model and ITT sensitivity remain unresolved.
- Do not duplicate Barcaui or the current Eedi RCT already proposed in open PRs #8 and #10.
- Hold Oreopoulos: large one-week null/interaction boundary, but the cited registry is a later follow-on, the exact model is undisclosed and the four-item outcome has assistance-state and multiplicity limits.
- Hold Wu, Akgun and Toker, Qin, Sezgunsay and the Saudi vocabulary study for same-session horizons, simulated assistance, unverified withdrawal, unmatched packages or unclear model identity.

### Coverage boundary and failures

This remains a bounded weekly update, not the database-complete review. The intent-level gateway worked for capabilities, discovery, identity resolution, lawful staging and Frontiers fetches. Unpaywall, Podcast Index, YouTube and transcription remained unavailable. The MDPI gateway PDF and HTML fetches returned HTTP 403; the complete publisher HTML was inspectable through native web. Docling did not return a usable bounded extraction for the Frontiers PDFs, so lawful local copies were inspected with `pdftotext`. No full text or transcript entered Git.
