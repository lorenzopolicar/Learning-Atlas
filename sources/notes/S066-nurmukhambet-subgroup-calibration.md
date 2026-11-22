---
{
  "id": "S066",
  "type": "source",
  "title": "Subgroup Calibration and Mastery Decision Errors in Knowledge Tracing",
  "citation_key": "nurmukhambet2026subgroup",
  "source_kind": "conference-paper",
  "epistemic_roles": ["empirical-study"],
  "year": 2026,
  "url": "https://doi.org/10.1109/SIST61674.2026.11596401",
  "status": "reviewed",
  "topics": ["learner-modelling", "assessment-validity", "product-measurement", "ethics-and-governance"],
  "added": "2026-11-22",
  "last_reviewed": "2026-11-22",
  "technology_dependence": "model-independent",
  "access": "restricted"
}
---

# S066 — Subgroup calibration and mastery decision errors

## Why it matters

This paper shows how strong aggregate calibration can conceal materially worse reliability for a lower-performing subgroup and how the error changes with learning stage and decision threshold. A learner-model confidence field is therefore incomplete without the population, evidence regime, threshold, and decision for which calibration was checked.

## Identity and provenance

- Canonical identifier: Nurmukhambet, S., and Meirmanova, A., *2026 IEEE 6th International Conference on Smart Information Systems and Technologies (SIST)*, 13–15 May 2026; DOI 10.1109/SIST61674.2026.11596401.
- Version inspected: complete author-posted rendering alongside the IEEE record; no open licence was identified and no full text is stored in Git.
- Content inspected: complete paper, especially Methods pp. 3–4, Tables III–VII, Discussion, and limitations pp. 7–8.
- Retrieval: gateway candidate `cand_80d688651f0f548b`; Crossref/OpenAlex identity verified, OpenAlex W7168267893; no correction, retraction, or cited-by records found on 22 November 2026.
- Locator convention: publisher page and numbered paper table/page.

## Study

- Data: EdNet-KT1, 20,705 retained learners, 142 skills, 12,259 questions, and 5.89 million interactions; learner-level 80/10/10 split.
- Models: BKT, logistic regression, DKT, SAKT, AKT, and SAINT; SAINT showed an undertraining warning.
- Analysis: aggregate and subgroup calibration by learner performance third and early/middle/late learning stage; simulated promotion decisions at thresholds .70 to .90.
- Outcomes: ECE and related calibration metrics, false mastery rate, and decision equity ratio.

## Findings

- Aggregate ECE remained below .025 for every model, but all six overpredicted the lower-performing group and underpredicted the higher-performing group (Tables II–III).
- The five worst group-by-stage cells were all lower-performing learners under BKT or logistic regression, with ECE .157 to .195 (Table IV).
- At a .85 threshold, false mastery rates for lower-performing learners were 15.5% to 24.8%, compared with 8.3% to 14.2% for higher-performing learners; the gap changed with model and threshold (Tables V and VII).
- About one in seven lower-performing learners received more incorrect than correct simulated promotion decisions under the neural models (Table VI).

## Limitations and boundary conditions

- One Korean TOEIC dataset; performance groups are defined from observed accuracy, not demographic or protected groups.
- Promotion is simulated from each interaction as if it were an independent mastery decision, so false mastery rates are upper bounds rather than observed platform harm.
- No post-hoc subgroup correction, learning outcome, fairness intervention, or replication was tested.
- The work does not show that subgroup-specific calibrators are fair or that their use would improve learning.

## Evidence profile

| Dimension | Rating | Reason |
|---|---|---|
| Internal validity | moderate | Large held-out dataset and multiple models; decision outcomes are simulated |
| Directness | high | Directly audits calibration and threshold decisions in learner models |
| Consistency | unclear | No cited-by replication located |
| Replication | low | One dataset and one research group |
| Magnitude | moderate | Aggregate ECE below .025 concealed subgroup-stage ECE up to .195 |
| Duration | low | Stage analysis within one logged course history |
| Transfer | low | One TOEIC platform and performance-defined subgroups |
| Ecological validity | moderate | Real interaction histories; simulated promotion decisions |

## Candidate claims

Primary support for [C040](../../claims/C040-calibration-depends-on-evidence-history.md). It narrows [C007](../../claims/C007-learner-models-are-probabilistic-inferences.md): calibration belongs to a versioned inference and decision context, not to a model or learner in the abstract.

