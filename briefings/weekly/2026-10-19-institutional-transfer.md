# Tutoring effects do not transfer without a delivery system — 2026-10-19

## Question and existing gap

**Queue item 8:** What institutional conditions determine whether AI tutoring evidence transfers to normal teaching practice?

Bounded Atlas retrieval returned C002, C001, C009, C012, P005 and the positive but bundled Nigeria programme [S005]. The Atlas already said that pedagogical structure matters. It did not distinguish the efficacy of a tutor under research conditions from an institution's ability to preserve dose, instruction, support, infrastructure and equity when the service becomes ordinary practice.

The initial commands were:

```text
python3 scripts/atlas.py query "institutional conditions teacher orchestration AI tutoring transfer normal teaching practice" --type claim --type principle
python3 scripts/atlas.py freshness
python3 scripts/research_gateway.py capabilities
```

## Answer

A tutoring result is not a portable property of software.

The evidence supports a provisional delivery-system claim [C035]: transfer depends on whether an institution can create adequate actual use without displacing more valuable instruction and can supply the infrastructure, troubleshooting, teacher authority, motivation, monitoring and support labour the service consumes. Those conditions are plausible boundaries, not a causal checklist: no admitted study independently randomizes every component.

The strongest falsifier is an implementer-randomized trial of identical CAL. The NGO implementation improved an independent English outcome by about 0.18 SD, while the government implementation was -0.07 SD and not significant [S055]. Substitution and monitoring differed, but those proposed mechanisms remain correlational.

The current implementation boundary is take-up. In two ordinary-school trials, only 53–61% of independently assigned students ever used an AI literacy tutor and average use was 2–5 minutes per week despite scheduled sessions. Engagement-focused human tutors added 1–4 minutes and more completed stories, but did not produce the intended dose or measurable learning [S054]. This does not show the tutor fails at adequate use, and the unnamed platform/model prevents a current-model claim.

The positive counterweight is a public-school PAL programme that produced 0.22 SD mathematics and 0.20 SD Hindi gains after 18 months [S056]. It was not software-only replication. The service was redesigned around labs, extended-battery devices, a local lab role, protected timetable periods, teacher accompaniment, monitoring and device sharing. Official grade-level exam effects were null, and lower support staffing initially reduced use.

The product rule is therefore: treat the operating model as the intervention [P008]. Licences, logins and model quality are inputs. Expansion should depend on achieved dose, displacement, recovery, teacher workload and control, subgroup participation, full cost and independent learning outcomes.

## Source lanes and search path

Three independent read-only lanes were used because implementation research is especially vulnerable to selecting either polished success stories or failure anecdotes:

- **Scout:** prioritized large recent school evaluations, teacher-orchestration reviews and qualitative abandonment cases.
- **Evidence analyst:** audited comparator strength, attrition, outcome timing, bundle attribution and existing [S005]; prioritized a current teacher-capacity RCT and Tutor CoPilot.
- **Contrarian:** searched for implementation failures, randomized institutional contrasts, instructional displacement, low dosage and scale adaptations.

Representative exact queries were:

```text
intelligent tutoring systems scale-up implementation teacher training organizational conditions classroom
teacher intervention K-12 AI instruction implementation feasibility orchestration systematic review
generative AI tutor normal classroom implementation teacher workload infrastructure professional development study
education technology scale-up trial null implementation fidelity teacher workload intelligent tutoring systems
Institutions implementation and program effectiveness rural China randomized evaluation
Access is Not Enough Human Support Improves Engagement with AI Tutoring
Mindspark adapting for scale experimental evidence technology aided instruction India
```

Backward and forward OpenAlex chains were run around Tutor CoPilot, current teacher-orchestration reviews and the scale studies. Full texts were resolved through EdWorkingPapers, NBER, publishers, institutional repositories and lawful author copies.

