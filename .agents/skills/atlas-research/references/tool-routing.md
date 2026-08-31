# Research tool routing

Select tools by research stage and authority. More tools do not make a stronger chain.

| Need | Start with | Then verify or inspect with | Do not infer |
|---|---|---|---|
| Current web or unfamiliar field | Native web search | Exa for semantic alternatives; original publisher/source | Search synthesis is evidence |
| Scholarly work | `discover_sources` with `lane=scholarly` | `resolve_source` with `lane=scholarly`, `explore_citations`, original full text | Metadata or abstract establishes findings |
| Existing personal library | `search_zotero` | Attachment/annotation and original document | A saved item was fully inspected |
| PDF, report, EPUB, slides | `fetch_lawful_document` when remote, then `extract_source` with `kind=document` | Original layout, pages, tables, notes, methods | Extracted Markdown preserves all meaning |
| Podcast | Native web/Exa or `discover_sources` with `lane=podcasts` | `resolve_source` with `lane=media` for a transcript page; otherwise `lane=feed` | Speaker confidence establishes empirical truth |
| Video or lecture | Native web/Exa; `discover_sources` with `lane=videos` when configured | Publisher page, official captions, original audio/video | Automatic captions are exact |
| Public X or LinkedIn post | Native web/Exa; sample for argument quality, reach, novelty, or counterposition explicitly | `resolve_source` with `lane=web`, stable post ID, linked originals; signed-in Browser only when public retrieval is incomplete and authorized | Popularity, identity, or a social citation establishes truth |
| Web transcript or newsletter | Exa/native web | `resolve_source` with `lane=web`, canonical page, linked sources | Timestamp-like text proves a podcast identity |
| Local authorized media | Publisher transcript first | `transcribe_media`; verify uncertain spans against audio | ASR is a ground-truth quotation |
| Whole website/archive | Exa first | Firecrawl only when repeated site extraction is the bottleneck | Crawling increases source authority |
| Broad orientation | Deep Research or another synthesis agent | Re-run decisive searches and inspect originals | Generated synthesis can enter the evidence chain |

## Provider fallbacks

- Without Podcast Index credentials, podcast discovery uses Apple Podcasts Search and resolves the publisher RSS feed.
- Without `UNPAYWALL_EMAIL`, lawful-access lookup uses OpenAlex OA metadata and labels the fallback.
- Without YouTube credentials, use native web or Exa and inspect a selected public URL.
- Without Docling, PDFs use `pdftotext` and plain text uses a bounded reader. Record structure/table limitations.
- Without an OpenAI API key, use publisher transcripts or official captions. Do not download media merely to satisfy the pipeline.
- Without Zotero running, continue with canonical publisher sources and record that personal-library lookup was unavailable.

## Staging contract

Stage only normalized metadata, bounded summaries/excerpts, locators, hashes, rights, verification checks, and warnings. The local inbox is gitignored. Admission requires a source note, bibliography entry, content inspection, appropriate epistemic role, and repository validation.

The MCP surface is intentionally intent-level. The agent chooses a lane and epistemic role; the gateway performs transport and provenance. Use `candidate_inbox` with `action=stage|list|merge` for reversible candidate operations. The lower-level `research_gateway.py` CLI remains available for diagnostics.
