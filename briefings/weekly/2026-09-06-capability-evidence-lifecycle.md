# Capability evidence needs separate observation and inference lifecycles — 2026-09-06

## Question and bounded Atlas starting point

**Q002 / queue item 3:** How should a capability evidence event represent assistance, context, confidence and expiry?

The run began with bounded retrieval, not an empty web search:

```text
python3 scripts/atlas.py query "How should a capability evidence event represent assistance context confidence expiry" --type claim --type belief --type principle --type decision --type question
python3 scripts/atlas.py freshness
python3 scripts/research_gateway.py capabilities
```

The query returned 12 relevant artifacts in 4,735 characters, led by C008, P006, C007, P003, P002, C009, C010 and C001. The existing graph already required probabilistic, contextual, contestable evidence and distinct assistance lanes. The unresolved problem was that E001 schema 0.1 placed observation, scored judgment, intended inference, model uncertainty, use policy and three expiry-like timestamps inside one append-only event.

## Answer

A capability evidence event should be an immutable, purpose-minimal observation envelope—not a mastery assertion. It should preserve event and recording time, task and instrument versions, construct-relevant conditions, observer/sensor provenance, work-product references, and assistance permission, availability, declaration, observed use, function and classification basis.

Scoring is a correctable assertion with rubric, evidence-rule, scorer and time provenance. Learner self-confidence is an optional observed response with a named scale and elicitation method; it is not model confidence. A learner-state estimate is a separately versioned inference linked to observations, with its model, calibration boundary, typed uncertainty, use boundary, temporal policy and supersession state.

There are three different clocks:

1. observation `retentionUntil` governs deletion or de-identification;
2. inference `reviewAfter` or `doNotUseAfter` governs staleness for a decision;
3. `authorizedUntil` governs permitted use.

Elapsed time does not make the historical observation epistemically disappear. It should change an estimate only through a validated, context-specific model [C013].

## Source lanes and citation chain

Lanes were chosen because each could change a different part of the answer:

- **Assessment architecture:** exact-title and official ETS/CRESST resolution led to Mislevy, Almond and Lukas [S026]. Their evidence-centred design separates work products, response-processing observables and probabilistic student-model variables. This changed the object boundary.
- **Empirical falsification:** knowledge-tracing and forgetting searches led through DBLP to the official EDM/ERIC proceedings and Qiu et al. [S027]. Time-aware BKT produced gains, nulls and reversals across prediction settings and datasets. This blocked a universal expiry rule.
- **Interoperability/provenance:** event-standard searches led to the official 1EdTech Caliper 1.2 specification [S028]. Its event and envelope distinctions exposed missing observer/sensor, recorded/send-time and profile-version provenance. Caliper is a design precedent, not validity evidence.

The search and citation path was:

```text
Q002 + C007/C008/C010 + P002/P006 + D002/E001
  -> evidence-centred design / student-evidence-task models
  -> time-aware BKT / forgetting / new-day prediction
  -> learning activity event / sensor / sendTime / profile version
  -> public assessment-AI and learner-data discourse
  -> linked original articles, publisher RSS and standards
```

Representative gateway/native queries included:

```text
evidence centered design task model evidence model learner model
"Does Time Matter? Modeling the Effect of Time with Bayesian Knowledge Tracing"
knowledge tracing time decay forgetting confidence uncertainty learner model primary research PDF
1EdTech Caliper event envelope sensor sendTime official
official xAPI 2.0 statement context result timestamp authority
site:linkedin.com/posts assessment AI evidence capability assistance
site:x.com assessment AI evidence capability learner assistance
"What AI Changes About Assessment Evidence" podcast RSS Kristen DiCerbo transcript
```

Citation exploration also followed ECD forward into later assessment work, the learning-analytics privacy study backward into contextual-integrity sources, and public posts to their linked original articles. Those chains refined boundaries but did not outrank the admitted trio.

## Admitted sources