The public-discourse lane sampled stable LinkedIn posts from the Stanford AI Hub, Qiao Jin, Jeremy Roschelle and Dan Meyer. The podcast/media lane sampled *When AI Can Teach, What Is the Teacher For?*, *Will AI Tutors Change the Classroom?*, and an official Sal Khan interview transcript. These were discovery or perspective sources only; none was admitted as effect evidence. No stable relevant X result survived verification.

## Admitted sources and claim effect

The three-source autonomous cap was reached:

1. **S054 — Robinson et al. (2026).** Two randomized ordinary-school implementations show that access and dedicated session time did not produce meaningful AI-tutor use. Human engagement support improved use and content completion, but dose remained low and exploratory learning effects were null and imprecise. The exact platform and model are unnamed.
2. **S055 — Mo et al. (2020).** A 120-school cluster RCT randomized identical English CAL to NGO implementation, government implementation or control. NGO delivery improved an independent test; government delivery did not. The institution contrast is causal, while explanations through instructional substitution, staffing and monitoring are not.
3. **S056 — Muralidharan and Singh (2025).** An 80-school, roughly 6,500-learner cluster RCT retained meaningful independent mathematics and Hindi gains over 18 months after an earlier efficacy intervention was redesigned for public-school schedules, hardware, support staffing, teacher work and monitoring. The bundle, eligible-school context and null school-exam effects limit portability.

Portfolio effect: [Q005] now names institutional transfer as a decision problem; [C035] makes the delivery-system boundary explicit; [P008] converts it into a falsifiable readiness and rollout principle. [C002] remains active but no longer allows “human in the loop” or “structured tutor” to stand in for adequate institutional delivery.

## Held and rejected candidates

- **Liu et al. (2026), DOI `10.26300/y3f8-vh05`: held.** A current 2,379-student university GenAI-tutor RCT found about 15% take-up and adverse grade and LMS-engagement estimates. It is highly relevant, but S054 supplies the more direct ordinary-school support randomization under the cap.
- **Aston et al. (2026), EEF/NFER Maths-Whizz evaluation: held.** A 63-school RCT/process evaluation found a small independent gain and substantial dose, device, connectivity, support and method-alignment barriers. S056 supplies a longer positive scale test with a clearer adapted operating model.
- **Glave et al. (2026), DOI `10.1596/1813-9450-11476`: held.** A 390-school cluster RCT found that licence, curriculum-specific training and eight months of follow-up improved adoption and teacher output-evaluation skill but not reported time savings. It measures teacher capability, not tutoring or student learning.
- **Wang et al. (2026), arXiv `2410.03017`: held.** Tutor CoPilot increased same-session exit-ticket passing by four percentage points, especially for lower-rated tutors. Only 29% of treatment sessions used it, training was bundled and no standardized end-of-year gain was established.
- **Utterberg Modén et al. (2021), DOI `10.24251/HICSS.2021.186`: held.** The two-school abandonment case sharply identifies teacher control, curriculum alignment and accountability failure, but is small historical qualitative evidence.
- **Lee (2026), DOI `10.1186/s40561-026-00461-1`: held.** The systematic review adds breadth on monitoring, judgment, intervention and orchestration, but its heterogeneous evidence does not estimate institutional components causally.
- **Ferman et al. (2021), MPRA `109063`: held.** A 157-school Khan Academy null corroborates infrastructure and implementation risk; the randomized implementer contrast was more decisive.
- **Social and podcast candidates: rejected as empirical evidence.** They exposed useful questions about human relationships, tool sprawl, legitimacy and teacher work but added no independently inspected causal result.

## Agent disagreement and integration

The scout favoured the EEF/NFER process evaluation, an abandonment case and a current systematic review. The evidence analyst favoured the Peru teacher-capacity RCT and Tutor CoPilot and found that [S005] had been rated too strongly. The contrarian argued that the transfer claim should be built around one causal institutional contrast, one current take-up failure and one positive adapted scale-up.

The integrating decision followed the contrarian ranking because it changes the decision standard most directly: software identity and bounded efficacy are insufficient, while both success and failure depend on the enacted service. The scout and analyst recommendations remain visible as held candidates rather than being averaged into the claim.

## Existing-source correction

