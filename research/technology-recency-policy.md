# Technology recency policy

AI capability changes faster than most publication and evaluation cycles. A recent publication can still evaluate an old model, while an older learning-science result can remain highly relevant. The Atlas therefore tracks **technology dependence**, not paper age alone.

## Default preference

For empirical claims whose direction or magnitude plausibly depends on model capability, interface, tools, retrieval, multimodality, latency or agent behaviour:

- search the rolling 18-month window first;
- prefer studies that identify the exact system/model snapshot and data-collection period;
- prefer the newest credible post-GPT-4o system generations for product-direct evidence;
- retain older studies when they offer stronger causal design, delayed outcomes, replication, a useful null, or a mechanism that newer work has not tested;
- never substitute novelty, benchmark strength or a preprint date for internal validity and outcome relevance.

Search publication date and technology date separately. “Published in 2026” is not enough if the intervention used a materially older system.

## Technology-dependence classes

- `model-dependent`: the observed effect plausibly changes with the model or model-enabled product capability. Requires a technology context and recurring freshness review.
- `system-dependent`: the argument or observation concerns the surrounding AI ecosystem, interface, policy or practice, but does not estimate a model-specific effect.
- `mechanism-oriented`: the source primarily informs a mechanism or measurement construct expected to transfer across model generations; technological differences remain a boundary.
- `model-independent`: the source concerns learning, measurement or institutions without relying on an AI system's capability.
- `unclassified`: temporary intake state allowed only while a source remains `seed`.

## Required model-dependent context

Record:

- system and exact version or an explicit “not reported”;
- data-collection or study period, not merely publication year;
- the date temporal relevance was assessed;
- `current-system`, `recent-system`, `historical-system`, or `unknown`;
- a technology-specific review date;
- what is likely to transfer and what requires current-system replication.

`current-system` means representative of the current product capability being considered, not “the globally best model.” `recent-system` is still informative but should not be the sole product-direct anchor. `historical-system` can support mechanisms and longitudinal interpretation but cannot alone justify current product behaviour.

## Synthesis and product rules

- Separate model-contingent effects from durable learning or measurement mechanisms.
- A product-direct recommendation should include at least one current-system anchor or explicitly label the transfer from older systems as a hypothesis.
- When current evidence is methodologically weaker than older evidence, show both; do not hide the trade-off.
- Re-run the freshness register during monthly synthesis, quarterly review, and after a material capability shift.
- Use `python3 scripts/atlas.py freshness` to expose the current register and overdue reviews.

This policy is a search and interpretation prior, not a ban on older work.
