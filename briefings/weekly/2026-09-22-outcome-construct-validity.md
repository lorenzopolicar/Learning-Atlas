# Agency, dependence, calibration and help-seeking are not one scale — 2026-09-22

## Question and existing gap

**Queue item 5:** Which outcomes capture learner agency, dependence, calibration and help-seeking?

Bounded Atlas retrieval returned C010, S021, E001 and B004. The gap was not simply a missing instrument. Existing records already separate correct adoption from correct resistance and confidence level from discrimination, but E001 could still mistake independence for agency, preferred help behaviour for learning, and elicited confidence for a passive observation.

The initial commands were:

```text
python3 scripts/atlas.py query "learner agency dependence calibration help-seeking outcomes" --type claim --type principle
python3 scripts/atlas.py freshness
python3 scripts/research_gateway.py capabilities
```

## Answer

Do not build an omnibus “learner sovereignty” or dependence score. Use a portfolio whose components remain interpretable:

- **Agency:** self-endorsed goals and support, meaningful choice, voice, revision and refusal—not simply acting without help [C030].
- **Dependence/harm:** support-withdrawal decrement, loss of control or capability, negative consequences and recovery, while preserving access-restoring technology. Usage frequency is context, not diagnosis.
- **Calibration:** item-level correctness and confidence, absolute bias and discrimination, plus correct adoption and correct resistance. Treat prompt timing and frequency as an intervention because confidence elicitation can change monitoring and control [C032].
- **Help-seeking:** condition on need or opportunity; distinguish timing, source, instrumental versus answer-seeking help, escalation, verification and application. A preferred log pattern is not a learning outcome [C031].
- **Learning safeguard:** keep supported quality, immediate accessible-independent performance, delayed retention and transfer separate.

Confidence is moderate for these separations and low for any diagnostic use. No admitted source validates a combined score or a current GenAI learner trait.

## Source lanes and search path

Three independent lanes were chosen to expose construct errors rather than accumulate similarly framed scales:

- **Scout:** searched validated agency, help-seeking, observable reliance and current GenAI process evidence. It preferred Reeve and Tseng's agentic-engagement scale, Zheng et al.'s reliance taxonomy and Viberg et al.'s LLM help-seeking interviews.
- **Evidence analyst:** audited psychometrics and criterion validity. It found Reeve and Tseng useful for constructive classroom contribution, while current dependence/help scales remained largely self-report, single-setting or weakly tied to independent outcomes.
- **Contrarian:** searched for sources that would invalidate the measurement plan. It surfaced the autonomy–independence distinction, behavioural-help-versus-learning dissociation and confidence-rating reactivity.

Representative exact queries were:

```text
agentic engagement student agency scale Reeve Tseng
academic help seeking instrumental executive avoidance validated scale
generative AI student reliance calibration help seeking behavior
2025 2026 generative AI students dependence overreliance calibration help seeking behavioral experiment unassisted performance
validated student agentic engagement scale Reeve Tseng 2011 DOI full text
metacognitive calibration measures absolute accuracy bias discrimination
AI as First Stop academic help-seeking STEM students
```

The citation chain was:

```text
C010 + S021 + E001 + B004
  -> agency scales and AI reliance/help process candidates
  -> S045 autonomy versus independence
  -> S046 help-behaviour change versus learning/transfer
  -> S047 confidence-rating reactivity
  -> non-composite E001 measurement portfolio
```

## Admitted sources and portfolio effect

The three-source autonomous cap was reached:

1. **S045 — Chen et al. (2013).** In 573 urban and rural Chinese adolescents, self-endorsed motives for both independent and dependent family decisions related positively to need satisfaction and well-being; behavioural independence itself did not. This changes the construct: assistance and agency are not opposite ends of one scale. It is cross-sectional family-decision evidence, not an AI or learning intervention.
2. **S046 — Roll et al. (2011).** Help Tutor feedback reduced faulty help requests from 36% to 26% and bottom-out requests from 70% to 48%, with limited process transfer, but no domain-learning gain or far transfer. This changes interpretation: help-log improvement is not outcome validation. It is historical, small and based on a rule-based geometry tutor.
3. **S047 — Double and Birney (2018/2019).** In a randomized timed-reasoning study of 89 community participants, repeated confidence ratings worsened retrospective calibration and changed response-time strategy conditional on prior confidence, without an overall performance benefit. This changes method: confidence-prompt density must be randomized or sampled, not assumed neutral.

Portfolio effect: the Atlas now has three explicit construct falsifiers. They make E001 more testable without promoting a new trait, composite or product score.

## Held and rejected candidates