The three-source autonomous admission cap was reached:

- **S026 — Mislevy, Almond & Lukas (2003), _A Brief Introduction to Evidence-Centered Design_.** Complete CRESST reissue inspected; DOI and OpenAlex/Crossref identity verified. Foundational theoretical architecture, not causal evidence. Supports separate event, observable and inference objects.
- **S027 — Qiu et al. (2011), _Does Time Matter? Modeling the Effect of Time with Bayesian Knowledge Tracing_.** Complete paper inspected in official open proceedings. Empirical model comparison and useful contradiction. Supports context-specific temporal weighting, not general capability decay.
- **S028 — 1EdTech (2020), _Caliper Analytics Specification 1.2_.** Official full HTML inspected and hashed by the gateway. Authoritative interoperability standard. Supports event/transport provenance only.

No full text, transcript or copyrighted source body was committed. Local lawful copies remain in the gitignored research inbox with receipts and hashes.

## Rejected and held candidates

- **Abdelrahman et al., Knowledge Tracing survey:** full open article inspected, but its broad review added less answer-changing evidence than Qiu's primary null/reversal under the cap.
- **W3C Verifiable Credentials 2.0 and Open Badges 3.0:** authoritative for a future credential layer, including credential validity and refresh, but E001 prohibits credentialing and the standards do not validate cognition.
- **xAPI 2.0:** the current IEEE source repository was inspected by an agent and is the strongest next standards comparator. It was held because Caliper had deterministic gateway provenance and already supplied the needed event/envelope distinction; the legacy public xAPI 1.0.3 copy was not substituted as current authority.
- **Gervet, Galyardt/Goldin, Settles/Meeder and a 2025 decay-model comparison:** strong calibration and temporal-policy alternates. They were held to avoid using the cap on overlapping model studies; the next pass should revisit Gervet or the newer comparison if calibration or expiry becomes the principal claim.
- **Jacobs & Wallach, Selbst et al., OAIC guidance, Mutimukwe et al., and Longin et al.:** strong construct-validity, privacy and governance challenges. They shaped falsifiers and purpose minimization but were indirect to the narrow event/inference boundary or overlapped existing Atlas validity sources.
- **Phill Dawson and Oleksandra Poquet LinkedIn positions:** stable activity identities were preserved and empirical links followed. Dawson's post led to Corbin, Dawson and Liu's inspected article; Poquet's post led to data-sharing studies. Posts remained expert context/discovery leads rather than evidence authority.
- **Podcast episodes:** EDUCAUSE's privacy episode and PSI/Kristen DiCerbo's assessment-evidence episode were sampled. The latter was resolved to publisher URL, RSS GUID `624495e9-2e0a-4acb-99a6-1054ed123ba9` and duration `00:36:21`, but no transcript was available and audio was not inspected. Neither was admitted.
- **Public X:** no stable, inspectable position added a distinct argument, so no source was promoted to satisfy a lane quota.

## Agent disagreements and integrating judgment

The independent scout prioritized ECD, Qiu and Caliper. The evidence analyst preferred ECD, a calibration benchmark and current xAPI. The contrarian wanted a stronger four-object split—observation, assertion, inference and governance—and prioritized measurement-validity, newer forgetting and Australian privacy sources.

The disagreement was substantive rather than averaged away. The canonical update uses the scout's three complementary evidence roles, adopts the analyst's separate scored-observable and calibration boundary, and adopts the contrarian's warning that confidence, assistance function and correctness are assertions with provenance. It stops short of a production-ready four-service architecture because none of the sources validates that implementation choice in Orqestra.

## Claim, principle and contract changes

