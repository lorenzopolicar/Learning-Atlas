---
{
  "id": "S063",
  "type": "source",
  "title": "Independent Engineering Transfer After Traceable Generative-AI-Assisted Learning: A Six-University Controlled Trial with Deterministic Cluster Allocation in Agricultural Engineering Education",
  "citation_key": "syromiatnykov2026transfer",
  "source_kind": "controlled-trial",
  "epistemic_roles": ["empirical-study"],
  "year": 2026,
  "url": "https://doi.org/10.3390/app16188949",
  "status": "reviewed",
  "topics": ["learning-vs-performance", "transfer", "ai-tutoring", "human-ai-collaboration"],
  "added": "2026-11-15",
  "last_reviewed": "2026-11-15",
  "technology_dependence": "model-dependent",
  "technology_context": {
    "system": "Microsoft 365 Copilot Chat in Microsoft Teams",
    "version": "GPT-4o backbone dated 2024-08-06; provider build not disclosed",
    "study_period": "2025-02-03 to 2025-09-08; intervention ended 2025-05-19",
    "assessed_as_of": "2026-11-15",
    "temporal_relevance": "historical-system",
    "review_due": "2027-05-15",
    "recency_note": "The delayed tool-free transfer design is unusually direct, but the GPT-4o intervention is historical-system evidence and the configuration requires current-model randomized replication."
  },
  "access": "open"
}
---

# S063 — Traceable GenAI and independent engineering transfer

## Why it matters

This is a rare multicentre comparison with an active control, unfamiliar supervised tool-free transfer forms, and a follow-up almost four months after instruction ended. Its positive direction narrows the delayed-transfer gap, but deterministic post-baseline class allocation prevents a randomization-based causal interpretation.

## Identity and provenance

- Canonical identifiers: DOI `10.3390/app16188949`; OpenAlex `W7211991287`.
- Version inspected: 21-page published *Applied Sciences* article dated 9 September 2026 plus the publisher's public methods, results, limitations and supplementary-material descriptions.
- Gateway provenance: staged candidate `cand_cc0d319484b97e8b`; Crossref and OpenAlex found no correction or retraction relation.
- Access: CC BY publisher full text. The gateway PDF fetch returned HTTP 403, so full content was inspected through the publisher HTML; no copyrighted full text was committed.
- Locators: sections 2.1, 2.4–2.10, 3.2–3.4 and 4.7; tables 2–3; supplementary files S1–S8.

## Study

- Population and setting: 656 second- and third-year agricultural-engineering students in 28 intact classes taught by nine instructors at six universities in Uzbekistan.
- Design: two-arm controlled trial. Classes were assigned within teacher blocks by deterministic constrained minimization after baseline covariates were observed; assignment was not random.
- Intervention: a 16-week five-stage workflow requiring an independent attempt, a bounded adaptive GenAI alternative, critical comparison, independent verification, and a documented professional decision. Dialogue was limited to four turns.
- Active control: the same curriculum, tasks, time, feedback, verification and decision workflow using version-controlled teacher/textbook alternatives and predefined clarifications. Adaptivity and dialogue were not fully matched.
- Outcomes: Form A on 26 May 2025 and parallel Form B on 8 September 2025. Both used unfamiliar integrated scenarios and were supervised without GenAI, internet, notes, laptops or communication. Blinded assessors scored eight engineering-transfer criteria on a 0–32 scale.
- Registration: no public prospective trial registration. A date-stamped protocol existed, but the signed protocol, analysis plan and protected allocation log were not public.

## Findings

- Available-outcome analyses included 641 immediate and 589 delayed outcomes from the 656 assigned students.
- The adjusted immediate difference was `+2.78/32`, 95% CI `[2.02, 3.55]`, `p<.001`, model-based `d=.72` (table 3).
- The delayed difference was `+2.34/32`, 95% CI `[1.54, 3.14]`, `p<.001`, model-based `d=.51` (table 3).
- Class-level, allocation-covariate, attendance and leave-one-class-out sensitivity estimates were directionally similar. These checks do not remove residual confounding from deterministic allocation.
- The study did not separately score assisted performance, so it does not observe the complete assisted → immediate independent → delayed independent chain.

## Limitations and boundary conditions

- Allocation selected one covariate-balanced assignment deterministically from 75,288 admissible allocations after baseline observation. Confidence intervals are model-based, not randomization-based.
- The public supplement omits the signed protocol, analysis plan and allocation log. Residual class, schedule and institutional confounding remains possible.
- The complete configuration was bundled: independent attempt, adaptive dialogue, comparison, verification, documentation and professional interpretation. The contrast cannot isolate the model, adaptivity, timing or traceability.
- Form A failed the prespecified raw-score comparability tolerance against Forms P and B. Covariate-adjusted between-condition contrasts are interpretable; raw within-person change is not.
- Delayed missingness was about 10%, and the deterministic pattern-mixture stress test did not include imputation uncertainty.
- The author-developed assessment had strong scoring reliability but no separate formal content- or construct-validity study.
- The intervention used historical GPT-4o, one language and one engineering programme family. It is not a current-system forecast.

## Evidence profile

| Dimension | Rating | Reason |
|---|---|---|
| Internal validity | low-moderate | Strong active control, baseline adjustment, blinded scoring and cluster-sensitive analyses; deterministic post-baseline allocation and unavailable prospective materials leave material confounding risk |
| Directness | high | Supervised unfamiliar tool-free immediate and delayed outcomes directly address independent near transfer |
| Consistency | moderate | Positive configuration-level direction contrasts with adverse and null unrestricted-access studies without identifying a moderator |
| Replication | low | One research programme; no independent replication located |
| Magnitude | moderate | Model-based differences of 2.78 and 2.34 on a 32-point rubric, with causal interpretation limited by allocation |
| Duration | moderate-high | Sixteen-week intervention and a delayed form almost four months after the module ended |
| Transfer | moderate-high | Unfamiliar integrated scenarios in the same agricultural-engineering construct family |
| Ecological validity | high | Authentic multicentre course delivery across six Uzbek universities |

## Candidate claims

Supports the bounded configuration-sensitivity claim in [C002](../../claims/C002-pedagogical-structure-changes-ai-learning-outcomes.md). It challenges any universal claim that AI-supported learning necessarily harms independent outcomes, but it does not establish that GenAI, attempt-first timing or verification caused the advantage.

## Notes

The decisive replication would prospectively randomize classes, freeze a current model, match adaptivity and dialogue in the active control, separately score assisted performance, and repeat novel independent forms immediately and after one and four to six weeks.
