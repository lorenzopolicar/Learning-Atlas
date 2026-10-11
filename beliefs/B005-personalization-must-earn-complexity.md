---
{
  "id": "B005",
  "type": "belief",
  "title": "Personalization must earn its complexity",
  "statement": "Personalization is justified only when learner evidence changes an intervention in a way that measurably improves outcomes over a strong, transparent default.",
  "status": "adopted",
  "confidence": "moderate",
  "topics": ["learner-modelling", "product-measurement", "scaffolding"],
  "derived_from": ["C003", "C007", "C033", "C034"],
  "counterarguments": ["Some personalization value appears in relevance, dignity, or access before outcome gains are statistically visible.", "Experiments may be underpowered for heterogeneous effects.", "A short null may reflect insufficient evidence accumulation or a poor implementation rather than a limit of adaptation."],
  "would_change_my_mind": ["A defensible non-outcome rationale that clearly outweighs model, privacy, and maintenance cost.", "Evidence that users consistently value harmless personalization even without learning gains."],
  "last_reviewed": "2026-10-11"
}
---

# B005 — Personalization must earn its complexity

## Position

Personalization is a causal claim: because the system knows something about this learner, a different action will help. It should be evaluated against simple policies, not assumed valuable because the output feels tailored.

## Why we believe this

Guidance effectiveness can reverse with expertise [C003], creating a real heterogeneity problem. Repeated learner-item evidence can make adaptive sequencing useful [C033], but a matched short-horizon trial found no incremental learning value [C034]. Learner states remain uncertain inferences [C007], so heterogeneity does not automatically justify model complexity.

## Strongest counterarguments

Outcome-only tests may miss belonging, accessibility, agency, and preference. The comparison must therefore include a multidimensional value and harm model, not just test scores.

## What would change our mind

We would accept personalization without measurable learning gain where a clearly stated access, dignity, safety, or agency benefit outweighs cost and risk.

## Implications

Begin with the least complex policy a human can inspect. Introduce model-driven adaptation only with an explicit decision, sufficient evidence horizon, evaluation plan, calibration and coverage checks, learner override, and fallback. Count maintenance, explanation, privacy, fairness and delivery burden alongside learning benefit.

## Revision history

- 2026-08-31: adopted as a founding belief.
- 2026-10-11: retained at moderate confidence; added direct positive and null comparative evidence and made the transparent baseline an incremental-value requirement.
