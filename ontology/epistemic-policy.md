# Epistemic policy

The atlas is designed to accumulate judgment without disguising uncertainty. Its unit of progress is not “a paper collected”; it is a traceable change in what we can responsibly claim, believe, design, or test.

## The publication ladder

1. **Source** — a work exists and has been inspected.
2. **Observation** — a result, argument, or limitation is extracted in context.
3. **Claim** — an atomic proposition is supported by one or more observations.
4. **Belief** — a revisable synthesis expresses our present view across claims and discourse.
5. **Principle** — a conditional design recommendation follows from beliefs and claims.
6. **Decision** — a concrete choice applies principles to a context and records trade-offs.
7. **Experiment** — an intervention tests whether the reasoning survives contact with reality.

Movement up the ladder is not automatic. A source can be valuable without supporting a general claim. A compelling belief can remain provisional. A principle that works in deliberate instruction can be wrong for time-critical performance support.

## Evidence dimensions

Appraise evidence as a profile, not a single magic score:

| Dimension | Question |
|---|---|
| Internal validity | Could bias or confounding explain the result? |
| Directness | Does the population, task, intervention, and outcome match our question? |
| Consistency | Do relevant studies point in a similar direction? |
| Replication | Has the result survived independent tests? |
| Magnitude | Is the effect large enough to matter? |
| Duration | Does it persist beyond the immediate session? |
| Transfer | Does it generalize to new tasks or settings? |
| Ecological validity | Does it survive realistic constraints and behaviour? |
| Technology directness | If the result depends on AI capability, does the evaluated system represent the product capability under consideration? |

Ratings are `high`, `moderate`, `low`, `unclear`, or `not-applicable`. Write the reason; do not average the dimensions into false precision.

## Technology-sensitive recency

Publication date and technology date are different evidence properties. Model-dependent AI results record the system/version, study period, temporal-relevance assessment and review date defined in [the technology recency policy](../research/technology-recency-policy.md).

Recent, methodologically weak evidence does not outrank an older strong design by default. Instead, syntheses show the trade-off: older work may provide stronger causal or mechanism evidence, while current-system work provides better technology directness. Product advice needs both where possible and must label extrapolation when no current-system anchor exists.

## Claim status and confidence

- `seed`: worth investigating; not ready for product use.
- `provisional`: supported enough to guide cautious exploration, with material uncertainty.
- `contested`: relevant credible evidence or interpretation conflicts.
- `established`: supported across appropriate methods and contexts; still bounded, never eternal.
- `retired`: superseded, disproven, duplicated, or no longer useful.

Confidence is `low`, `moderate`, or `high`. Status describes maturity; confidence describes our present confidence within the stated boundary conditions.

## Rules against evidence laundering

- A search result, model response, or secondary summary may discover a source but cannot support a claim.
- An abstract can establish relevance and basic study facts; it rarely establishes enough detail for a strong claim.
- Preprints are identified as preprints and are not described as peer reviewed.
- Reports from institutions are useful evidence but their incentives and methods remain part of appraisal.
- Citation count, prestige, and novelty do not substitute for methodological fit.
- Absence of contradicting evidence is not evidence of absence.
- Product analytics show behaviour in context; they do not automatically show learning or causality.
- A podcast, interview, talk, or practitioner essay defaults to perspective, argument, or testimony. Follow any empirical citation to its original work before using it as empirical support.
- Automatic transcripts and captions are navigation aids. Preserve timestamp, speaker, transcript provenance, and uncertainty; verify consequential quotations against publisher media or an official transcript.
- A book, standard, or institutional document may be authoritative for a definition, rule, or intellectual position without establishing a causal learning effect.
- Discovery metadata, citation graphs, and open-access resolvers establish identity and access paths—not methods, findings, or validity.

## Learning outcome hierarchy

Always distinguish:

1. **Assisted task performance** — output while support is present.
2. **Independent immediate performance** — output without support soon after practice.
3. **Delayed retention** — independent performance after time has passed.
4. **Near transfer** — application to structurally similar novel tasks.
5. **Far transfer** — application across materially different contexts.
6. **Real-world capability** — sustained, appropriately selected behaviour in authentic settings.

Engagement, completion, satisfaction, and speed are useful process measures. They are not interchangeable with learning.

## Belief revision

Every belief names counterarguments and what would change our mind. Revisions preserve history in Git and explain:

- the new evidence or reasoning;
- the old and new position;
- whether confidence, scope, or direction changed;
- implications for principles and decisions.

The atlas is intentionally opinionated. “Neutrality” that hides assumptions is less honest than an explicit position with falsifiers.
