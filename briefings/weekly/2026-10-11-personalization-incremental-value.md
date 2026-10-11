# Personalization must show incremental value — 2026-10-11

## Question and existing gap

**Queue item 7:** When does learner-model personalization outperform a transparent rule-based sequence?

Bounded Atlas retrieval returned C003, C007, B005 and P003. The Atlas already said that expertise matters and learner states are uncertain, but it had no direct comparative evidence showing when a model-driven policy beats a strong rule. P003 could therefore be read as treating adaptation as the answer to heterogeneity before its incremental value had been tested.

The initial commands were:

```text
python3 scripts/atlas.py query "adaptive feedback learner evidence delayed transfer" --type claim --type belief --type principle
python3 scripts/atlas.py freshness
python3 scripts/research_gateway.py capabilities
```

## Answer

Learner-model personalization has not earned a general presumption over transparent sequencing.

It is most defensible when repeated learner-item evidence changes how a constrained practice budget should be allocated, the state signal is calibrated for that decision, and the advantage survives a matched fixed baseline on an independent or delayed outcome [C033]. A five-month GenAI sequencing RCT and semester-long personalized review meet much of that bar [S051, S052].

It is not reliably valuable when exposure is too brief for a useful state estimate, default parameters substitute for local calibration, mastery gates restrict content coverage, or a fixed policy already supplies sensible sequencing. A direct matched 30-minute classroom experiment found exactly no added posttest value [S053, C034].

The product rule is therefore: use the least complex inspectable policy that wins. Add a learner model only after a randomized incremental-value test against matched fixed and learner-controlled policies, with independent, delayed and transfer outcomes plus calibration, coverage, subgroup error and delivery cost.

## Source lanes and search path

Three independent read-only lanes were used because the question is vulnerable to evidence-selection bias:

- **Scout:** ranked direct adaptive-versus-fixed field experiments, prioritizing recent systems, independent outcomes and delayed retention.
- **Evidence analyst:** audited exposure matching, comparator strength, attrition, outcome timing and component attribution; it emphasized large field nulls and exact dose-yoked ablations.
- **Contrarian:** searched for direct falsifiers, simple-rule alternatives, learner-controlled policies, calibration inequity and implementation failures.

Representative exact queries were:

```text
adaptive personalized review fixed schedule randomized learner model
mastery learning learner model heuristic comparison
adaptive instruction learner model compared fixed sequence randomized trial knowledge tracing
Bayesian knowledge tracing adaptive problem selection compared mastery learning fixed sequence
2025 2026 randomized adaptive fixed AI tutor sequence
knowledge tracing fairness subgroup calibration mastery decision errors adaptive learning
```

Backward and forward citation chains were run around Chung et al., Lindsey et al. and Pelánek and Řihák. Full texts were resolved through arXiv, Zenodo and lawful author or institutional manuscripts.

## Admitted sources and claim effect

The three-source autonomous cap was reached:

1. **S051 — Chung et al. (2026).** In a five-month Python course across ten Taipei high schools, 770 analyzed learners were individually randomized between the same GPT-4o tutoring platform with a learner-state reinforcement-learning sequence or a fixed easy-to-hard sequence. The adaptive arm improved an in-person, device-free written certification exam by 0.150 adjusted standard deviations. The effect was concentrated among beginners, but the subgroup requires replication. The policy is bundled, 26% of enrolled learners were excluded from the main analysis, exact model snapshots are unreported and there is no delayed follow-up.
2. **S052 — Lindsey et al. (2014).** In semester-long middle-school Spanish, items were randomized within learners to massed, generic spaced or personalized review with equal review opportunities. Personalized review beat generic spacing by 8.3 points at semester end and 10.0 points 28 days later. It is strong delayed mechanism evidence but limited to vocabulary in one school and does not separate learner-item targeting from broader temporal distribution.
3. **S053 — Sibley et al. (2026).** In 132 second-grade learners, identical tutors differed only in BKT-driven task selection versus a textbook-like fixed sequence. After 30 minutes, the adjusted posttest effect was partial eta squared .00; fixed-sequence learners progressed further by the platform's own mastery estimate. It is a clean direct null, bounded by short exposure, default BKT parameters and no delayed outcome.

Portfolio effect: [C033] now states the bounded positive case for repeated learner-state sequencing, while [C034] states the direct short-horizon null. C003 is no longer allowed to turn expertise heterogeneity into an assumed requirement for complex adaptation.

## Held and rejected candidates

