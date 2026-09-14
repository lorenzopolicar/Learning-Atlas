---
{
  "id": "P001",
  "type": "principle",
  "title": "Use progressive assistance",
  "statement": "In deliberate learning, offer a low-burden attempt or diagnosis before substantive help when prerequisites and access permit, then escalate through learner-controlled hints, explanations, worked examples or answers with a fast reveal path; make performance-support mode explicit when urgency changes the goal.",
  "status": "active",
  "confidence": "moderate",
  "topics": ["scaffolding", "learning-vs-performance", "ai-tutoring"],
  "based_on": ["C001", "C002", "C003", "C011", "C028", "C029", "B002"],
  "applies_to": ["deliberate learning", "formative practice", "AI tutoring"],
  "exceptions": ["Safety-critical or time-critical performance support", "Accessibility needs where the attempted action is incidental to the target capability", "Novice schema acquisition or high-element-interactivity tasks where a worked example is the instruction", "A learner explicitly choosing worked-example study or diagnostic answer checking"],
  "falsifiers": ["With time and exposure equated, delayed independent or transfer outcomes are no better than answer-first worked-example support.", "The policy creates inequitable dropout, tool switching or unproductive frustration that a fast reveal path cannot mitigate.", "An adaptive escalation policy does not outperform a transparent fixed rule."],
  "last_reviewed": "2026-09-14"
}
---

# P001 — Use progressive assistance

## Principle

In deliberate learning, first offer a low-burden opportunity to think, retrieve, predict, choose, diagnose or attempt when the learner has enough prerequisite knowledge and the action is accessible. Escalate assistance based on observable need, and keep a fast learner-controlled route to a worked example or answer when further struggle is unlikely to be productive.

## Rationale

Unrestricted assistance can improve the current artifact while weakening later independent performance [C001]. Structured tutoring changes outcomes [C002], and the appropriate amount of guidance varies with expertise [C003].

One narrow controlled study found that delaying access matched a no-access condition and beat always-on access on an immediate independent test [C011]. Newer field evidence shows that structured post-error help improves retry quality more consistently than delayed learning [C028], while a small current-system study shows that absolute answer withholding can reduce immediate performance and cause disengagement [C029]. Together these results justify a calibrated comparative pilot, not a universal gate or an opaque RL policy.

## Apply when

The goal is capability development, the learner has enough domain-specific prior knowledge to make the attempt informative, the attempt itself is accessible, and errors are safe and recoverable.

## Do not apply blindly when

The user is explicitly in performance-support mode, the situation is urgent or safety critical, a novice needs a worked example to acquire a schema, or the action creates construct-irrelevant linguistic, executive or accessibility burden.

## Product patterns

- intent switch: learn, assess, or accomplish;
- one low-burden attempt or diagnosis before substantive help;
- progressive hints with learner-controlled escalation and a visible reveal option;
- self-explanation after a worked example;
- pacing thresholds that escalate when repeated questioning produces no progress;
- assistance-state, time, reveal and later-outcome logging.

## Falsifiers and measures

Compare a low-burden attempt with immediate worked-example or core-answer access, crossed with transparent fixed versus adaptive escalation. Hold model, content and time constant where possible; measure delayed independent performance, transfer, completion, external-tool switching, frustration and differential impact—not immediate task success alone.

## Revision history

- 2026-09-14: narrowed the attempt default, added worked-example and diagnostic exceptions, and required a fast reveal path after S042–S044 showed strong retry evidence, weak delayed evidence and a rigid-withholding failure mode.