- **Reeve and Tseng (2011), DOI `10.1016/j.cedpsych.2011.05.002`: held.** A five-item agentic-engagement scale with reliability and incremental achievement validity in one Taiwanese school. It measures constructive contribution to instruction, not independence or AI resistance; useful for later co-design but less decision-changing under the cap.
- **Zheng et al. (2025), DOI `10.1609/aies.v8i3.36760`: held.** A 12-pattern event taxonomy combines AI correctness/relevance, adoption and final correctness across 315 ChatGPT-4 conversations. One short quiz, 182 learners, a small human-labelled seed and no delayed outcome keep it a behavioural candidate rather than a dependence measure.
- **Viberg et al. (2026), DOI `10.20851/ll.v8.60`: held.** Interviews with 20 Swedish STEM learners suggest need recognition, source choice, help type and evaluation stages. The proposed survey items are preliminary and the publisher PDF endpoint returned HTTP 404.
- **Goh et al. (2025/2026): held.** The GenAI Dependency Scale has multi-study self-report evidence and bounded harm dimensions, but cross-sectional associations, young US/Singapore samples, one-week retest and common-method limits prevent learner diagnosis or causal capability-loss claims.
- **Wu et al. AIDep-22 and other pathology-first scales: rejected for product inference.** Cross-sectional retrospective self-attribution cannot establish that AI caused ability loss, and pathological wording can misclassify legitimate access or high-use contexts.
- **Paula de Barba LinkedIn activity `7494711063209246720`, Sam Illingworth activity `7489957017382531072`, Olga Viberg activity `7434141258266222592`, and *The Atlantic* episode “Why Learn Something That a Machine Can Do for You?”: rejected as empirical evidence.** They exposed useful positions about agency, first-stop help and learner control; linked originals were followed where available.

## Agent disagreement and integration

The scout and evidence analyst preferred a balanced psychometric/process portfolio: Reeve and Tseng, Zheng, and Viberg. The contrarian argued that this would add measures before correcting the assumptions underneath them. The integrating decision admitted S045–S047 because each changes what E001 is allowed to infer:

- independent performance remains important, but cannot define agency;
- help behaviour can be valid process evidence, but cannot stand in for learning;
- confidence can support calibration inference, but its elicitation can change the process.

The held measures remain candidates for later co-design and criterion validation. This disagreement is preserved rather than disguised as lane consensus.

## Claim, belief, experiment and Orqestra change

- **C030:** autonomy is not the inverse of dependence.
- **C031:** improved help-seeking behaviour does not establish learning.
- **C032:** confidence elicitation can change monitoring and control.
- **C010:** now names confidence-prompt reactivity as a boundary.
- **B004:** now treats independence as an observation context, not an agency or virtue score.
- **E001:** now randomizes dense versus sparse/no confidence prompts, distinguishes self-endorsement from assistance, and conditions help-seeking analysis on need and later outcomes.

For Orqestra, preserve separate outcome fields and explanations. Do not label a learner “dependent” because they use AI frequently, “agentic” because they work alone, “well calibrated” because they provide many confidence ratings, or “good at help-seeking” because they follow the interface's preferred request sequence. The next decision is co-design and validation, not instrumentation at scale.

## Uncertainty and falsification plan

The admitted evidence is model-independent and mechanism-relevant, but two studies are historical and none validates a GenAI learning battery. Falsify or narrow the proposed portfolio by testing:

1. incremental prediction over domain accuracy and simpler performance baselines;
2. dense versus sparse/no confidence elicitation for changes in strategy, burden, calibration and learning;
3. support-withdrawal and delayed transfer without removing access-restoring technology;
4. measurement invariance and interpretation across culture, disability/access needs, language, age and prior knowledge;
5. agreement between self-report, interaction logs, learner explanations and independent performance;
6. whether learners understand, correct and contest the resulting record.

## Capability limitations and fallbacks

- The runtime did not expose the intent-level Atlas MCP tools (`research_capabilities`, `discover_sources`, `resolve_source`, `explore_citations`, `extract_source`). The documented `scripts/research_gateway.py` fallback supplied capability checks, identity resolution, lawful locations, hashes and gitignored staging. This run does not claim the missing MCP surface executed.
- OpenAlex and Crossref were available. Unpaywall was unset, so OpenAlex OA locations and native publisher/repository pages were used and labelled. Exa was advertised but not callable.
- Docling was available; deterministic `pdftotext` was used for bounded inspection where extraction stalled or a stable local PDF existed.
- The Roll author PDF had an expired TLS certificate. After DOI and author-host identity verification, it was streamed once with certificate verification disabled into `pdftotext`; the binary was not retained. The gateway record remains metadata-only.
- The Goh publisher page returned HTTP 403; an OSF-hosted author preprint was inspected instead. The Viberg publisher PDF URL returned HTTP 404.
- Podcast Index, YouTube API and OpenAI transcription were unavailable. Publisher pages, RSS/direct URLs and public social pages were discovery/perspective fallbacks; no audio-derived claim was admitted.

## Process lesson and scheduler observation

Open draft PRs remained part of scheduler state. The run fetched `origin/main`, created a dedicated temporary worktree, fast-forwarded through the verified PR #1 and PR #2 heads, and selected queue item 5 from the integrated stack. The user-owned checkout was not edited.

This is actual scheduled observation **3 of 3**. The dedicated record is `research/process-lab/2026-09-22-scheduled-research-scout-observation-3.md`.

The process lesson is substantive: a source portfolio can appear balanced across self-report, logs and qualitative evidence while every lane shares the same invalid construct assumption. A contrarian lane should be able to replace the apparent measurement winners with sources that invalidate the proposed inference.

## Checks

- Canonical index and NotebookLM export regenerated successfully.
- Strict validation: 72 artifacts, 0 errors and 0 warnings.
- Retrieval evaluation: 6 of 6 contracts passed.
- Unit tests: 34 passed.
- Model-dependent freshness register: 10 sources, all explicitly classified.
- `git diff --check`: passed.

No product implementation, learner-data collection, merge or maturity promotion is authorized by this briefing.