- **van Klaveren, Vonk and Cornelisz (2017), DOI `10.1016/j.econedurev.2017.04.003`: held.** A 1,021-learner year-long field RCT found no average advantage for adaptive practice and about a 0.08 SD static advantage among higher-ability learners. It is highly relevant, but S053 is a more current and cleaner one-component falsifier under the cap.
- **Iterbeke, De Witte and Schelfhout (2021), DOI `10.1016/j.chb.2020.106666`: held.** A 1,177-learner cluster-randomized factorial found no robust immediate or four-week adaptive advantage and lower motivation. Only 32 clusters, selective delayed follow-up and low outcome reliability limit admission.
- **Mettler, Massey and Kellman (2016), DOI `10.1037/xge0000170`: held.** Equal-exposure and yoked geography experiments favour response-contingent scheduling, but the strongest delayed item-yoked contrast was imprecise and the samples were small.
- **Pelánek and Řihák (2017), DOI `10.1145/3079628.3079667`: held.** Even under BKT-friendly simulations, simple mastery criteria made similar decisions, and real-data input choice mattered more than model family. It is a strong complexity warning but does not measure randomized learning outcomes.
- **Upadhyay et al. (2021), DOI `10.1038/s41539-021-00105-8`: rejected from admission in this pass.** A large app experiment favoured machine-learning scheduling, but extensive post-randomization exclusions and in-app/model-derived forgetting weaken the independent-outcome claim.
- **LinkedIn activity `7439676051057786881` and the *AI in Education Podcast* episode “More A’s, More Fails”: rejected as empirical evidence.** They led to or discussed original studies but added no independently inspected causal result.

## Agent disagreement and integration

The scout prioritized S051 and S052 because they directly show positive independent or delayed value over credible fixed policies. The evidence analyst argued that two large authentic field nulls and matched retirement ablations make the general evidence less favourable than a positive-study pair suggests. The contrarian agreed that P003 should narrow now and proposed learner-controlled support as an additional comparator.

The integrating decision admitted one current GenAI positive, one historical delayed positive and one current direct null. This preserves the disagreement in the evidence structure: C033 and C034 are separate claims, P003 remains active at moderate confidence, and Q004 requires a three-arm fixed/model/learner-controlled test rather than resolving the conflict by averaging unlike interventions.

## Claim, belief, principle and Orqestra change

- **Q004:** asks what incremental learning value personalization adds after complexity and harm costs are counted.
- **C033:** repeated learner-state sequencing can improve independent or delayed outcomes over fixed practice.
- **C034:** short, default-parameter difficulty adaptation can add no value over a matched fixed tutor.
- **C003:** expertise heterogeneity is no longer treated as proof that model-driven adaptation is required.
- **B005:** remains adopted at moderate confidence; now counts calibration, coverage, privacy, fairness, explanation, maintenance and delivery burden.
- **P003:** now starts with the least complex inspectable policy and requires matched fixed and learner-controlled comparisons.

For Orqestra, the next decision is an experiment, not a richer learner-model build. Compare a transparent fixed response rule, a learner-model policy and learner-controlled/on-demand support. Hold the tutor, content, feedback, interface, exposure budget and assessment constant. Predefine a smallest meaningful effect and report immediate independent, delayed and transfer outcomes, state calibration, false promotion/hold, content coverage, burden and subgroup effects.

## Uncertainty and falsification plan

Narrow or reject the active principle if preregistered, same-interface field trials across more than one domain show no meaningful advantage on delayed independent outcomes, or if average gains are offset by subgroup false promotion, false hold, restricted coverage, disengagement or material teacher and maintenance burden.

Strengthen it only if the learner-model arm beats both fixed and learner-controlled policies after:

1. identical content, feedback, teacher contact, session cap and exposure budget;
2. externally calibrated state estimates and identical mastery/retirement rules;
3. intention-to-treat, cluster-aware analysis with attrition bounds;
4. independent immediate, delayed, near-transfer and far-transfer outcomes;
5. prespecified prior-knowledge and accessibility subgroup interactions;
6. an ablation showing which learner-state signals change useful decisions.

## Capability limitations and fallbacks

- The runtime did not expose the intent-level Atlas MCP tools. The documented `scripts/research_gateway.py` fallback supplied capabilities, discovery, DOI resolution, citation chains, lawful locations, hashes and gitignored staging.
- OpenAlex and Crossref were available. Unpaywall was unset, so OpenAlex OA locations and publisher/repository pages were used and labelled. Exa was configured as a separate MCP but not callable.
- Docling was available; deterministic `pdftotext` was used for bounded inspection of stable local PDFs.
- Lindsey's author site had an expired TLS certificate. DOI and author-host identity were verified before the manuscript was fetched; the staged copy remains gitignored.
- Podcast Index, YouTube API and OpenAI transcription were unavailable. Public episode and social pages were used only as discovery/perspective lanes, and no audio-derived claim was admitted.

## Process and scheduler state

Open draft PRs remained part of scheduler state. The run fetched `origin/main` at `651eadf`, created `/private/tmp/learning-atlas-weekly-20261011T024558Z-J4AXv0` on `atlas/research-weekly-20261011T024558Z`, and based it on the verified PR #4 head so proposed research was not duplicated. The user-owned checkout was not edited.

This is the fifth actual weekly scheduler execution. The observation target remains complete at **3 of 3**; no new observation counter or process-lab file was created.

## Checks

- Canonical index and NotebookLM export regenerated successfully.
- Strict validation: 81 artifacts, 0 errors and 0 warnings.
- Retrieval evaluation: 6 of 6 contracts passed.
- Unit tests: 34 passed.
- Model-dependent freshness register: 11 sources, all explicitly classified.
- `git diff --check`: passed.

No product implementation, learner-data collection, merge or maturity promotion is authorized by this briefing.
