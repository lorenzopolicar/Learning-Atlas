# Taxonomy

## Core entities

| Prefix | Type | Purpose |
|---|---|---|
| `S` | Source | A research paper, report, book, dataset, standard, or other inspected work |
| `C` | Claim | An atomic empirical or carefully delimited theoretical proposition |
| `B` | Belief | Our current synthesis and direction of travel |
| `P` | Principle | Conditional guidance for product or learning design |
| `D` | Decision | A contextual application of one or more principles |
| `E` | Experiment | A test of a claim, belief, principle, or product assumption |
| `Q` | Question | An unresolved research or normative question |
| `R` | Review | A protocol-led synthesis programme |
| `N` | Discourse note | Philosophical, critical, historical, or practitioner perspective |

IDs are permanent and never reused. Titles and filenames may evolve; inbound references use IDs.

## Source media and epistemic role

`source_kind` describes the container: journal article, preprint, report, book, chapter, podcast episode, interview, lecture, video, newsletter, social post, standard, dataset, product evidence, or another precise kebab-case kind.

`epistemic_roles` describes what the inspected source can contribute:

- `empirical-study` and `research-synthesis` — evidence that still requires design and boundary appraisal;
- `theoretical-argument` and `normative-argument` — reasoning to examine rather than effects to quote;
- `expert-perspective` and `firsthand-account` — situated testimony, experience, and taste;
- `historical-source` and `institutional-guidance` — context, policy, or authoritative interpretation;
- `product-claim` — a claim by an interested maker that requires independent verification;
- `dataset` — observations whose construction determines suitable inference;
- `discovery-lead` — something that points to another source but is not yet evidence.

A source may have several roles. Container does not determine authority: a podcast can contain firsthand testimony, a paper can be a theoretical argument, and a standards document can be authoritative for requirements without proving learning effects.

## Topic vocabulary

Use a small set of stable top-level topics and add precise free-text tags only when necessary:

- `learning-vs-performance`
- `learner-modelling`
- `assessment-validity`
- `feedback`
- `retrieval-and-spacing`
- `scaffolding`
- `metacognition`
- `motivation-and-agency`
- `transfer`
- `ai-tutoring`
- `human-ai-collaboration`
- `teacher-practice`
- `institutional-design`
- `ethics-and-governance`
- `product-measurement`

## Context vocabulary

Important boundaries should be written in prose and may also use these facets:

- learner expertise: novice, intermediate, expert;
- mode: deliberate learning, assessment, performance support;
- setting: school, higher education, workplace, informal;
- social arrangement: individual, peer, cohort, teacher-mediated;
- stakes: low, medium, high;
- time horizon: immediate, delayed, longitudinal;
- outcome: performance, retention, near transfer, far transfer, real-world capability.

## Relationship vocabulary

- `supports` / `challenges`: source-to-claim evidence relations
- `derived_from`: claim-to-belief synthesis
- `based_on`: claim/belief-to-principle reasoning
- `applies`: principle-to-decision application
- `tests`: experiment-to-claim/belief/principle falsification
- `supersedes`: explicit replacement without deleting history
- `tension_with`: unresolved contradiction worth preserving
