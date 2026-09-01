# Learning Atlas

Learning Atlas is a living, opinionated knowledge system for designing AI-powered learning. It turns research, practical observation, and first-principles inquiry into traceable claims, revisable beliefs, product principles, and testable decisions.

Its central question is not merely whether AI helps someone finish a task. It is whether the person develops durable, transferable capability—and what an intelligent system must observe, do, and withhold to make that more likely.

## The knowledge chain

```text
Sources -> Claims -> Beliefs -> Principles -> Decisions -> Experiments
              ^          |          |              |
              +----------+----------+--------------+
                    revision from new evidence
```

These layers are deliberately separate:

- **Sources** record what was studied, by whom, and under which conditions.
- **Claims** are atomic, bounded propositions supported or challenged by sources.
- **Beliefs** are our current synthesis. They are useful, explicit, and revisable.
- **Principles** translate evidence and belief into guidance for learning-system design.
- **Decisions** explain why a product or research choice was made at a point in time.
- **Experiments** try to falsify claims, beliefs, and product assumptions.
- **Discourse notes** hold philosophical, historical, and critical perspectives without mislabelling them as empirical evidence.

## Start here

- [Project instructions](AGENTS.md)
- [Epistemic policy](ontology/epistemic-policy.md)
- [Research agenda](research/agenda.md)
- [R001: Learning versus performance in AI-assisted learning](reviews/R001-learning-performance-gap/protocol.md)
- [Current beliefs](indexes/beliefs.md)
- [Design principles](indexes/principles.md)
- [Orqestra bridge](bridges/orqestra.md)
- [Orqestra AI-mediated stewardship design brief](bridges/orqestra-ai-mediated-stewardship.md)
- [E001 implementation-ready pilot package](experiments/E001-ai-mediated-stewardship-probe/pilot-package.md)
- [Tooling architecture](bridges/tooling.md)
- [First end-to-end pipeline smoketest](research/process-lab/2026-08-31-research-pipeline-smoketest.md)
- [Multisource passes and harness audit](research/process-lab/2026-08-31-multisource-passes-and-harness-audit.md)
- [First supervised multi-agent proving cycle](research/process-lab/2026-08-31-supervised-agent-cycle-1.md)
- [E001 product-contact pass](research/process-lab/2026-09-01-e001-product-contact.md)
- [Automation model](.harness/runbooks/research-cycle.md)
- [Configured schedules](.harness/automations.md)
- [How to work with the Atlas](guides/using-learning-atlas.md)

## Use it

The harness has no third-party runtime dependencies and requires Python 3.11+.

```bash
python3 scripts/atlas.py status
python3 scripts/atlas.py recent --limit 5
python3 scripts/atlas.py query "assessment feedback transfer" --type claim --type principle
python3 scripts/atlas.py new claim worked-example-fading
python3 scripts/atlas.py index
python3 scripts/atlas.py validate --strict
python3 scripts/atlas.py eval
python3 -m unittest discover -s tests -v
```

### Research gateway

Codex and Claude share a provenance-first MCP declared in `.codex/config.toml` and `.mcp.json`. Its nine intent-level tools discover, resolve, extract, trace, lawfully store, transcribe, search Zotero, and manage candidate envelopes. Public X and LinkedIn posts are handled as stable, snapshot-limited social sources; empirical links are followed to originals. The gateway never assigns evidentiary authority or admits a source—the reviewing agent does.

```bash
python3 scripts/research_gateway.py capabilities
python3 scripts/research_gateway.py discover works "AI tutoring delayed retention" --limit 5
python3 scripts/research_gateway.py resolve-paper 10.1038/s41598-025-97652-6
python3 scripts/research_gateway.py discover podcasts "AI education learning" --limit 5
python3 scripts/research_gateway.py resolve-feed https://publisher.example/feed.xml
python3 scripts/research_gateway.py resolve-media https://publisher.example/episode/transcript
```

OpenAlex and Crossref require no credentials. Optional provider variables are documented in `.env.example`. Full text, transcripts, media, and intermediate extractions stay in the gitignored `.harness/inbox/`; Git contains only lawful metadata, bounded excerpts, locators, and original synthesis.

Docling is an optional isolated extractor rather than a project dependency:

```bash
uv tool install docling
```

If it is absent, the gateway reports and uses its bounded `pdftotext` or plain-text fallback.

Create a source note using the closest profile:

```bash
python3 scripts/atlas.py new source example-study --source-profile empirical
python3 scripts/atlas.py new source example-interview --source-profile media
python3 scripts/atlas.py new source example-post --source-profile social
python3 scripts/atlas.py new source example-book --source-profile book
python3 scripts/atlas.py new source example-dataset --source-profile dataset
```

To create the human-readable NotebookLM pack:

```bash
python3 scripts/atlas.py export notebooklm
```

The generated pack is a portable reading and conversation surface. The repository remains the source of truth.

## Operating rhythm

- **Continuously:** capture promising sources and questions in the research queue.
- **Weekly:** scout a narrow question, admit at most three high-value sources, update claims, and publish a briefing.
- **Monthly:** synthesize accumulated evidence, seek contradictions, and propose belief/principle revisions.
- **Quarterly:** reassess the agenda and retire stale beliefs, weak questions, and product assumptions.

The programmes are continuity scaffolds, not a static syllabus. Signals, queue priorities, source lanes, and methods evolve weekly and monthly; material programme changes are recorded in [the agenda ledger](research/agenda-ledger.md) and require human review.

For complex passes, Codex can delegate independent read-heavy work to project-scoped research, evidence, contrarian, and synthesis agents under `.codex/agents/`; Claude has matching definitions under `.claude/agents/`. The primary agent remains responsible for comparing their outputs, editing the canonical artifacts, and running validation.

Automated agents may research and open pull requests. They do not silently promote provisional claims, merge their own work, or overwrite a disputed belief. Human judgment remains the publication boundary.

## Source policy

Bibliographic metadata and original synthesis belong in Git. Copyrighted PDFs do not. Keep PDFs and annotations in Zotero (or another reference manager), using stable citation keys that match source notes. See [source intake](.harness/runbooks/source-intake.md).

## License

Original repository content is licensed under [CC BY 4.0](LICENSE). Third-party works retain their own copyright and are referenced, not redistributed.