[S005] was reappraised. The positive Nigeria result remains useful, but its internal-validity profile is now moderate rather than high. The intervention combined GPT-4/Copilot, up to 18 hours of extra after-school time, teacher training and oversight, paired devices, curriculum-aligned prompts and active monitoring. Endline completion was 57% overall and differential by assignment, spillover occurred, and the public package withholds participant datasets. The study supports a positive bundle under selected lab-equipped conditions, not an isolated AI or teacher-orchestration effect.

## Orqestra change

The Orqestra bridge now requires an institutional-delivery gate [C035, P008]:

- protected intended time and measured achieved dose;
- the activity displaced and an equal-time comparator;
- devices, connectivity, accessibility and failure-recovery ownership;
- named owners for motivation, troubleshooting, monitoring and escalation;
- teacher visibility, rationale, defer, reject and override;
- net teacher and support-staff workload, subgroup participation and full delivery cost;
- independent immediate, delayed, transfer and institution-aligned outcomes;
- a de-support phase after research or vendor help withdraws.

This is a research and product-evaluation requirement, not authorization to implement or collect learner data.

## Uncertainty and falsification plan

Narrow or reject [C035] if a multisite current-model trial shows stable independent and delayed learning effects across low-readiness institutions without protected dose, assigned support labour or monitoring, and without shifting hidden work to teachers or excluding students who need support most.

Strengthen it only if a trial holds tutor and content constant, randomizes a preregistered readiness/support bundle, and includes:

1. equal-time normal instruction or transparent non-AI practice;
2. at least one full year plus a de-support year;
3. intended and achieved dose plus displaced activity;
4. infrastructure failures and recovery time;
5. teacher workload, authority and attention coverage;
6. special-education, language and prior-attainment participation;
7. total delivery cost;
8. independent delayed, transfer and institution-aligned outcomes.

## Capability limitations and fallbacks

- The runtime did not expose the intent-level `research_capabilities` MCP or other Atlas research-intent tools. The documented `scripts/research_gateway.py` fallback supplied capability discovery, DOI resolution, citation chains, lawful locations, content hashes and gitignored staging.
- OpenAlex and Crossref were available. Unpaywall was unavailable because `UNPAYWALL_EMAIL` was unset, so publisher, repository and OpenAlex locations were used and labelled.
- Exa was configured separately but not callable from this run. Podcast Index and YouTube APIs were unavailable. OpenAI transcription was unavailable; no unverified audio claim was used.
- Docling and deterministic PDF extraction were available. Stable local PDFs were inspected directly; no full text was committed.
- Crossref returned HTTP 429 for the Robinson DOI during one resolution attempt. The official EdWorkingPapers page, DOI, full PDF and hash supplied the identity and provenance fallback.

## Process lesson and scheduler state

The process lesson is substantive: implementation evidence should be selected as a success/failure contrast around the decision, not as a catalogue of barriers. A current implementation review or large process evaluation adds breadth, but the randomized implementer comparison changed the causal standard. The next run should prefer component randomization and de-support evidence over another general efficacy paper.

Open draft PRs remained scheduler state. The run fetched `origin/main` at `651eadf`, created `/private/tmp/learning-atlas-weekly-20261019T005730Z` on `atlas/research-weekly-20261019T005730Z`, and based it on the verified head of the existing weekly research stack so proposed research was not duplicated. The user-owned checkout was not edited.

This is the sixth actual weekly scheduler execution. The observation target remains complete at **3 of 3**; no new observation counter or process-lab file was created.

## Checks

- Canonical indexes, graph and NotebookLM export regenerated and current.
- Strict validation: 87 artifacts, 0 errors and 0 warnings.
- Retrieval evaluation: 7 of 7 contracts passed, including the new institutional-transfer contract.
- Unit tests: 34 passed.
- Model-dependent freshness register: 11 sources, all classified; S002 was re-inspected and updated from unknown to historical-system.
- `git diff --check`: passed.

No merge, product implementation, learner-data collection or maturity promotion is authorized by this briefing.
