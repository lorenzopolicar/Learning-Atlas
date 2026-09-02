---
{
  "id": "S021",
  "type": "source",
  "title": "Modeling the Joint Impact of Human and AI Metacognitive Sensitivity on Human–AI Collaboration",
  "citation_key": "li2026metacognitive",
  "source_kind": "journal-article",
  "epistemic_roles": ["empirical-study", "theoretical-argument"],
  "year": 2026,
  "url": "https://doi.org/10.1016/j.jmp.2026.102988",
  "status": "reviewed",
  "topics": ["human-ai-collaboration", "metacognition", "assessment-validity", "product-measurement"],
  "added": "2026-08-31",
  "last_reviewed": "2026-08-31",
  "technology_dependence": "mechanism-oriented",
  "access": "open"
}
---

# S021 — Human and AI metacognitive sensitivity

## Why it matters

The paper shows why raw confidence or calibration is not enough for combining human and AI judgments. What matters in its model is whether each agent's confidence discriminates its own correct from incorrect decisions—and whether the agents make different errors.

## Identity and provenance

- DOI: 10.1016/j.jmp.2026.102988; *Journal of Mathematical Psychology*, volume 129, article 102988
- Version inspected: complete open published manuscript, dated 24 April 2026
- Content inspected: full text, formal derivation, simulations, empirical validation and limitations
- Access and rights: CC BY
- Retrieval: gateway record `cand_0875a2fa7c54659d`; PDF SHA-256 `930e796291d481b9355a4cd170591a880824df20a8eea1f10dd881583f800849`
- Locator convention: numbered sections, propositions, figures and tables

## Study and model

- Construct: metacognitive sensitivity is the degree to which confidence separates correct from incorrect decisions. AUROC2 estimates the probability that a randomly chosen correct response has higher confidence than a randomly chosen incorrect response; 0.5 is chance and 1 is perfect discrimination.
- Formal contribution: a Bayes-optimal arbitration rule combines each agent's accuracy and metacognitive sensitivity. Under the model, above-chance sensitivity in either agent can enable complementarity.
- Empirical validation: the authors reused ImageNet-16H observations from 145 Mechanical Turk workers and predictions from 20 AI models. They constructed 2,900 human–AI dyads from 200 image-classification trials per person; the people did not collaborate live under the proposed rule.

## Findings

- The Bayes-optimal combination reached accuracy .826, compared with .781 for choosing the more confident answer, .784 for humans, .633 for AI and .709 for random choice in the analyzed dyads.
- The proposed rule achieved complementarity for 76.2% of dyads versus 44.1% for the maximum-confidence strategy.
- Human and AI errors were positively correlated (mean phi approximately .25). Treating errors as independent can overstate the opportunity for complementary performance.
- Accuracy, calibration, confidence level and metacognitive sensitivity are related but non-equivalent. A system can be confident without having confidence that meaningfully discriminates its errors.

## Limitations and boundary conditions

- The headline result is an analytical upper-bound-style result under a specified statistical model, not evidence that ordinary learners can learn or execute the Bayes-optimal rule.
- The empirical component constructs dyads after the fact from an image-classification dataset. It is not a live collaboration, educational intervention or longitudinal study.
- AUROC2 requires many correctness-labelled judgments and sufficient variation. It is a task-level estimate, not a stable person trait or a substitute for domain performance.
- Classification with known truth does not generalize automatically to creative, ethical, social or open-ended tasks. Confidence elicitation can also add burden or distort behaviour.

## Evidence profile

| Dimension | Rating | Reason |
|---|---|---|
| Internal validity | moderate | Clear formal assumptions and extensive constructed validation; no live intervention |
| Directness | moderate | Direct for arbitration theory, indirect for teachable learner capability |
| Consistency | unclear | One dataset family and derived dyads |
| Replication | low | No independent replication assessed in this pass |
| Magnitude | moderate | Model materially exceeded simpler combination rules in the analyzed data |
| Duration | low | Repeated trials without longitudinal follow-up |
| Transfer | low | No cross-domain or educational transfer |
| Ecological validity | low | Post-hoc image-classification dyads, not authentic AI-mediated work |

## Candidate claims

Supports the confidence-quality boundary in [C010](../../claims/C010-appropriate-reliance-has-distinct-components.md). It motivates measuring confidence discrimination only where the task and trial count make that inference defensible.
