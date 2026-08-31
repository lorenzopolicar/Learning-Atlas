# Research pipeline smoketest — 2026-08-31

## Purpose

Exercise the research harness through real scholarly and podcast sources, then test mixed-source retrieval and degraded capability paths. The aim was not to manufacture new Atlas claims. It was to learn where agents lose identity, provenance, epistemic boundaries, or momentum before scheduled research begins.

## Capability snapshot

| Capability | Result | Route used or expected fallback |
|---|---|---|
| Semantic web discovery | Configured | Exa is a separate project MCP; native web remains the discovery fallback |
| Scholarly discovery and graph | Live | OpenAlex |
| DOI and update verification | Live | Crossref |
| Lawful-access resolution | Degraded | OpenAlex metadata; `UNPAYWALL_EMAIL` was unset |
| Podcast discovery | Degraded | Apple Podcasts plus native web; Podcast Index credentials were unset |
| Podcast identity and transcript | Live | Publisher page, RSS, Podcasting 2.0 transcript tag |
| YouTube discovery | Degraded | Credential was unset; gateway directed the agent to Exa/native web plus direct inspection |
| Document extraction | Live | Docling 2.123.1, with `pdftotext` as fallback |
| Media preparation | Live | `ffmpeg` and `yt-dlp` were present, subject to rights and platform terms |
| Speech-to-text | Degraded | `OPENAI_API_KEY` was unset; publisher transcript remained preferred |
| Personal library | Unavailable at runtime | Zotero local API was not running |

Full text, fetched documents, transcripts, and normalized candidates remained in the gitignored `.harness/inbox/`. None was admitted merely because the pipeline could retrieve it.

## Iteration 1 — scholarly source from question to bounded extraction

Question-shaped query: `generative AI tutoring delayed retention independent performance` for 2024–2026.

Selected source:

- *Beyond the “Wow” Factor: Using Generative AI for Increasing Generative Sense-Making*
- DOI `10.1007/s10648-025-10039-x`
- normalized candidate `cand_ce680b1b39030a36`

Flow exercised:

1. OpenAlex discovery returned a relevant delayed-follow-up study.
2. Crossref verified the DOI, bibliographic identity, and update relationships.
3. The gateway merged provider records, used the DOI as the stable candidate identity, and recorded the OpenAlex lawful-access fallback.
4. A publisher-open CC BY PDF was fetched only after an explicit `publisher-open-access` rights basis and stored with a hash and receipt.
5. Docling extracted a bounded ten-page navigation copy. The original PDF remained authoritative for layout, tables, notes, methods, and quotations.
6. The candidate was staged, not admitted. No claim or confidence changed during this smoke test.

Defects exposed and corrected:

- Provider-specific identifiers initially fragmented one DOI into two candidates. Canonical DOI, GUID, ISBN, or platform identity now wins over provider IDs.
- Crossref JATS tags leaked into summaries. Metadata markup is now stripped.
- Initial Docling Markdown contained embedded base64 images. The gateway now requests placeholders and sanitizes residual embedded-image markup.
- The first Docling invocation used an obsolete command form. The installed CLI is probed through its current `convert` interface with explicit page and OCR bounds.

## Iteration 2 — podcast from discovery lead to timestamped provenance

Question-shaped query: conversations about AI, teaching, and what remains worth learning.

Selected source:

- HigherEdJobs Podcast, *S5 Ep91: Teaching With AI, Part 1: Navigating the New Era of Human Learning*
- publisher episode GUID `b1dbc6f1-1bbc-4423-ad20-2276da7fcc4d`
- normalized candidate `cand_770205244a52fe1c`

Flow exercised:

1. Apple Podcasts search was tested and found to be too broad for niche semantic discovery. Native web located a promising publisher transcript; the directory is better used to resolve known series than to rank ideas.
2. Direct page inspection recorded canonical page, date, series, duration, content hash, named speakers, and bounded timestamp excerpts.
3. The page’s RSS discovery link resolved to `https://feeds.transistor.fm/the-higheredjobs-podcast`.
4. Feed matching found the exact episode, media enclosure, GUID, and Podcasting 2.0 publisher transcript.
5. Direct-page and RSS records merged without losing timestamp locators or source-specific verification records.
6. The raw publisher transcript was parsed into 21 speaker-labelled turns. A smoke request for three excerpts returned three bounded turns rather than the full transcript.

Defects exposed and corrected:

- Feed search discarded the short but meaningful term `AI`; query tokenization now preserves it while removing actual stop words.
- Speaker markers containing spaces inside parentheses were missed; timestamp parsing now accepts them.
- Page chrome produced false speaker names; normalization and JSON-LD parsing were tightened.
- Visible date, duration, RSS discovery links, and generic JSON-LD episode metadata were not initially retained.
- The transcript CLI did not expose excerpt and segment bounds. Both CLI and MCP now do.
- A warning that content had not been inspected survived after direct inspection. Merging now removes superseded warnings.
- Plain publisher transcripts initially returned speaker labels without the following words. They now return bounded speaker, time, and text segments.
- A pre-feed direct candidate can remain beside the merged GUID candidate. Staging now reports possible duplicate identities so a monthly review can reconcile, not silently delete, them.

