# Multisource passes and harness audit — 2026-08-31

## Audit conclusion

The Atlas had a strong epistemic schema and a capable transport layer, but its canonical corpus was paper-dominant and its MCP exposed too many provider-shaped tools. Worse, direct-page code had begun making epistemic decisions from superficial page features. The implemented redesign makes the system more agentic where judgment matters and more deterministic where reproducibility, safety and rights matter.

The stable architecture is:

```text
native web / Exa / scholarly graph / feeds / browser fallback
                            ↓
      bounded candidate envelope with identity + provenance
                            ↓
     agent appraisal, contradiction, source role, admission
                            ↓
 sources → claims / discourse → beliefs → principles → tests
```

## Real passes and iterations

### 1. Controlled empirical pass

The targeted query for post-2025 controlled GenAI studies with later unaided outcomes found [S015]. The full arXiv paper was fetched lawfully, hashed, extracted and read through methods, results, appendices and limitations. It changed the Atlas by adding [C009] and narrowing the stronger interpretation of [C001].

This pass caught a false transcript: `18:15:08` in the arXiv submission history triggered the old generic timestamp heuristic. The fix was not a longer exclusion list. Transcript extraction now runs only when the caller or a verified container says the source is media.

### 2. Public X and LinkedIn pass

Native web search located a high-reach X substitution thesis [S017] and a detailed LinkedIn orchestration thesis [S018]. Direct public pages supplied stable IDs and bounded content. Reach was an explicit sampling signal for a culturally visible argument, not evidence.

The first X parse repeated the false-transcript bug on the post time. The revised candidate records now have `social-post` type, platform locators, point-in-time warnings and only `discovery-lead` before agent appraisal. LinkedIn link extraction surfaced the linked OSF preprint. The OSF page returned 403 to automated inspection; ResearchGate and search metadata confirmed the DOI and abstract, but the post was admitted only as argument and discovery lead.

A repeat fetch changed the raw LinkedIn page hash because platform chrome and comments are dynamic. Candidates now retain both the raw retrieval hash and a normalized-content hash derived from the bounded primary description, allowing agents to distinguish transport drift from a changed post body.

Limitations that remain:

- public search cannot promise exhaustive or unbiased platform recall;
- deleted, private, login-only and some thread/reply context may require an authorized signed-in Browser session;
- engagement numbers are volatile and should not enter stable evidence fields;
- platform search ranking can overrepresent already prominent English-language voices.

There is no installed X or LinkedIn research plugin, and none is currently necessary. Native web/Exa plus direct normalization covers public discovery; the existing Browser is the controlled fallback for incomplete public pages. Sales-data plugins would not improve epistemic research.

### 3. Podcast pass

The HigherEdJobs episode [S019] resolved through its publisher page, RSS feed, GUID, enclosure and publisher transcript. Consequential observations retain speaker timestamps. The first generic transcript extraction returned timestamps with blank text because it processed HTML tags rather than visible text. HTML transcript extraction now passes through the page parser, with a regression test.

Podcast directories were again weaker than web search for semantic discovery. Their highest-value role is resolving a known series or feed. Publisher RSS and transcript identity are worth keeping deterministic; interpreting the guests' claims remains agent work.

### 4. Policy/framework pass

The current OECD–European Commission AI literacy framework [S016] resolved by DOI and was inspected from its CC BY 4.0 PDF. It contributes institutional guidance, definitions and an adaptable four-domain/19-competence architecture. It does not establish causal learning effects. Provider metadata called it a book; the agent admitted the inspected object as a report. That disagreement is a successful demonstration of the boundary.

## Source variety: before and after

| Measure | Before | After |
|---|---:|---:|
| Canonical sources | 14 | 19 |
| Social posts | 0 | 2 |
| Podcast episodes | 0 | 1 |
| Current AI-literacy framework in this pass | 0 | 1 |
| Controlled studies with immediate and delayed unaided outcomes in R001 | 1 | 2 |

The gap is not “more modalities at all costs.” The next portfolio priorities are learner testimony, books and intellectual history for Q003, datasets or validated measures for agency/calibration, and less selective or non-Western institutional contexts.

## Simplifications implemented

### MCP surface

The agent-visible MCP moved from 18 provider- and operation-specific tools to nine intent-level tools:

1. `research_capabilities`
2. `discover_sources`
3. `resolve_source`
4. `explore_citations`
5. `extract_source`
6. `fetch_lawful_document`
7. `transcribe_media`
8. `search_zotero`
9. `candidate_inbox`

The diagnostic CLI retains granular commands. This reduces agent tool-selection overhead without removing recovery paths. `atlas_mcp.py` fell from 314 to 279 lines and its advertised tools fell 50%. The gateway grew from 1,505 to 1,659 lines because it added social identity, outbound-link provenance and regression fixes; total script lines rose about 5%. Surface complexity fell even though correctness code increased.

The new Q003 retrieval eval initially failed for a deeper reason: evaluations ranked only claims, beliefs and principles. Discourse notes, questions, reviews and source frameworks could therefore never be asserted as retrievable. Each eval case can now declare its intended artifact types; existing product cases stay focused while Q003 explicitly tests questions, discourse and sources.

