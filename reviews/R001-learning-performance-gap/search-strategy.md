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

## 2026-11-09 current-system transfer update

Question: does any current-generation controlled study jointly measure a delayed, novel, independent outcome after substantive AI assistance is withdrawn?

### Bounded Atlas retrieval

The Atlas query for Q001 returned [C001], [C002], [C009], [C011] and [P005]. `research_gateway.py capabilities` reported OpenAlex and Crossref available; Unpaywall, Podcast Index and OpenAI transcription unavailable; Exa described as a separate MCP but not exposed in this runtime. The intent-level Atlas MCP tools were also absent, so the repository gateway plus native web were used.

### Exact scholarly queries

- `generative AI delayed novel transfer independent performance randomized`
- `large language model assistance later unassisted transfer learning controlled experiment`
- `ChatGPT AI tutor delayed retention novel task posttest randomized students`
- `GPT-5 learning transfer without AI delayed test experiment`
- `generative AI later unassisted posttest new task transfer experiment student`
- `AI tutoring four week follow-up conceptual knowledge randomized ChatGPT`

Filters prioritized 2025–2026 controlled studies, then manually verified model/version, study period, assistance state, delay and transfer distance. Native web added exact-title, registry, LinkedIn and podcast queries. Counts from heterogeneous native-web result pages are not reproducible and are not represented as database counts.

### Citation and registry chains

- 2025 Eedi/LearnLM exploratory RCT → `AEARCTR-0018079` → 29 October 2026 expanded report [S062].
- [S001] → NUMI March 2026 experiment → EdWorkingPaper/NBER report → `AEARCTR-0018678`; the registry describes a later follow-on and does not preregister the reported March pilot.
- Bassner DOI → Zenodo reproducibility package v5; its corrigendum changes the analytic sample and several results, so the stale v4 package cannot support admission.

### Public discourse and audio sampling

Stable LinkedIn activities `7502137944741302272` and `7509631823497498624` were inspected as competing practitioner framings. The first usefully distinguishes assisted from later independent performance; the second overstates durable harm. Leon Furze podcast episode 91 has Apple episode ID `1000770726396`, but no timestamped publisher transcript was available. No stable public X post added an original empirical lead. These records remain perspective or discovery material.

### Admission decisions and coverage boundary

Admit only [S062]. Hold the sport-skill RCT pending chronology clarification; hold Oreopoulos et al. pending model and registry resolution; hold corrected Bassner pending version-of-record/corrigendum inspection. Reject duplicated, indirect, bundled or inaccessible candidates for this cycle as recorded in `screening.csv`.

This remains a bounded targeted update, not the protocol's reproducible database search. No current-system study located here combined delayed, novel, independent post-withdrawal performance. No meta-analysis or publication-bias assessment was attempted.
