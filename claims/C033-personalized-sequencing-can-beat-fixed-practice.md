---
{
  "id": "C033",
  "type": "claim",
  "title": "Personalized sequencing can outperform a fixed practice sequence",
  "statement": "Learner-state-driven practice selection can improve independent or delayed outcomes over a matched fixed sequence when repeated learner-item evidence changes how a constrained practice budget is allocated.",
  "status": "provisional",
  "confidence": "moderate",
  "topics": ["learner-modelling", "scaffolding", "retention", "ai-tutoring"],
  "supporting_sources": ["S051", "S052"],
  "contradicting_sources": ["S053"],
  "boundary_conditions": ["The positive studies used semester-scale or five-month interventions; a 30-minute matched adaptation was null.", "Benefits are established for practice sequencing, not personalization of tone, format, identity or every tutor response.", "State estimation and policy components are bundled in the current GenAI field result.", "The strongest current effect was concentrated among programming beginners; expertise interactions require replication."],
  "product_relevance": "Test adaptive sequencing against a transparent fixed policy with the same content, interface, feedback and exposure budget; require independent and delayed outcomes before accepting the added learner-model complexity.",
  "last_reviewed": "2026-10-11"
}
---

# C033 — Personalized sequencing can outperform fixed practice

## Claim

Personalization earns its complexity when learner evidence changes which practice exposure is selected and the advantage survives a matched fixed baseline after support is removed.

## Evidence and reasoning

In a five-month Python course, a learner-state reinforcement-learning policy improved an independent written exam by 0.15 standard deviations over the same GPT-4o tutor with a fixed sequence [S051]. In semester-long Spanish review, a learner-by-item memory scheduler improved retention by 8.3 points at semester end and 10.0 points 28 days later over a generic spaced schedule with equal review opportunities [S052].

These results share a plausible boundary: repeated observations let the system reallocate a scarce practice budget across learner-item pairs. They do not establish that every personalization mechanism or richer model is useful.

## Boundary conditions

[S053] isolated task-difficulty adaptation for 30 minutes and found no posttest advantage over a structurally matched fixed tutor. Long enough observation, calibrated signals, recoverable state errors, adequate content coverage and a decision that genuinely differs by learner are candidate preconditions, not established universal moderators.

## Counterevidence and uncertainty

The current field RCT bundles LLM-scored signals, particle filtering, reinforcement learning and difficulty choice. The historical retention study bundles item targeting with temporal distribution. Neither isolates which model feature is necessary, and neither demonstrates far transfer.

## Product relevance

Begin with a strong inspectable sequence. Add adaptation only through a randomized incremental-value test that holds the tutor, content, feedback and opportunity constant and measures unassisted retention or transfer.
