---
{
  "id": "Q004",
  "type": "question",
  "title": "When does learner-model personalization earn its complexity?",
  "question": "What incremental learning value does learner-model personalization add over a strong transparent sequence, for which learners and decisions, after model, delivery and measurement costs are counted?",
  "status": "open",
  "priority": "high",
  "topics": ["learner-modelling", "scaffolding", "product-measurement", "ai-tutoring"],
  "related_claims": ["C003", "C007", "C033", "C034"],
  "last_reviewed": "2026-10-11"
}
---

# Q004 — When does personalization earn its complexity?

## Why this matters

Orqestra can build increasingly rich learner models, but prediction quality is not the same as better instructional decisions. Personalization also creates calibration, privacy, fairness, explanation and maintenance costs.

## Scope and definitions

Compare transparent fixed or response-contingent rules, learner-controlled policies and model-driven adaptation while holding content, interface, feedback, exposure budget and assessment constant. Separate task selection, spacing, hint fading, answer access and presentation personalization rather than treating “adaptive” as one intervention.

## Current synthesis

Long-horizon sequencing can improve independent or delayed outcomes over credible fixed policies [C033], but isolated short-horizon difficulty adaptation can produce no added learning value [C034]. Learner state is probabilistic [C007], and expertise heterogeneity [C003] does not by itself prove that a complex model is the best policy.

## Next search and experiment

Pre-register a three-arm Orqestra-like trial: transparent fixed response rule, learner-model adaptive policy and learner-controlled/on-demand policy. Hold the tutor, content, feedback and exposure budget constant; power immediate independent, delayed and transfer outcomes; report state calibration, false promotion/hold, content coverage, burden and subgroup effects. Ablate learner-state features before attributing gains to the model.
