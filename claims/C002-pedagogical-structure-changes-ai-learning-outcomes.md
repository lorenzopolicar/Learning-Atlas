---
{
  "id": "C002",
  "type": "claim",
  "title": "Pedagogical structure changes AI learning outcomes",
  "statement": "Generative AI interventions designed around instructional structure, guided interaction, and appropriate facilitation can improve learning outcomes, whereas unrestricted answer provision may not.",
  "status": "provisional",
  "confidence": "moderate",
  "topics": ["ai-tutoring", "scaffolding", "teacher-practice", "learning-vs-performance"],
  "supporting_sources": ["S001", "S002", "S005", "S014", "S024", "S063", "S064"],
  "contradicting_sources": [],
  "boundary_conditions": ["The studied interventions are bundled and context-specific.", "Evidence is stronger for short-term, near outcomes than long-term transfer.", "Teacher mediation, curriculum, and additional time may contribute materially.", "The direct access-timing study is a preprint with non-random workshop-level assignment and no policy ablation.", "The delayed engineering-transfer study used deterministic post-baseline class allocation and historical GPT-4o.", "The current GPT-5.3 writing study used only six intact classes and bundled delegation limits with compulsory reflection."],
  "product_relevance": "Treat the pedagogical harness as the product, not as a prompt wrapped around a general chatbot.",
  "last_reviewed": "2026-11-15"
}
---

# C002 — Pedagogical structure changes AI learning outcomes

## Claim

The educational effect of generative AI depends materially on the surrounding pedagogical design. Structured, research-based tutor interactions and teacher-supported programmes have produced positive learning outcomes [S002, S005], while an unrestricted interface created a performance/learning gap that guardrails reduced [S001].

## Evidence and reasoning

The convergent pattern is promising across secondary mathematics, university physics, and an after-school programme in Nigeria. Earlier intelligent-tutoring research also suggests that step-linked feedback and task structure—not the mere appearance of conversation—can produce meaningful effects [S014].

[S024] narrows one potentially causal design dimension: its delayed-access policy beat always-on access on an immediate unassisted test. Because conditions were assigned by workshop and the adaptive reward was bundled, this strengthens the access-timing hypothesis without establishing the superiority of RL or any specific component.

[S063] adds a longer-horizon positive signal: across 28 classes at six Uzbek universities, an attempt-first, compare-and-verify GPT-4o workflow was associated with higher supervised unfamiliar immediate and delayed engineering-transfer scores than a closely matched curated-alternative workflow. Deterministic post-baseline allocation and unmatched adaptivity mean the result belongs to the complete configuration and remains non-causal.

[S064] adds a current-system but fragile contrast. Open GPT-5.3 collaboration produced the strongest assisted writing products, while bounded support plus compulsory reflection produced the strongest observed supervised no-AI near-transfer profile. With only six intact classes and exact wild-cluster p values from 0.050 to 0.063, it is mechanism-consistent boundary evidence rather than a validated policy recipe.

## Boundary conditions

Each intervention bundles multiple components. We cannot yet infer one universal “AI tutor recipe,” the independent contribution of the model, or durable far transfer. Domain structure, instructor role, dosage, and learner characteristics vary.

The mechanism claim is more durable than any effect magnitude. The chain now includes a current GPT-5.3 classroom comparison, but that study is class-confounded and bundles reflection with delegation limits. Historical GPT-4/4o and recent-system evidence still carry much of the stronger causal or delayed-outcome signal. Current-model randomized replications should test whether stronger generation changes the value of guardrails, reflection, verification and access timing rather than assuming transfer.

## Counterevidence and uncertainty

Novelty, extra time, unusually intensive author-led design, aligned assessments and unmatched adaptivity may inflate results. The new positive delayed study and the current-system bounded-support pattern do not identify attempt timing, reflection, verification, adaptivity or the model as the active component. Independent replications and factorial component studies remain priorities.

## Product relevance

Learning products should expose and test their pedagogical policy: when to ask, hint, explain, model, retrieve, delay, and hand control back. Model capability alone is not a learning architecture.