Epistemic result: this source is `expert-perspective` and a `discovery-lead`. It can shape questions, design taste, and normative tensions. Any consequential empirical statement still has to resolve to the original study. The transcript is a navigation surface; audio is authoritative for consequential quotations.

## Iteration 3 — mixed retrieval and degraded paths

The local query `human AI collaborative capability independent capability assessment` returned a bounded eight-artifact set led by `C008`, `B004`, `C001`, `P005`, and `B001`. This confirmed that an agent can begin from existing Atlas reasoning instead of rediscovering the whole field.

Failure-path checks then confirmed:

- a `127.0.0.1` research URL is refused before fetch, protecting the public web tools from SSRF;
- missing YouTube credentials produce the precise Exa/native-web fallback;
- missing speech-to-text credentials produce the publisher-transcript/captions fallback;
- unavailable Zotero produces an actionable local-API instruction;
- the MCP initializes, lists tools, and executes a capability call without network access;
- candidate validation rejects full text or full transcript fields even when nested;
- lawful document fetching refuses calls without an explicit rights basis.

This is the desired degradation model: name the missing capability, preserve the research question, suggest the next-best route, and never lower the evidence standard invisibly.

## Process changes adopted

1. **Discovery and resolution are separate.** Native web/Exa find possibilities; canonical APIs, publisher pages, feeds, and original documents establish identity and provenance.
2. **All modalities enter one candidate envelope.** Papers, reports, books, datasets, pages, podcasts, and videos share identity, creator, date, access, provenance, locator, epistemic-role, verification, and warning fields.
3. **Staging is reversible.** Agents can accumulate and deduplicate candidates without expanding the canonical knowledge graph.
4. **Admission is a judgment gate.** A source note, content inspection, epistemic role, bibliography entry, and strict validation are still required.
5. **Capabilities are runtime data.** Research begins with a capability report so provider fallbacks become part of the briefing.
6. **Agenda signals are outputs.** A useful source may narrow, split, or deprioritize a question even when it supports no new claim.
7. **Tool accumulation has a threshold.** Improve the gateway or current skill after repeated evidence; add a provider only when it closes a recurring, measured bottleneck.

## Skill decisions

Updated now:

- `atlas-research`: stable end-to-end workflow for multimodal discovery, canonical verification, bounded extraction, source-role assignment, staging, evidence admission, and reporting.
- Three eval prompts now cover a scholarly delayed-learning question, a podcast/normative question, and a mixed-source Orqestra question.

Candidates to split into their own skills only after repeated runs:

- `atlas-agenda-steward`: quarterly signal aggregation and reversible programme transitions;
- `atlas-contradiction-hunter`: forward/backward citation chaining around a disputed claim;
- `atlas-media-intake`: only if publisher-feed-transcript reconciliation remains a frequent independent task;
- `atlas-source-reconciler`: only if inbox duplicate and correction handling becomes too complex for monthly synthesis.

The deterministic gateway remains an MCP rather than a skill because identity normalization, URL safety, hashing, rights receipts, and provider calls should not depend on prompt compliance.

## Limitations and next falsification steps

- Exa is configured at project level but was not available inside the already-running task; verify it in a fresh trusted Codex and Claude session.
- Podcast Index, YouTube Data, Unpaywall direct lookup, OpenAI transcription, and Zotero were not live-tested because their credentials or process were absent. Each degraded path was tested.
- Apple Podcasts is a weak semantic discovery engine. Compare native web and Exa recall on the three skill eval prompts before deciding whether Podcast Index credentials add enough value.
- Speaker extraction is heuristic. Test at least three other publishers, overlapping speech, multiword names, and hour-long timestamps before treating the parser as mature.
- Docling extraction is a navigation aid and can flatten meaning in tables, figures, equations, footnotes, and appendices. Add golden-file tests for methods-heavy papers and policy PDFs.
- The gateway records possible duplicates but does not auto-delete or auto-admit. This is deliberate; add an explicit candidate lifecycle only after observing inbox volume.
- Automated skill A/B evaluation was not run in this turn: independent subagent execution was unavailable, and the local Claude CLI was not a viable baseline. The eval prompts and assertions are committed so later runs can be compared.
- Scheduled-task prompts were updated, but their real Git worktree, draft-PR, and Scheduled-inbox behavior must be observed over the first three executions. Review those runs for churn, source laundering, duplicate work, and useful agenda evolution.

## Review after the next three scheduled runs

Measure:

- unique candidates discovered, staged, rejected, reconciled, and admitted;
- percentage with canonical identifiers, correction checks, lawful-access basis, and precise locators;
- source-lane and population coverage without quota-filling;
- number of empirical claims first encountered in media and successfully traced to originals;
- claim changes, useful negative results, agenda changes, and Orqestra decisions informed;
- provider failure and fallback rate;
- time lost to parser/provider friction;
- PR churn, validation failures, and requested human decisions.

Keep a change only if it improves one of those outcomes without weakening provenance or epistemic control.
