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

## Recommended next connections

### Zotero plus Better BibTeX

Use Zotero for PDFs, annotation, deduplication, collections, and stable citation keys. Export BibTeX to `sources/bibliography/references.bib`. A future Zotero MCP should begin read-only: search library, retrieve metadata, inspect annotations, and expose attachment availability. It should not promote claims or overwrite source notes.

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

Revisit these omissions when retrieval evaluation fails at scale, human review becomes a measured bottleneck, or a connector closes a specific provenance gap.
