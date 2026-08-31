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
- [Tooling architecture](bridges/tooling.md)
- [Automation model](.harness/runbooks/research-cycle.md)
- [Configured schedules](.harness/automations.md)

## Use it

The harness has no third-party runtime dependencies and requires Python 3.11+.

```bash
python3 scripts/atlas.py status
python3 scripts/atlas.py query "assessment feedback transfer" --type claim --type principle
python3 scripts/atlas.py new claim worked-example-fading
python3 scripts/atlas.py index
python3 scripts/atlas.py validate --strict
python3 scripts/atlas.py eval
python3 -m unittest discover -s tests -v
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

Automated agents may research and open pull requests. They do not silently promote provisional claims, merge their own work, or overwrite a disputed belief. Human judgment remains the publication boundary.

## Source policy

Bibliographic metadata and original synthesis belong in Git. Copyrighted PDFs do not. Keep PDFs and annotations in Zotero (or another reference manager), using stable citation keys that match source notes. See [source intake](.harness/runbooks/source-intake.md).

## License

Original repository content is licensed under [CC BY 4.0](LICENSE). Third-party works retain their own copyright and are referenced, not redistributed.
