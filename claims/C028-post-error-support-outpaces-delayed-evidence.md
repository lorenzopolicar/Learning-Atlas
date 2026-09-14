---
{
  "id": "C028",
  "type": "claim",
  "title": "Post-error AI support improves retry quality more clearly than delayed learning",
  "statement": "In two recent field experiments, structured or interactive AI support after an incorrect attempt improved immediate correction or recovery relative to static hints or non-AI worked solutions, while delayed independent benefit was unmeasured in one study and modest, imprecise and bundled with mastery in the other.",
  "status": "provisional",
  "confidence": "moderate",
  "topics": ["ai-tutoring", "scaffolding", "feedback", "learning-vs-performance"],
  "supporting_sources": ["S042", "S043"],
  "contradicting_sources": ["S044"],
  "boundary_conditions": ["Both field interventions bundle multiple tutoring components and do not isolate attempt-before-answer.", "LearnLM messages were human-supervised and its outcomes were immediate or next-topic.", "NUMI's one-week gain was marginal, limited to one practiced item in the mastery condition and accompanied by slower progression."],
  "product_relevance": "Treat post-error recovery as a process signal, not a mastery update; compare a transparent fixed escalation and learner-controlled reveal against answer-first support on delayed independent transfer.",
  "last_reviewed": "2026-09-14"
}
---

# C028 — Post-error AI support improves retry quality more clearly than delayed learning

## Claim

Interactive or structured AI support can help a learner recover after an error, but current evidence is much stronger for the next response than for durable independent learning [S042, S043].

## Evidence and reasoning

In NUMI, randomized AI assignment inside a mastery workflow improved observed next-attempt recovery after mistakes and reduced attempts to the next correct answer, while increasing time. The cleanest one-week estimate was only 3.2 percentage points on one practiced item and was marginally significant [S042]. In Eedi, human-supervised LearnLM and human tutoring sharply improved next-attempt and same-topic correction over a static hint; the next-topic result was still immediate and within the same platform [S043].

These studies support intervening at a diagnosed error. They do not establish that every learner must attempt before receiving any substantive help, that hints should always precede worked examples, or that adaptive/RL selection beats a transparent rule.

## Counterevidence and uncertainty

A small current-system experiment found that a rigid Socratic bot underperformed unrestricted answers on an immediate post-test and caused substantial abandonment [S044]. That result cannot adjudicate delayed learning, but it shows that withholding and pacing can dominate the intended mechanism.

## Product relevance

Log the initial attempt, error type, help level, reveal choice, recovery, time and later independent outcome separately. Do not infer mastery from a corrected retry or a three-in-a-row platform threshold.
