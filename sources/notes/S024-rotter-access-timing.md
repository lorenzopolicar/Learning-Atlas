---
{
  "id": "S024",
  "type": "source",
  "title": "Access Timing as Scaffolding: A Reinforcement Learning Approach to GenAI in Education",
  "citation_key": "rotter2026access",
  "source_kind": "preprint",
  "epistemic_roles": ["empirical-study"],
  "year": 2026,
  "url": "https://arxiv.org/abs/2605.15850",
  "status": "reviewed",
  "topics": ["scaffolding", "learning-vs-performance", "metacognition", "ai-tutoring"],
  "added": "2026-09-01",
  "last_reviewed": "2026-09-01",
  "technology_dependence": "model-dependent",
  "technology_context": {
    "system": "Mistral",
    "version": "Mistral 3 14B",
    "study_period": "not reported in the inspected note",
    "assessed_as_of": "2026-09-02",
    "temporal_relevance": "recent-system",
    "review_due": "2027-03-01",
    "recency_note": "Recent access-policy evidence; its main uncertainty is study design rather than model age, and replication should compare a current system with a transparent fixed rule."
  },
  "access": "publisher-open"
}
---

# S024 — Access Timing as Scaffolding

## Why it matters

This is a direct component study of when a learner should receive ordinary GenAI access. It compares always-on, never-on and adaptively delayed access, then removes AI for an objective test. Its positive result is product-relevant, while its assignment and analysis limitations make it a hypothesis-strengthening preprint rather than a deployment warrant.

## Identity and provenance

- Canonical identifier: arXiv:2605.15850v3
- Version inspected: 11 August 2026, submitted for peer review
- Content inspected: complete HTML/PDF methods, task and policy description, measures, quantitative/qualitative results, limitations and appendices relevant to the reward function
- Access and rights: publisher-open arXiv PDF
- Retrieval: gateway candidate `cand_6a6fb6f04c45653b`; PDF SHA-256 `14f8d8a9821f6f57f3e44900003b233e86a4a3fbdebe660819334eaf90fd21f5`
- Locator convention: numbered section, table and figure in v3

## Study

- Population and setting: 105 university students, mostly bachelor-level, aged 18–39 in nine controlled workshops; 60 women and 45 men.
- Intervention and comparator: an RL policy allowed Mistral 3 14B access after states such as failed attempts and time, compared with always-available and never-available GenAI.
- Outcomes and timing: learning-phase errors, time and AI requests; after a drawing distractor, eight unassisted multiple-choice items about the same social-media/self-image content, item-level confidence judgments and MAI-AI self-report.
- Design: between-group controlled laboratory study. Entire workshop sessions—not individuals—received one condition so sessions would finish together. The policy was trained on simulated students parameterized from a nine-person pilot.

## Findings

- The delayed-access group scored 5.11/8 on the immediate unassisted test versus 4.03/8 for always-on access (t(71)=2.51, p=.014, d=.59). It did not differ from never-on access (5.25/8; p=.762, d=-.07).
- Item-level metacognitive accuracy was higher under delayed than always-on access (5.95 vs 5.17; p=.023, d=.54), but did not differ from never-on access. Self-reported metacognitive-awareness change did not differ among conditions.
- Delayed access produced 2.46 AI requests on average versus 11.25 for always-on access; 43.2% of the delayed group never used AI.
- Exploratory error/time advantages versus never-on access disappeared after controlling for the conditions' unequal gender distribution.

## Limitations and boundary conditions

- Condition assignment by workshop session and a significant gender imbalance weaken causal attribution; the paper's pairwise tests do not model workshop clustering.
- Four participants, including those who answered zero unassisted items correctly, were excluded. If that criterion was not predeclared and is affected by condition, it can bias the primary comparison.
- The policy bundles reward components for completion, time, alternating use, productive failure and cognitive load. No ablation shows that adaptive RL—or any single theory—caused the result.
- The outcome is an eight-item immediate, near test after a short distractor, not delayed retention, transfer or repeated strategy development.
- The policy was trained from a nine-person pilot; participants can game its access rule; the study is a preprint in one topic and laboratory.
- Because 43.2% of the delayed group never received AI, the contrast is an intention-to-treat policy effect, not the effect of delayed AI use among users.

## Evidence profile

| Dimension | Rating | Reason |
|---|---|---|
| Internal validity | low-moderate | Controlled comparison, but session-level assignment, imbalance, exclusion and unmodelled clustering create material bias risk |
| Directness | high | Access policy is manipulated and AI is removed for the objective outcome |
| Consistency | moderate | Direction aligns with attempt-before-support theory and S001; direct replications are absent |
| Replication | low | One preprint |
| Magnitude | moderate | d=.59 versus always-on access on eight items |
| Duration | low | Same-session distractor only |
| Transfer | low | Same content and response format |
| Ecological validity | low | One brief laboratory task with an experimental access gate |

## Candidate claims

Supports low-confidence [C011](../../claims/C011-delayed-access-can-beat-always-on.md). It is not evidence that an RL policy should be deployed; a transparent fixed attempt threshold is the appropriate next comparator.

## Notes

The useful intervention is access timing. The RL machinery is one implementation and should not inherit credit for a bundled policy without ablation.
