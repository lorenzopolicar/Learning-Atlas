# Multisource full passes — 2026-08-31

## Signal

The corpus now contains a real disagreement rather than a one-way case for pedagogical guardrails. A 2026 randomized preprint found that ordinary GPT-4o access improved immediate and one-week unaided learning in one time-held setting [S015, C009], while prior work found unrestricted access could damage later unaided performance [S001]. The design problem is therefore conditional: identify who is learning, offloading, or reallocating time under which task and incentive structure.

The future-of-learning pass also produced an explicit discourse map [N001]. A prominent substitution position argues for directing AI instead of learning the task [S017]; orchestration, institutional and policy positions instead emphasize judgment, outcome-specific assistance, agency and the capacity to evaluate and shape systems [S016, S018, S019]. The emerging phrase **capability sovereignty** is a draft design direction, not an adopted belief.

## Passes completed

| Pass | Search and route | Admitted | Epistemic effect |
|---|---|---|---|
| Controlled scholarly | Native web targeted 2025–2026 RCT search; arXiv full text and local bounded extraction | S015 | Added positive one-week counterevidence and provisional C009 |
| Public social discourse | Native web queries for AI education X and LinkedIn posts; direct public-page normalization; linked-original follow-up | S017, S018 | Added substitution and orchestration positions without empirical laundering |
| Podcast | Native web discovery; publisher transcript, RSS, GUID and timestamp resolution | S019 | Added outcome-specific and institutional expert positions with timestamps |
| Institutional framework | OECD DOI resolution; CC BY PDF; full report and annex inspection | S016 | Added a four-domain AI-literacy vocabulary as non-binding guidance |

No pass admitted more than three sources. Staged candidates remained in the gitignored inbox. The linked Wood OSF preprint was resolved to DOI 10.35542/osf.io/uthme_v1, but automated OSF full-text access failed; its empirical findings were not admitted through the LinkedIn post.

## Source portfolio effect

The canonical corpus moved from 14 sources with no podcast or social source to 19 sources including two public social posts, one podcast episode and one current institutional framework. Source variety improved, but important gaps remain: books, datasets, learner testimony, critical history, non-elite institutions and non-English discourse.

## Tool and provider result

- Public X and LinkedIn pages were retrievable without dedicated platform plugins. Stable status/activity IDs, publication times, authors, content hashes and snapshot warnings are now normalized.
- LinkedIn outbound-link extraction found the OSF preprint. Platform navigation was noisy, so same-site variants are now filtered.
- Repeat social fetches changed raw page-shell hashes; candidates now also record a normalized-content hash for more meaningful snapshot comparison.
- Publisher podcast transcript and RSS resolution worked. A second iteration exposed blank text from HTML transcript extraction; the parser now extracts visible speaker text and has a regression test.
- The arXiv page exposed a serious false-media bug: its submission time was treated as a transcript timestamp. The same happened to an X post time. Media detection is now gated by an explicit media container, and scripts no longer assign expert or empirical roles.
- Retrieval evals previously excluded discourse, questions, reviews and sources. Cases can now declare the typed surface they test, so source variety remains visible to downstream agents without crowding product-only contracts.
- OpenAlex/Crossref typed the OECD work as a book; the reviewing agent correctly admitted the inspected object as a report and institutional framework. This is the intended agent/script boundary.

## Product implication

Orqestra should model capability as conditional on assistance and intended outcome. “Can direct AI” should not silently replace “can act independently,” but neither should independent work be the universal gold standard. A capability event should make task purpose, assistance state, learner decisions, verification behavior, delay and recovery requirements inspectable.

## Next falsification steps

1. Complete the reproducible R001 database and citation-chain search; one positive preprint cannot settle heterogeneity.
2. Randomize assistance policies or incentives that encourage augmentation rather than infer their effects from learner-selected modes.
3. Develop [N001] with critical/historical scholarship, learner voices and concrete disciplinary cases.
4. Test capability sovereignty as a construct: what independent knowledge predicts error detection, responsible delegation and recovery when tools fail?
5. Observe the next three scheduled runs for agent disagreement quality, source-lane recall, duplicate handling and PR churn.
