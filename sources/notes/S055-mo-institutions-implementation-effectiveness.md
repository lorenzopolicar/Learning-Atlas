---
{
  "id": "S055",
  "type": "source",
  "title": "Institutions, Implementation, and Program Effectiveness: Evidence from a Randomized Evaluation of Computer-Assisted Learning in Rural China",
  "citation_key": "mo2020institutions",
  "source_kind": "journal-article",
  "epistemic_roles": ["empirical-study"],
  "year": 2020,
  "url": "https://doi.org/10.1016/j.jdeveco.2020.102487",
  "status": "reviewed",
  "topics": ["ai-tutoring", "institutional-design", "teacher-practice", "transfer", "product-measurement"],
  "added": "2026-10-19",
  "last_reviewed": "2026-10-19",
  "technology_dependence": "model-independent",
  "access": "author-manuscript"
}
---

# S055 — The same tutoring software produced different effects under different implementers

## Why it matters

This is the cleanest located falsifier of software portability. It randomized the same computer-assisted English programme across an NGO implementer, a government implementer and no programme, so the institutional delivery system—not just the software—varied causally.

## Identity and provenance

- Authors: Di Mo, Yu Bai, Yaojiang Shi, Cody Abbey, Linxiu Zhang, Scott Rozelle and Prashant Loyalka.
- Publication: *Journal of Development Economics*, 146, 102487; DOI `10.1016/j.jdeveco.2020.102487`.
- Version inspected: complete ten-page author/publisher manuscript.
- Access: lawful open author copy; no full text is stored in Git.
- Retrieval: gateway candidate `cand_2836d107b867d6b3`; PDF SHA-256 `feb50cc4b79a2ac003aa40f94f3c0c3d163206a582a9acd27f0ccd10cf28f7d7`.
- Locator convention: journal PDF page and table.

## Study

- Population and setting: 5,574 grade 4 learners in 120 poor rural public schools in Qinghai, China; 5,253 contributed to the primary endline estimate.
- Design: schools were randomized to the same English CAL programme implemented by an NGO, implemented by government education offices, or business-as-usual control for one academic year.
- Programme: two 40-minute computer-lab sessions per week using identical curriculum, software and training materials. The protocol expected computer teachers to supervise sessions in addition to regular English instruction.
- Outcome: a proctored standardized English test containing items that did not overlap with the software exercises.

## Findings

- The NGO implementation improved English by 0.16–0.18 SD relative to control. The government implementation estimate was -0.07 SD and not significant (page 6; table 4).
- Compared with NGO schools, government schools were 20 percentage points more likely to replace regular English classes with CAL, 30 points more likely to assign English teachers instead of computer teachers to supervise it, and 50 points less likely to receive a call or visit monitoring progress (page 7; table 6).
- Substitution and direct monitoring correlated with test scores, but these intermediate mechanisms were not randomized. The paper explicitly treats that explanation as tentative (pages 7–8; table 7).
- The positive NGO effect could reflect CAL plus additional English time, or even additional instruction time alone. The study therefore establishes an implementer effect, not the independent effect of monitoring or software.

## Limitations and boundary conditions

- This is historical computer-assisted learning, not GenAI. Use it for institutional mechanism and external-validity boundaries, not current-model effect size.
- The government-versus-NGO contrast is causal, but the proposed substitution, staffing and monitoring mechanisms are post-randomization and correlational.
- The study covers one subject, grade, province and governance context. It does not establish that government delivery is generally inferior.
- Hardware was treated as a sunk public investment, which narrows cost transfer to institutions without existing labs.

## Evidence profile

| Dimension | Rating | Reason |
|---|---|---|
| Internal validity | high for implementer contrast | Cluster randomization of identical software across two implementers and control |
| Directness | high for institutional transfer | Directly varies the delivery institution; not GenAI-specific |
| Consistency | moderate | Converges with scale-up and access evidence, but few studies randomize implementer |
| Replication | low | One province and programme |
| Magnitude | small-to-moderate versus null | NGO +0.18 SD; government -0.07 SD and nonsignificant |
| Duration | high | One academic year |
| Transfer | moderate | Independent standardized subject test; no delayed follow-up or far transfer |
| Ecological validity | high | Ordinary rural public schools and government implementation |

## Candidate claims

Supports [C035](../../claims/C035-tutoring-effects-belong-to-delivery-systems.md): a bounded efficacy result cannot be carried across institutions as a software property. It also requires the claim to distinguish the causal implementer effect from correlational explanations about substitution and monitoring.
