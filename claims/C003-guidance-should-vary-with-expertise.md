---
{
  "id": "C003",
  "type": "claim",
  "title": "Effective guidance varies with learner expertise",
  "statement": "Instructional guidance that benefits novices can become redundant, inefficient, or detrimental for more knowledgeable learners, so scaffolding should respond to domain-specific expertise.",
  "status": "provisional",
  "confidence": "moderate",
  "topics": ["scaffolding", "learner-modelling", "ai-tutoring"],
  "supporting_sources": ["S009"],
  "contradicting_sources": [],
  "boundary_conditions": ["Expertise is domain- and task-specific.", "Fading guidance is not equivalent to withdrawing all support.", "Learner-state estimates may be wrong."],
  "product_relevance": "Condition explanation depth, hints, examples, and autonomy on evidence of learner state rather than a static persona.",
  "last_reviewed": "2026-08-31"
}
---

# C003 — Effective guidance varies with learner expertise

## Evidence and reasoning

The expertise-reversal literature documents interactions in which guidance that helps novices becomes redundant or harmful for experienced learners [S009]. This makes adaptive support a learning requirement, not merely a preference feature.

## Boundary conditions and uncertainty

Expertise cannot be safely inferred from confidence, job title, or a few correct responses. Different knowledge components within one learner may need different support. Motivation and task novelty can also alter the right degree of guidance.

## Product relevance

Represent support decisions as hypotheses tied to learner evidence. Fade support gradually, preserve an override, and test whether independent outcomes improve.