- Added low-confidence provisional C013: elapsed time does not create a universal evidence-expiry rule.
- Strengthened C007 with evidence-centred design's observation–observable–inference separation.
- Revised P002 to require linked but separate observation, scored assertion and inference records, purpose-minimal provenance, and distinct retention/use/review controls.
- Updated Q002 and D002 with the bounded synthesis and next falsification step.
- Revised E001's event schema from 0.1.0 to 0.2.0 and added a separate inference schema plus synthetic inference fixture.
- The event now distinguishes occurred/recorded times; permission, availability, declared and observed assistance; classification basis/status; self-reported confidence and model uncertainty; scoring provenance; immediate/delayed horizon and transfer distance.
- Removed `intendedInference.expiresAt` and `inferenceBoundary.validUntil` from the event. The inference fixture separately demonstrates review, use authorization and no-decay policy while the event retains its own retention deadline.
- R001 was not changed: its living review concerns assisted versus later independent learning outcomes, not Q002's representation contract. Q002, D002, P002 and the dated briefing are the relevant review trail for this pass.

## Orqestra relevance

Orqestra should not stretch existing course or assessment summaries into a durable learner trait. A research-flagged pilot can preserve purpose-minimal task observations and correctable scoring assertions, then build a versioned inference view whose evidence links and boundaries are inspectable. Tool presence or permission cannot establish substantive delegation; learner self-confidence cannot stand in for calibrated model uncertainty; and a fixed TTL cannot stand in for validated forgetting.

This is a research-contract change, not authorization to implement a production profile, credential, rank, employment signal or silent mastery update. Learner/domain/accessibility co-design and an Orqestra architecture/privacy review remain gates.

## Uncertainty and falsification

Confidence in the architecture direction is moderate; confidence in C013 is low. ECD is foundational but not a causal validation. Qiu is historical, model-specific and limited to two tutoring datasets. Caliper establishes interoperability semantics, not epistemic validity or privacy sufficiency. The E001 fixtures are synthetic.

The next pass should try to falsify the richer contract:

- compare decision quality, calibration, contestability and debugging against a purpose-minimal no-history baseline;
- test whether learners and independent raters can reliably classify assistance function and basis, including `unknown` and disputed states;
- measure missingness, response reactivity, accessibility burden, anxiety and privacy cost from confidence and provenance collection;
- compare no-decay, elapsed-time and opportunity-order policies prospectively by domain and use;
- verify that corrections actually supersede downstream assertions/inferences and that retention removal covers indexes, copies and backups;
- test current xAPI 2.0 and calibrated knowledge-tracing representations without confusing provenance integrity with construct validity.

## Capability limitations and fallbacks

- Initial OpenAlex discovery failed under sandbox DNS; an approved network rerun succeeded.
- OpenAlex and Crossref were available. Unpaywall was unconfigured, so OpenAlex/native lawful locations were used.
- Exa was advertised as a separate MCP but was not callable in this environment; native web filled broad discovery.
- Zotero local API access failed.
- Docling returned no usable output for the inspected PDFs; `pdftotext` was the deterministic fallback.
- Podcast Index and OpenAI transcription were unavailable; Apple Search, publisher RSS and publisher transcripts/pages were used. No inference was made from uninspected audio.
- LinkedIn direct inspection redirected to sign-up for one post; stable activity identity and the linked original were preserved, and the partial snapshot was not admitted.

## Process lesson and scheduler observation

Fresh-worktree queue selection changed the question relative to the stale dirty checkout, demonstrating why origin/main must be authoritative before source discovery. The first actual scheduled-run observation is recorded in `research/process-lab/2026-09-06-scheduled-research-scout-observation-1.md`; the counter is now **1 of 3**. The branch name retained the stale label, but canonical work and state use Q002. No pull-request churn occurred before opening the single draft.

## Checks

- Both JSON Schema contracts and all synthetic fixtures passed `check-jsonschema`.
- `atlas.py validate --strict` validated 61 artifacts with zero errors and zero warnings.
- All six retrieval evaluations passed.
- All 34 repository tests passed.
- Ten generated index/map files and the NotebookLM pack were regenerated; the generated-view test confirmed they are current.
