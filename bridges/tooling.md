# Tooling architecture

Choose tools by epistemic role. No application should silently occupy discovery, evidence, synthesis, publication, and product decision-making at once.

## Active foundation

| Tool | Role | Authority |
|---|---|---|
| GitHub | Versioned publication, review, CI, issues, and pull requests | Canonical for atlas synthesis |
| Codex desktop schedules | Local recurring scout, synthesis, and direction-review jobs | May propose changes; cannot self-merge |
| Codex and Claude skills | Repeatable research, synthesis, and product-consultation workflows | Procedural guidance |
| Web and scholarly repositories | Discovery and original-source access | Original source is evidence; search output is not |
| Python harness | Schema, graph, bounded retrieval, export, and integrity evaluation | Deterministic repository guardrail |
| Atlas research gateway MCP | Normalized scholarly/media identity, citation checks, lawful extraction, locators, transcription, Zotero lookup, and reversible staging | Candidate metadata and provenance only |
| Exa MCP | Semantic discovery and targeted web retrieval | Discovery lead only |

## Recommended next connections

### Active research gateway

Codex reads `.codex/config.toml`; Claude Code reads `.mcp.json`. Both receive the same local `atlas-research` MCP, while Exa is configured as a separate discovery MCP. The local server is dependency-free and degrades explicitly:

- OpenAlex and Crossref work without credentials;
- Unpaywall uses `UNPAYWALL_EMAIL`, with a labelled OpenAlex fallback;
- Podcast Index uses its key/secret, with a labelled Apple Search plus RSS fallback;
- YouTube discovery uses `YOUTUBE_API_KEY`, with native web/Exa as fallback;
- Docling is preferred when installed, with `pdftotext`/plain-text fallback;
- OpenAI diarized transcription requires `OPENAI_API_KEY`; publisher transcripts and captions remain preferred;
- Zotero uses its read-only local API when the desktop app enables it.

Run `python3 scripts/research_gateway.py capabilities` to see the actual environment. Candidate records go to `.harness/inbox/` and never become canonical merely because a tool returned them.

### Zotero plus Better BibTeX

Use Zotero for PDFs, annotation, deduplication, collections, and stable citation keys. Export BibTeX to `sources/bibliography/references.bib`. The gateway now supports read-only local-library search; richer annotation and attachment retrieval should be added only after testing against the user's library. It must not promote claims or overwrite source notes.

### NotebookLM

Use the generated research pack for source-grounded human exploration, audio overviews, and adversarial questions across selected sources. It is not canonical because conversations and generated insights do not provide the atlas’s typed, versioned publication chain. Verify every useful discovery against original sources before writing it back.

### Google Drive

Connect Drive only if it materially improves NotebookLM refresh or collaboration. Mirror the generated pack and lawful source materials; never create a second editable master. A sync job must be one-way from a validated Git commit.

### Slack

Connect Slack when scheduled reports need a team audience. Send briefing and pull-request links, not full evidence dumps. Slack discussion becomes a question or decision record only through explicit curation.

### Product observability

PostHog and Sentry belong to the Orqestra feedback loop, not the literature pipeline. PostHog can support predeclared product experiments; Sentry can reveal operational failure. Neither establishes learning without a valid outcome and comparison.

## Workspace Agent option

A hosted Workspace Agent can later complement the local loop as a read-mostly scout and briefing interface. Give it GitHub read access, scholarly discovery, and optional Drive/Slack delivery. Require it to return a structured source candidate or open a draft PR; deny direct maturity promotion and merge. Keep local deterministic checks as the publication boundary.

Suggested agent contract:

- input: one atlas question, current claim IDs, and a source limit;
- output: search log, candidate sources, contradiction map, claim delta, and next action;
- tools: GitHub, primary-source web access, optional Zotero/Drive, optional Slack delivery;
- prohibition: no claim from snippets, no private learner data, no direct merge, no full-corpus prompt injection.

## Deliberate omissions

- A vector database is premature at the current corpus size; deterministic ranked retrieval is easier to inspect and test.
- An autonomous multi-agent swarm would increase review volume before the evidence model has proven its quality.
- A direct NotebookLM-to-Git write path would turn generated conversation into apparent evidence.
- Broad plugin installation without a defined role increases permissions and maintenance surface.
- Exa and Tavily are not installed together because their broad search/retrieval roles overlap.
- Firecrawl remains deferred until repeated whole-site or newsletter-archive extraction is a measured bottleneck.

Revisit these omissions when retrieval evaluation fails at scale, human review becomes a measured bottleneck, or a connector closes a specific provenance gap.
