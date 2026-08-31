---
{
  "id": "C010",
  "type": "claim",
  "title": "Appropriate reliance has distinct adoption and resistance components",
  "statement": "In bounded tasks with verifiable correctness and recorded pre-advice judgments, appropriate human-AI reliance has two distinct components: adopting correct AI advice after an initially wrong human judgment and retaining an initially correct human judgment against incorrect AI advice; confidence helps combination only insofar as it discriminates correct from incorrect judgments under the decision conditions.",
  "status": "provisional",
  "confidence": "moderate",
  "topics": ["human-ai-collaboration", "assessment-validity", "metacognition", "product-measurement"],
  "supporting_sources": ["S020", "S021"],
  "contradicting_sources": [],
  "boundary_conditions": ["The task must have defensible ground truth, an initial human judgment before advice, and enough human-AI disagreement cases for stable estimates.", "Evidence comes from sequential classification tasks, not open-ended generative collaboration or an educational intervention.", "The formal complementarity result assumes a specified arbitration model and does not show that learners can learn or transfer the rule."],
  "product_relevance": "For suitable low-stakes tasks, preserve initial and final judgments and report correct adoption and correct resistance separately; never infer supervisory capability from final accuracy, agreement, or raw confidence alone.",
  "last_reviewed": "2026-08-31"
}
---

# C010 — Appropriate reliance has distinct adoption and resistance components

## Evidence and reasoning

Schemmer et al. operationalize correct uptake (RAIR) and correct resistance (RSR) from sequential decisions [S020]. Their explanation condition improved RAIR but not RSR, demonstrating why agreement or a single reliance direction can be misleading. Li and Steyvers distinguish confidence level and calibration from metacognitive sensitivity—the capacity of confidence to discriminate correct from incorrect judgments—and show its role in an idealized arbitration model [S021].

Together, the sources support a narrow measurement claim: when correctness and pre-advice state are observable, supervisory behaviour has at least two directions and confidence quality is conditional. They do not establish a general human–AI capability construct.

## Boundary conditions

RAIR and RSR are conditional rates whose denominators depend on initial human accuracy, AI accuracy and disagreements. Sparse denominators make them unstable. Asking for an initial answer can also anchor the learner, so the measure changes the interaction it observes.

The claim does not cover creative, normative or social work whose quality is plural or delayed. It does not establish authorship, responsibility, justice, durable learning, or the teachability of evaluative control.

## Product relevance

Use these measures only inside a transparent task-level evidence portfolio. Pair them with domain capability, error severity, verification and escalation behaviour, delayed performance, accessibility, learner burden, and the learner's opportunity to contest an inference.
