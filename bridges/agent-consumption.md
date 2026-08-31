# Agent consumption contract

Learning Atlas is a knowledge dependency, not an always-on prompt appendix.

## Retrieval contract

Agents begin with a concrete product question and receive at most 12 relevance-ranked artifacts or 6,000 characters. They then open only the claims, beliefs, principles, and source notes necessary for the decision.

```bash
python3 scripts/atlas.py query "<question>" --type claim --type belief --type principle
```

Each response should retain:

- artifact ID and maturity;
- the bounded proposition or recommendation;
- source relationships;
- boundary conditions and exceptions;
- falsifiers and relevant outcome timing;
- canonical repository path.

## Why retrieval is bounded

Loading the whole atlas would make growing knowledge compete with the code and user request for context. It would also privilege repeated wording over relevant evidence. Bounded retrieval keeps the corpus cumulative while the working context remains selective and inspectable.

## Coding-agent output contract

When atlas evidence influences a design, the agent should state:

1. product mode: learning, assessment, or performance support;
2. recommendation and atlas IDs;
3. relevant learner and context assumptions;
4. assistance, delay, and transfer implications;
5. observable falsifier or evaluation plan;
6. uncertainty that still requires judgment.

Do not treat an atlas principle as a mandatory code shape. Principles constrain reasoning; architecture still responds to the product context.

## Write-back contract

Observations from product work enter as an experiment or research question. They do not automatically change an atlas claim because production behaviour can be confounded, context-bound, and measured through proxies. Atlas edits occur in this repository under its review gates.
