---
{
  "id": "P003",
  "type": "principle",
  "title": "Adapt and fade guidance with evidence",
  "statement": "Use the least complex inspectable support policy that improves independent outcomes; add learner-model adaptation only when domain-specific evidence changes a decision and beats a matched fixed or learner-controlled baseline.",
  "status": "active",
  "confidence": "moderate",
  "topics": ["scaffolding", "learner-modelling", "ai-tutoring"],
  "based_on": ["C003", "C007", "C033", "C034", "B005"],
  "applies_to": ["worked examples", "hint policies", "adaptive pathways", "practice"],
  "exceptions": ["Stable accessibility support", "Safety procedures that require persistent checks", "Learner-requested reference material"],
  "falsifiers": ["Preregistered matched trials across more than one domain show no meaningful superiority on delayed independent outcomes.", "Learner-state errors systematically withdraw support or restrict content coverage for those who need it.", "Average gains are offset by subgroup harm, reduced engagement, delivery burden, or a learner-controlled policy."],
  "last_reviewed": "2026-10-11"
}
---

# P003 — Adapt and fade guidance with evidence

## Principle

Start with a transparent, response-contingent sequence. Make scaffolding conditional on the target knowledge component, demonstrated performance, assistance history and recentness only when those signals are calibrated for the decision. Fade one dimension at a time, expose the reason and override, and verify independent success.

## Rationale

Guidance can reverse in value as expertise develops [C003], but the state used to adapt is uncertain [C007]. Semester-scale sequencing has beaten credible fixed policies [C033], while isolated 30-minute difficulty adaptation did not [C034]. Personalization must therefore beat a matched transparent or learner-controlled policy rather than merely sound individualized [B005].

## Product patterns

- worked example → completion problem → independent problem;
- assistance budgets per capability;
- fixed-policy fallback while state evidence is sparse or poorly calibrated;
- learner override and reason for adaptation;
- periodic unscaffolded probes.

## Falsifiers and measures

Evaluate independent immediate, delayed and transfer outcomes; state calibration; false promotion and false hold; content coverage; help misuse; frustration; fairness across groups; teacher and maintenance burden; and the incremental effect over well-designed fixed and learner-controlled sequences. Hold content, feedback, interface, exposure budget and assessment constant.
