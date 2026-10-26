---
{
  "id": "C002",
  "type": "claim",
  "title": "Pedagogical structure changes AI learning outcomes",
  "statement": "Generative AI interventions designed around instructional structure, guided interaction, and appropriate facilitation can improve learning outcomes, whereas unrestricted answer provision may not.",
  "status": "provisional",
  "confidence": "moderate",
  "topics": ["ai-tutoring", "scaffolding", "teacher-practice", "learning-vs-performance"],
  "supporting_sources": ["S001", "S002", "S005", "S014", "S024", "S058"],
  "contradicting_sources": [],
  "boundary_conditions": ["The studied interventions are bundled and context-specific.", "Evidence is stronger for short-term, near outcomes than long-term transfer.", "Teacher mediation, curriculum, and additional time may contribute materially.", "The direct access-timing study is a preprint with non-random workshop-level assignment and no policy ablation.", "The current-system metacognitive-feedback result is immediate, uses one-sided tests, and does not isolate the active feedback component."],
  "product_relevance": "Treat the pedagogical harness as the product, not as a prompt wrapped around a general chatbot.",
  "last_reviewed": "2026-10-26"
}
---

# C002 — Pedagogical structure changes AI learning outcomes

## Claim

The educational effect of generative AI depends materially on the surrounding pedagogical design. Structured, research-based tutor interactions and teacher-supported programmes have produced positive learning outcomes [S002, S005], while an unrestricted interface created a performance/learning gap that guardrails reduced [S001].

## Evidence and reasoning

The convergent pattern is promising across secondary mathematics, university physics, and an after-school programme in Nigeria. Earlier intelligent-tutoring research also suggests that step-linked feedback and task structure—not the mere appearance of conversation—can produce meaningful effects [S014].

[S024] narrows one potentially causal design dimension: its delayed-access policy beat always-on access on an immediate unassisted test. Because conditions were assigned by workshop and the adaptive reward was bundled, this strengthens the access-timing hypothesis without establishing the superiority of RL or any specific component.

[S058] supplies the first current-system component anchor in this chain. With complete solutions available only on explicit request, AI-only did not significantly reduce immediate unaided performance. Contextual metacognitive feedback reduced repeat complete-answer offloading and modestly improved the immediate test, while a symbolic effort reward changed neither outcome. Because the feedback combined several elements and the confirmatory tests were one-sided, this is a promising interaction-policy result rather than a validated recipe.

## Boundary conditions

Each intervention bundles multiple components. We cannot yet infer one universal “AI tutor recipe,” the independent contribution of the model, or durable far transfer. Domain structure, instructor role, dosage, and learner characteristics vary.

The mechanism claim is more durable than any effect magnitude. The chain now includes current-system GPT-OSS-120B evidence [S058] alongside GPT-4/4o-era systems and recent Mistral evidence, but no current-system study reports a delayed outcome. Current-model replications should test whether stronger generation changes the value of guardrails, explicit-request friction and feedback rather than assuming transfer.

## Counterevidence and uncertainty

Novelty, extra time, unusually intensive author-led design, aligned assessments and one-sided inference may inflate results. The AI-only null in [S058] also shows that access alone is not deterministically harmful. Independent delayed replications and component ablations are priorities.

## Product relevance

Learning products should expose and test their pedagogical policy: when to ask, hint, explain, model, retrieve, delay, and hand control back. Model capability alone is not a learning architecture.
