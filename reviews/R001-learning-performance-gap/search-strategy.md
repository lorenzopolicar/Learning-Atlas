# R001 search strategy

Last searched: 2026-09-14
Coverage status: targeted current-evidence and progressive-assistance update; not yet database-complete.

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

## 2026-09-14 targeted progressive-assistance update

Question: which progressive-hint and attempt-before-answer policies have causal evidence in LLM tutoring?

### Providers, queries and citation chain

- Bounded Atlas query: `Does a post-feedback attempt and progressive assistance improve delayed independent learning?`, limited to claims and principles; freshness audit run before external search.
- Native current web: `2025 2026 randomized trial LLM tutoring progressive hints attempt before answer delayed independent learning`.
- Native current web: `site:arxiv.org LLM tutor hint progressive feedback randomized learning study 2025 2026`.
- Native current web: `2025 generative AI tutor Socratic hints versus answers experiment learning outcomes`.
- Native current web: `podcast AI tutoring productive struggle hints answers learning 2025 2026`.
- OpenAlex gateway, 2025–2026: `progressive hints attempt before answer generative AI tutor learning`; anonymous API returned HTTP 429.
- OpenAlex gateway, 2025–2026: `mastery based math LLM tutoring next attempt delayed test`; anonymous API returned HTTP 429.
- OpenAlex gateway, 2025–2026: `Socratic generative AI tutor direct answers randomized`; the query resolved multiple candidates but was noisy.
- Exact DOI/arXiv resolution and publisher full-text inspection for NBER `10.3386/w35621`, arXiv `2512.23633`, arXiv `2609.00584`, arXiv `2606.08807`, and SSRN `10.2139/ssrn.5040921`.
- Citation chaining followed S024 and S001 into guard-railed tutoring, the NBER paper's mastery and post-error references, LearnLM/Eedi's static-hint and human-tutoring comparators, and the current GPT-5.2 strict-withholding counterexample.
- Public LinkedIn activity `7432447285814329346` and the *My Robot Teacher* episode of 3 September 2026 were sampled as practitioner/product perspectives; their empirical claims were followed to originals and neither was admitted.

### Admission decisions

- Include [S042] after complete NBER PDF inspection: individually randomized 2 × 2 × 2 field experiment with 6,997 middle-school learners, strong post-mistake recovery evidence and only a marginal 3.2-point one-week gain on one practiced mastery item.
- Include [S043] after complete arXiv PDF inspection: static hints versus interactive support after a wrong answer, with human versus human-supervised LearnLM session randomization. Immediate correction improved, but human pacing edits and no delayed outcome limit the claim.
- Include [S044] after complete arXiv PDF inspection: a small current-system same-model comparison where strict no-answer Socratic tutoring produced lower immediate gains, lower helpfulness and more disengagement than unrestricted answers.
- Hold Blasco and Charisi, DOI `10.2139/ssrn.5040921`: direct randomized Socratic-versus-non-Socratic null lead, but SSRN full text returned HTTP 403 and secondary summaries do not support admission.
- Hold Bassner et al., DOI `10.1016/j.caeai.2025.100537`: direct calibrated-hint null remains unavailable as full text.
- Reject Heickal and Lan, arXiv `2606.08807`, for this claim: full paper inspected, but feedback exposure was conditional and the reported analyses are associative; outcomes are repeated submission performance, not independent learning.
- Reject the LinkedIn and podcast candidates as empirical evidence: both express useful productive-friction positions but add no inspectable causal result beyond the originals.

### Coverage boundary

This was a bounded falsification pass, not a complete systematic search. No admitted study isolates the full P001 sequence, and only S042 measures beyond the same session. Database exports, formal RoB 2 adjudication and publication-bias assessment remain open.

## Required search log

For every database: platform, full query, filters, date searched, result count, export filename, and deduplication count. Store citation metadata in Zotero and screening decisions in `screening.csv`.
