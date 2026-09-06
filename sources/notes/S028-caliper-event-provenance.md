---
{
  "id": "S028",
  "type": "source",
  "title": "Caliper Analytics Specification 1.2",
  "citation_key": "onedtech2020caliper",
  "source_kind": "standard",
  "epistemic_roles": ["institutional-guidance"],
  "year": 2020,
  "url": "https://www.imsglobal.org/spec/caliper/v1p2/",
  "status": "reviewed",
  "topics": ["learner-modelling", "interoperability", "provenance", "learning-analytics"],
  "added": "2026-09-06",
  "last_reviewed": "2026-09-06",
  "technology_dependence": "model-independent",
  "access": "open"
}
---

# S028 — Caliper event provenance

## Why it matters

Caliper is an authoritative interoperability precedent for a compact learning-activity event and a separate transmission envelope. It sharpens the provenance missing from E001 without pretending that an event standard supplies construct validity.

## Identity and provenance

- Publisher and version: 1EdTech Consortium, final release 1.2, issued 27 March 2020.
- Canonical URL: `https://www.imsglobal.org/spec/caliper/v1p2/`.
- Content inspected: full public HTML, especially §2.1 Event and §5.2 Envelope.
- Retrieval: gateway candidate `cand_99cac240601e14e3`; content SHA-256 `9b3b18abaa9dea7dd614ecf006cf1d6ac318e74628e1cc7eb4bf3306e7b1d311`; normalized content SHA-256 `2171990eb4c1e08f6868e04c021d07874266af05a6397717244b4f3dcee81a63`.

## Standard

- Section 2.1 defines an event around identity, actor, action, object and event time, with contextual links such as profile, application, target, group, membership and session.
- Section 5.2 separates the transport envelope's sensor, send time and data version from the enclosed event data.
- Caliper's tool-use vocabulary records that software was used. It does not determine what function the tool served or whether the recorded activity supports a capability inference.

## Implication for the Atlas

E001 should distinguish occurrence time from record or send time and identify the observer, sensor or asserting application. Event and profile versions should travel with the record. Tool availability, declared use and observed use need separate fields because a generic tool-use event does not establish assistance function.

## Limitations and boundary conditions

- Caliper specifies interoperability, not the truth of an assertion, the validity of a learner construct, calibrated confidence, privacy sufficiency or evidence expiry.
- Version 1.2 is a design precedent, not a requirement that Orqestra serialize the E001 pilot as Caliper.
- The standard's generic activity vocabulary is intentionally less specific than the pilot's assessment argument.

## Candidate claims

Supports the provenance and event-envelope patterns in [P002](../../principles/P002-use-an-evidence-ledger.md). It is not supporting evidence for a claim about learner capability.