### Role allocation

| Deterministic code owns | Agents own |
|---|---|
| public-URL and SSRF safety | question framing and search strategy |
| rights basis, receipts and gitignored storage | relevance and portfolio selection |
| hashes and canonical DOI/GUID/platform IDs | epistemic role and authority |
| provider resolution and deduplication hints | methods appraisal and boundary conditions |
| bounded extraction and locators | contradiction and rival explanation |
| schema validation, indexes, graph and exports | claims, discourse, beliefs and agenda proposals |

Removed from script authority: timestamp-based source reclassification and automatic `expert-perspective` assignment. Provider metadata remains data that an agent may override with an explicit, inspectable reason.

### Agent roles

Claude already had specialist definitions. Matching project-scoped Codex agents now exist for research scouting, evidence extraction, contrarian review and synthesis. They are read-only by default; one integrating agent writes canonical artifacts. The active weekly, monthly and quarterly scheduled prompts were updated to use these roles and the intent-level MCP.

This follows the platform guidance that skills should be instruction-first unless deterministic behavior or external tools are needed, and that parallel agents are best for bounded read-heavy work while concurrent writes increase conflict. The Atlas research skill remains the reusable workflow; custom agents provide independent perspectives inside a run.

## What should remain scripted

- `atlas.py`: validation, bounded retrieval, IDs, indexes, graph, NotebookLM export and evals are deterministic integrity functions. Replacing them with agent judgment would weaken reproducibility.
- Rights-controlled fetch and local-path boundaries: these are safety properties.
- Identifier and feed reconciliation: canonical identity should not depend on prose compliance.
- Candidate storage limits: full text and transcripts must not leak into Git.

## What should become more agent-led

- Query reformulation, snowballing and deciding when a source lane is saturated.
- Sampling social discourse by explicit criteria such as reach, novelty, standing or counterposition.
- Following promising outbound links and deciding whether a linked original is decisive.
- Comparing effect heterogeneity instead of paper counting.
- Choosing source role, claim granularity and whether evidence changes wording, confidence, priority or nothing.
- Proposing reversible agenda changes from accumulated signals.

## Research tool stack

| Layer | Preferred tool | Why / boundary |
|---|---|---|
| Broad current discovery | Native web plus Exa | Strong for emerging work, public social posts, podcasts and semantic alternatives; results are leads |
| Scholarly graph and identity | OpenAlex plus Crossref | Citation chaining, DOI metadata, corrections and deduplication; full text still required |
| Lawful full text | Publisher/OA location plus rights receipt | Makes access basis and working-copy boundary explicit |
| PDFs and reports | Docling with `pdftotext` fallback | Navigation aid; original layout remains authoritative |
| Podcasts/video | Publisher page, RSS, official transcript/captions; optional transcription | Preserves series, GUID, speakers and timestamps; transcript confidence is not claim truth |
| Public social discourse | Native web/Exa, direct page, Browser fallback | Stable snapshot and linked originals; no exhaustive ranking guarantee |
| Personal library | Zotero local API | Useful for prior reading and annotations when running; a saved item is not inspected evidence |
| Human exploration | NotebookLM generated pack plus selected lawful originals | Excellent for questioning and conversation; never writes evidence back automatically |

No new plugin is required for the core loop. Google Drive would improve convenient NotebookLM-pack refresh if desired, but it should remain a mirror, not the canonical store. A dedicated Podcast Index credential, YouTube key or Unpaywall email should be added only when measured recall or access failures justify it.

## Skill decisions

Updated now:

- `atlas-research` now covers public social sampling, stable post provenance, intent-level MCP routing and explicit agent ownership of epistemic role.
- Its fourth eval exercises X, LinkedIn, podcast and linked-original separation.
- `consult-learning-atlas` now adds question/discourse/source lanes when Orqestra work turns on AI literacy, institutional purpose or human-AI capability, while retaining the smaller claim/belief/principle query for narrow implementation work.

Do not split yet:

- `atlas-media-intake`: two real podcast passes have revealed useful mechanics, but HTML and speaker parsing still need multiple publishers before becoming a separate stable skill.
- `atlas-discourse-mapper`: the X/LinkedIn/podcast process is promising; repeat it for a different controversy and add a counterposition-recall eval first.
- `atlas-source-reconciler`: inbox duplicates are visible but still low-volume; monthly synthesis can handle them.

## Remaining limitations and next tests

1. Re-run Exa inside a fresh trusted Codex and Claude session; this already-running task used native web.
2. Test social normalization on multi-post X threads, LinkedIn articles, deleted posts and pages that require a signed-in Browser.
3. Test media extraction across at least three more publishers, overlapping speakers and hour-long timestamps.
4. Add golden policy/table PDF fixtures; Docling can flatten figures, tables, footnotes and equations.
5. Observe whether nine intent-level tools improve real agent routing. Restore a low-level MCP tool only from repeated failure, not convenience.
6. Compare independent agent recommendations and log disagreement resolution; token spend is acceptable, but redundant consensus is not the goal.
7. Review the first three scheduled runs for worktree behavior, search breadth, write conflicts, validation failures, PR churn and human decision quality.
