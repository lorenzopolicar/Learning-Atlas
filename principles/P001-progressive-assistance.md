---
{
  "id": "P001",
  "type": "principle",
  "title": "Use progressive assistance",
  "statement": "In deliberate learning, elicit an attempt or diagnosis before escalating through the least sufficient hint, explanation, worked step, or answer; make performance-support mode explicit when urgency changes the goal.",
  "status": "active",
  "confidence": "moderate",
  "topics": ["scaffolding", "learning-vs-performance", "ai-tutoring"],
  "based_on": ["C001", "C002", "C003", "C011", "B002"],
  "applies_to": ["deliberate learning", "formative practice", "AI tutoring"],
  "exceptions": ["Safety-critical or time-critical performance support", "Accessibility needs where the attempted action is incidental to the target capability", "A learner explicitly choosing worked-example study"],
  "falsifiers": ["Delayed independent or transfer outcomes are no better than answer-first support.", "The policy creates inequitable dropout or unproductive frustration that cannot be mitigated."],
  "last_reviewed": "2026-09-01"
}
---

# P001 — Use progressive assistance

## Principle

In deliberate learning, ask the learner to think, retrieve, predict, choose, or attempt before the system supplies the full solution. Escalate assistance based on evidence, and reveal the answer when further struggle is unlikely to be productive.

## Rationale

Unrestricted assistance can improve the current artifact while weakening later independent performance [C001]. Structured tutoring changes outcomes [C002], and the appropriate amount of guidance varies with expertise [C003].

One narrow controlled study also found that delaying access matched a no-access condition and beat always-on access on an immediate independent test [C011]. Its limitations justify a comparative pilot, not a universal gate or an opaque RL policy.

## Apply when

The goal is capability development, the learner has enough prior knowledge to attempt, and errors are safe and recoverable.

## Do not apply blindly when

The user is explicitly in performance-support mode, the situation is urgent or safety critical, or the action creates construct-irrelevant accessibility barriers.

## Product patterns

- intent switch: learn, assess, or accomplish;
- attempt before reveal;
- progressive hints with learner-controlled escalation;
- self-explanation after a worked example;
- assistance-state logging.

## Falsifiers and measures

Compare against an answer-first condition using delayed independent performance, transfer, completion, frustration, and differential impact—not immediate task success alone.
