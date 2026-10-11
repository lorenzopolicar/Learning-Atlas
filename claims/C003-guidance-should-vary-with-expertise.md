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
  "boundary_conditions": ["Expertise is domain- and task-specific.", "Fading guidance is not equivalent to withdrawing all support.", "Learner-state estimates may be wrong.", "Expertise heterogeneity does not by itself prove that a complex adaptive policy beats a strong transparent rule."],
  "product_relevance": "Treat explanation depth, hints, examples, and autonomy as decisions to test against an inspectable policy rather than inferring an adaptive advantage from heterogeneity alone.",
  "last_reviewed": "2026-10-11"
}
---

# C003 — Effective guidance varies with learner expertise

## Evidence and reasoning

The expertise-reversal literature documents interactions in which guidance that helps novices becomes redundant or harmful for experienced learners [S009]. This establishes a heterogeneity problem, not that a complex learner model is necessarily the best solution. Direct adaptive-versus-fixed comparisons are conditional: long-horizon sequencing can help [C033], while short isolated difficulty adaptation can be null [C034].

## Boundary conditions and uncertainty

Expertise cannot be safely inferred from confidence, job title, or a few correct responses. Different knowledge components within one learner may need different support. Motivation and task novelty can also alter the right degree of guidance.

## Product relevance

Represent support decisions as hypotheses tied to learner evidence. Start with an inspectable rule, fade support gradually, preserve an override, and test whether adaptation improves independent outcomes beyond the rule.
