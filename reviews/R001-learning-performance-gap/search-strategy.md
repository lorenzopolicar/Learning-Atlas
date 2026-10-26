# R001 search strategy

Last searched: 2026-10-26
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

## 2026-10-25/26 current-generation withdrawal and retention update

Question: which current-generation controlled studies report both AI-assisted activity and an outcome after substantive assistance is removed, and what design features change that relationship?

### Bounded retrieval and capabilities

- Atlas query: `current-generation controlled studies assisted later unassisted GenAI outcomes`, restricted to claims, principles, questions and reviews. This returned the existing C001/C002/C009/C011, P005, Q001 and R001 evidence chain before external discovery.
- Gateway capabilities: OpenAlex and Crossref available; Unpaywall unavailable because `UNPAYWALL_EMAIL` was unset; Podcast Index, YouTube and OpenAI transcription unavailable; Docling installed but returned no usable thesis extraction; Exa was configured separately but not callable in this run.
- Gateway/OpenAlex queries: `generative AI assisted performance delayed unassisted learning randomized retention`; `generative AI learning delayed posttest unassisted randomized controlled trial`; `ChatGPT retention transfer without AI experiment students`; `AI tutor delayed learning unassisted posttest randomized 2025`; `LLM cognitive offloading learning retention experiment`; and the exact title `AI Assistance Reduces Persistence and Hurts Independent Performance`. Searches used the 2025–2026 window where supported and limits of 5–15.
- Native web queries: `2026 LLM assistance "unaided test" experiment learning`; `2026 ChatGPT "48 hours" retention students experiment`; `2026 GPT-5 learning retention randomized trial students unaided`; and `2026 generative AI "subsequent test" without assistance experiment learning`.
- Exact-title/arXiv resolution and lawful publisher-open PDF fetches completed for arXiv:2604.04721v6, arXiv:2609.20143v1 and arXiv:2609.21194v1. Candidate staging remained separate from admission.

### Citation chain and lane sampling

- Backward chaining from Maier et al. surfaced Bassner, Bastani, Liu, Shen and Tamkin, and Rismanchian. Liu's forward-citation results were mostly conceptual or commentary work rather than delayed replications.
- The useful empirical chain was `Bastani / Barcauí / Shen and Tamkin -> Liu -> Maier`: answer-ready assistance shows an immediate withdrawal penalty, while explicit-request friction and contextual feedback produce a null/intervention boundary.
- Public professional discourse was sampled deliberately. Rohan Paul's LinkedIn post, stable activity ID `7477277198882590720`, amplified Rismanchian's large quasi-experiment and linked to the original; Peter Slattery's LinkedIn post, stable activity ID `7479927204328603648`, amplified Strömberg's observational longitudinal result. Both were discovery/perspective only.
- Podcast discourse was sampled through APA *Speaking of Psychology* episode 389 with Brooke Macnamara. Its official transcript argues that the function and degree of offloading matter and recommends unaided self-testing. Episode feed/GUID resolution failed, so it was retained as contextual perspective rather than admitted.

### Admission decisions

- Include [S057]: three randomized GPT-5 experiments show improved assisted performance followed by lower immediate independent accuracy after withdrawal; the latter two reduce important exclusion/interface confounds. Do not infer durability.
- Include [S058]: a preregistered current-system factorial trial preserves an AI-only null under explicit-request friction and shows that contextual metacognitive feedback reduces answer offloading and modestly improves an immediate unaided test. Do not infer which bundled feedback component is active.
- Include [S059]: a small pseudo-randomized programming study reports higher assisted coding scores and lower immediate/48-hour recall. Treat as a lower-confidence delayed acquisition signal, not accelerated forgetting or independent coding transfer.
- Hold Barcauí, DOI `10.1016/j.ssaho.2025.102287`: the randomized 45-day result remains highly relevant, but ScienceDirect and SSRN full-text endpoints returned robots/403 in the integrating lane. Indexed or agent-inspected text was not substituted for a stable lawful extraction.
- Hold Bassner et al., DOI `10.1016/j.caeai.2025.100537`: metadata and public Zenodo analyses were resolved, but the publisher article was blocked. The reported null is informative, while substantial attrition and post-treatment non-use exclusions require full-paper appraisal.
- Hold Autor et al., NBER working paper 35720: the official abstract reports a three-month patent-drafting RCT with later unaided redlining, but NBER/SSRN full text returned reset/403 responses.
- Hold Rismanchian et al., arXiv:2605.21629: large proctored-retention signal, but AI use is inferred from task susceptibility rather than observed or randomized.
- Hold the 2026 programming meta-analysis: its no-AI-assessment subgroup is null overall, but the search ends in 2025, heterogeneity is high and it collapses assistance designs and delays that matter to this question.
- Reject the 13-person programming thesis as too imbalanced and underpowered for claim revision; reject the nursing trial for this run because ChatGPT-3.5 is bundled with peer discussion, guidelines, instructor correction and hands-on practice.

### Failures and coverage boundary

The broad native web search hung once and was terminated; focused searches succeeded. ScienceDirect and SSRN presented robot/CAPTCHA or 403 barriers and were not bypassed. Docling did not extract the thesis, so local `pdftotext` was used on the lawfully fetched document. Podcast feed resolution failed. This was a bounded update with at most three admissions, not a database-complete search, RoB 2 adjudication, trial-registry sweep or publication-bias assessment.

## Required search log

For every database: platform, full query, filters, date searched, result count, export filename, and deduplication count. Store citation metadata in Zotero and screening decisions in `screening.csv`.
