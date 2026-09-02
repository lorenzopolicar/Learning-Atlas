# Technology recency audit — 2026-09-02

## Trigger

The user asked the Atlas to prefer recent AI papers because model capability has advanced substantially beyond GPT-4o-era systems.

## Change made

The harness now distinguishes publication recency from technology recency. Every source declares whether it is model-dependent, system-dependent, mechanism-oriented or model-independent. Model-dependent sources additionally record the system/version, study period, temporal-relevance assessment, review date and a transfer warning.

Search and synthesis now use a rolling 18-month technology-current stratum first. Older work remains eligible for stronger causal designs, mechanisms, delayed outcomes, nulls and citation chains, but it cannot silently become current product evidence.

## Baseline audit

`python3 scripts/atlas.py freshness` found seven model-dependent empirical sources:

- 0 `current-system`;
- 2 `recent-system` ([S023], [S024]);
- 4 `historical-system` ([S001], [S005], [S015], [S025]);
- 1 `unknown` because the exact system snapshot and study period still need recovery ([S002]).

This is an important limitation of the present Atlas. Several papers were published recently, but their interventions used GPT-4 or GPT-4o. Their mechanism and research-design value remains; their product-direct effect magnitude is not a 2026 forecast.

## Design lessons

1. Publication year is an unreliable proxy for technology freshness because study and peer-review lag can span model generations.
2. A rolling date filter alone is insufficient; exact model snapshot and data-collection period are first-class evidence fields.
3. “Current” is relative to the product capability and research question, not a universal leaderboard position.
4. Recency and methodological quality must remain separate dimensions. Newer preprints can be more technologically direct and less causally credible.
5. Mechanisms such as retrieval practice, feedback timing, reliance measurement and validity do not expire at model-release speed.

## Next action

Queue item 2 now seeks controlled studies using post-GPT-4o system generations with assisted and later independent outcomes. The next scout should try to add a credible `current-system` anchor, recover [S002]'s exact technology context, and explicitly report when no suitably rigorous current evidence exists.
