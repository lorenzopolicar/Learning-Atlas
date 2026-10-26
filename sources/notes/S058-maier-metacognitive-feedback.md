---
{
  "id": "S058",
  "type": "source",
  "title": "Designing Against Deskilling: Metacognitive Feedback Reduces Cognitive Offloading to LLM Assistants",
  "citation_key": "maier2026deskilling",
  "source_kind": "preprint",
  "epistemic_roles": ["empirical-study"],
  "year": 2026,
  "url": "https://arxiv.org/abs/2609.20143",
  "status": "reviewed",
  "topics": ["learning-vs-performance", "cognitive-offloading", "metacognition", "scaffolding"],
  "added": "2026-10-25",
  "last_reviewed": "2026-10-25",
  "technology_dependence": "model-dependent",
  "technology_context": {
    "system": "OpenAI GPT-OSS-120B through Amazon Bedrock",
    "version": "openai.gpt-oss-120b-1:0",
    "study_period": "August 2026",
    "assessed_as_of": "2026-10-25",
    "temporal_relevance": "current-system",
    "review_due": "2027-04-25",
    "recency_note": "Exact current-generation open-weight endpoint and study month are reported; transfer to other models and ordinary chat interfaces remains untested."
  },
  "access": "publisher-open"
}
---

# S058 — Metacognitive feedback reduces answer offloading

## Why it matters

This preregistered component experiment supplies both current-system null evidence and a design intervention. It separates AI access from how a learner requests help: an explicit-request assistant did not significantly reduce immediate unaided performance, while contextual feedback reduced repeated complete-answer requests and modestly improved the independent test.

## Identity and provenance

- Canonical identifiers: arXiv:2609.20143v1; DOI 10.48550/arXiv.2609.20143
- Version inspected: 17 September 2026
- Content inspected: complete PDF, preregistration description, system validation, methods, tables 2–3, results, discussion and limitations
- Access and rights: publisher-open arXiv PDF
- Retrieval: gateway candidate `cand_646b583210877a07`; PDF SHA-256 `e9640db7b96cbb7d09ed9cab0c9a06cc476c804f2bbbd91bce91639b6f11e3ee`
- Locator convention: numbered section, table and page in v1

## Study

- Population and setting: 704 UK Prolific adults aged 18–80 after five non-completions and eleven honesty-check exclusions.
- Intervention and comparator: five randomized conditions—no AI, AI only, metacognitive feedback, symbolic effort reward, or both interventions—during ten fraction-arithmetic learning items.
- Assistance policy: GPT-OSS-120B offered guidance by default and complete solutions only when explicitly requested. The system, request classifier and frozen prompts were validated before deployment.
- Outcomes and timing: logged complete-answer offloading across nine measured learning items and six immediate unaided near-transfer items with new operands and expressions.

## Findings

- AI only did not significantly underperform no AI on the unaided test: .62 versus .65; OR .80, 95% CI [.42, 1.51], one-sided p=.244.
- Metacognitive feedback reduced complete-answer offloading (OR .47, 95% CI [.22, 1.00], one-sided p=.026) and improved unaided item accuracy (OR 1.51, 95% CI [.98, 2.33], one-sided p=.030).
- The symbolic effort reward changed neither offloading nor unaided accuracy significantly.
- A ten-percentage-point increase in offloading was associated with 32% lower odds of later correctness, but offloading was not randomized; this relationship is observational.
- Feedback reduced repeated offloading after an offloaded item without measurably improving the study's metacognitive-accuracy or sensitivity measures.

## Limitations and boundary conditions

- The assessment was immediate after one brief arithmetic session; durability and far transfer are unknown.
- Confirmatory tests were one-sided and the two-sided intervals for both feedback effects touched or crossed the null.
- The assistant already made answer offloading deliberate. Results need not generalize to default answer-giving systems.
- The feedback bundled a process mirror, practice explanation, monitoring cue and visualization. No ablation identifies the active component.
- The offloading–performance association is correlational and may reflect prior ability or disposition.
- The study is a single preprint using adult microtasks rather than an authentic course.

## Evidence profile

| Dimension | Rating | Reason |
|---|---|---|
| Internal validity | moderate-high | Preregistered randomized factorial design, exact system and logged behaviour; one-sided borderline tests limit confidence |
| Directness | high | Manipulates interaction design and removes AI for the outcome |
| Consistency | moderate | Reconciles current harm findings through an explicit-request boundary; independent replication absent |
| Replication | low | One preprint |
| Magnitude | small-moderate | Feedback OR 1.51 for unaided correctness with wide uncertainty |
| Duration | low | Same-session outcome |
| Transfer | moderate-low | New operands and expressions, same fraction procedures |
| Ecological validity | low | One short online arithmetic task |

## Candidate claims

Supports [C002](../../claims/C002-pedagogical-structure-changes-ai-learning-outcomes.md) as a current-system interaction-policy signal. It does not show that metacognitive feedback prevents durable deskilling or that explicit-request friction alone caused the AI-only null.

## Notes

The appropriate Orqestra test is an ablation with two-sided inference and a delayed independent assessment: explicit request alone, process mirror alone, practice explanation alone, monitoring cue alone, and combinations.
