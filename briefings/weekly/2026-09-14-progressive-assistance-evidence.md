# Progressive assistance needs a friction ceiling — 2026-09-14

## Question and existing gap

**Queue item 4:** Which progressive-hint and attempt-before-answer policies have causal evidence in LLM tutoring?

Bounded Atlas retrieval returned P001, C011 and the broader learning-versus-performance chain. The existing evidence gap was sharper than the queue wording implied: S024 tests a bundled binary access gate, not progressive hints; no admitted source isolated an initial attempt, hint granularity, escalation order and final reveal while measuring delayed independent learning.

The initial commands were:

```text
python3 scripts/atlas.py query "Does a post-feedback attempt and progressive assistance improve delayed independent learning?" --type claim --type principle
python3 scripts/atlas.py freshness
python3 scripts/research_gateway.py capabilities
```

## Answer

Current LLM evidence supports **structured help after a diagnosed error**, not a universal refusal to answer. Two field experiments show that interactive or structured support improves next-attempt recovery more clearly than it improves delayed independent learning [C028]. A small current-system study shows a credible opposite failure mode: a GPT-5.2 tutor that never revealed answers produced lower immediate gains, lower helpfulness and progressive disengagement [C029].

P001 should therefore create both a friction floor and a friction ceiling. When the goal is learning and prerequisites/access permit, offer one low-burden attempt or diagnosis before substantive help. Then escalate through hints, explanation, worked example or answer with a visible learner-controlled reveal. Worked-example-first support remains legitimate for novice schema acquisition, diagnostic checking, time pressure and construct-irrelevant access burden.

No admitted study isolates this full policy. The change is a narrower principle and a better experiment, not a maturity promotion.

## Source lanes and search path

Lanes were selected because each could reverse or bound the decision:

- **Large field experiment and delayed outcome:** native search identified the 2026 NUMI/NBER experiment [S042], then Crossref/OpenAlex verified DOI identity and the publisher PDF supplied tables, prompts, trial registration and one-week outcomes.
- **Direct post-error support comparison:** S024 and guard-railed-tutoring citation chains led to the LearnLM/Eedi exploratory RCT [S043], where every arm followed an incorrect attempt and static hints were compared with interactive human or human-supervised AI tutoring.
- **Current-system falsifier:** exact Socratic-versus-answer search found the September 2026 GPT-5.2 experiment [S044], which directly challenges rigid withholding.
- **Null and best-attempt counterpositions:** the scout and contrarian lanes inspected the Bastani guardrail trial, a current expertise-reversal meta-analysis, a worked-example-first experiment, a reflection-before-hint null and the unavailable Bassner and Blasco/Charisi RCTs. These kept the claim at component/bundle level.
- **Practitioner/social:** public LinkedIn activity `7432447285814329346` argued that answer-first use flattens growth and linked company analytics. The stable activity ID and snapshot hash were staged, but affiliation, self-selection and unresolved methods made it a product/discovery perspective only.
- **Podcast:** *My Robot Teacher*, episode 18, 3 September 2026, sampled Leah Belsky's argument for distinguishing productive friction from drudgery. Apple Podcasts Search plus publisher RSS was the Podcast Index fallback. It added a current product-maker perspective, not causal evidence, and was rejected from admission.

Representative exact queries were:

```text
2025 2026 randomized trial LLM tutoring progressive hints attempt before answer delayed independent learning
site:arxiv.org LLM tutor hint progressive feedback randomized learning study 2025 2026
2025 generative AI tutor Socratic hints versus answers experiment learning outcomes
podcast AI tutoring productive struggle hints answers learning 2025 2026
progressive hints attempt before answer generative AI tutor learning
mastery based math LLM tutoring next attempt delayed test
Socratic generative AI tutor direct answers randomized
```

The citation chain was:

```text
P001 + C011 + S024
  -> S001 guard-railed tutor mitigates harm but does not improve independent learning
  -> S042 mastery x AI field experiment and one-week test
  -> S043 static hint vs interactive tutoring after a wrong answer
  -> S044 strict Socratic withholding vs unrestricted GPT-5.2
  -> expertise-reversal and worked-example counterpositions
  -> proposed time-equated component factorial
```

## Admitted sources and portfolio effect

The three-source autonomous cap was reached:

1. **S042 — Oreopoulos et al. (2026), NBER 35621.** In 6,997 middle-school learners, AI improved post-error recovery but slowed progression; mastery alone did not improve delayed learning. Within mastery, the cleanest one-week estimate was 3.2 percentage points on one practiced item (`p=.065`). This adds scale, authentic classrooms and a delayed measure, but the model version is unreported and the tutor is a bundle.
2. **S043 — LearnLM Team and Eedi (2025).** Interactive support after an error sharply beat a static hint on retry and same-topic correction. Human-supervised LearnLM reached 66.2% on the next topic's first item versus 56.2% after a static hint, but every message was human-reviewed and 44.3% of edits addressed pacing. This adds a direct hint comparator and an operational boundary, not autonomous-system evidence.
3. **S044 — Deffarges, Kosmyna and Maes (2026).** In a 50-person GPT-5.2 lab study, unrestricted answers outperformed strict Socratic withholding on an immediate post-test (`d=.80`), while Socratic learners disengaged. This adds a current-system contradiction; small sequential cells, model grading and no delay keep confidence low.

Portfolio effect: the Atlas now contains a large authentic positive mechanism signal, a supervised interactive-tutoring comparison and a current-system negative policy test. The direction is more conditional and more product-useful than adding a fourth paper saying “guardrails matter.”

## Held and rejected candidates

- **Blasco and Charisi, DOI `10.2139/ssrn.5040921`: held.** Direct randomized Socratic-versus-non-Socratic null lead, but SSRN full text returned HTTP 403. Stanford and JRC summaries were inspected only as discovery metadata.
- **Bassner et al., DOI `10.1016/j.caeai.2025.100537`: held.** Highly relevant calibrated-hint null; complete methods remain unavailable.
- **Heickal and Lan, arXiv `2606.08807`: rejected for this claim.** Full paper inspected; reported feedback analyses are associative because exposure follows a failure, and outcomes are repeated submission performance rather than independent learning.
- **Choi et al., arXiv `2512.04630`: rejected for admission.** Useful reflection-before-hint null but only 33 learners activated the support in the main trial and no delayed outcome was measured.
- **Pardos and Bhandari, DOI `10.1371/journal.pone.0304013`: rejected for this pass.** Useful worked-solution counterposition, but 2023 ChatGPT technology and no attempt/escalation manipulation made it less direct than the selected current contradiction.
- **LinkedIn activity `7432447285814329346` and *My Robot Teacher* episode 18: rejected as evidence.** Both shaped the friction-boundary question; neither supplied an independently inspectable causal effect.

## Agent disagreements and integration

- The **research scout** found no full-policy isolation and preferred LearnLM/Eedi plus a reflection-before-hint null and a historical ChatGPT worked-solution counterexample.
- The **evidence analyst** showed that S024 is a direct-answer access gate rather than a hint ladder. It also found an AI-use count discrepancy and an exclusion sensitivity that could shrink the reported effect, supporting retention of low confidence only.
- The **contrarian** preferred an expertise-reversal meta-analysis and a worked-example-first trial, warning that hard gates can burden novices. It proposed immediate worked-example access for schema acquisition and a fast reveal.

The integrating decision admitted S042–S044 because they maximize causal scale, direct hint comparison and current-system falsification. The mechanism sources remain in the briefing and falsification design rather than being laundered into LLM efficacy.

## Claim, principle and Orqestra change

- **C028**: structured post-error AI support improves retry quality more clearly than delayed learning.
- **C029**: rigid answer withholding can impair immediate learning and persistence in a bounded current-system setting.
- **C011** remains provisional/low and now names S044 as a policy-shaped contradiction.
- **P001** remains active/moderate but is narrowed: low-burden attempt when appropriate, explicit worked-example exceptions, fast reveal and pacing threshold.

For Orqestra, the next experiment is a stratified current-model factorial:

1. one low-burden attempt/diagnosis before substantive help versus immediate core-answer/worked-example access with required self-explanation;
2. transparent fixed escalation versus adaptive escalation, both with one-click reveal;
3. identical model, content, interface and accuracy controls, with time/exposure either equated or explicitly decomposed;
4. primary one-week unassisted novel near transfer; secondary four-to-six-week retention, immediate independent performance, completion, external-tool switching, frustration, help-seeking and subgroup interactions for prior knowledge, disability/access need, language and time pressure.

Falsify the attempt gate if it has no practically meaningful delayed advantage or creates differential dropout/burden. Claim adaptivity only if it beats the fixed rule.

## Capability limitations and fallbacks

- The runtime did not expose the intent-level `research_capabilities`, `candidate_inbox`, `discover_sources`, `resolve_source`, `explore_citations` or `extract_source` MCP tools. The documented `research_gateway.py` diagnostic fallback supplied capability discovery, identity resolution, lawful fetch, hashes and gitignored staging. This run does not claim the missing MCP surface executed.
- OpenAlex and Crossref were available. Unpaywall was unset, so OpenAlex OA metadata was used and labelled. Two OpenAlex searches returned HTTP 429; native web, exact DOI/arXiv resolution and publisher pages were the fallback.
- Exa was advertised as a separate MCP but not callable; native web supplied broad discovery.
- Docling was available. Its first NBER extraction returned no output; deterministic `pdftotext` was used to inspect the complete 72-page paper. Docling succeeded for the programming-feedback candidate.
- Podcast Index, YouTube API and OpenAI transcription were unavailable. Apple Podcasts Search, publisher RSS/page and available publisher text were used; no audio-derived claim was admitted.
- SSRN blocked the Blasco/Charisi full text with HTTP 403. The candidate remained held.
- Zotero was a runtime probe and was not used; canonical publisher identifiers and source notes carry this run's provenance.

## Process lesson and scheduler observation

The fresh `origin/main` queue still pointed to Q002 because the first scheduled run is in open draft PR #1. Repeating it would have duplicated recent work. This branch therefore incorporated the verified PR #1 commit and is stacked on its head for review, preserving scheduled observation 1 and making today observation **2 of 3**. New IDs begin at S042/C028 because an unrelated local assessment branch already reserves S029–S041 and C014–C027; no files in that checkout were edited.

The dedicated observation is in `research/process-lab/2026-09-14-scheduled-research-scout-observation-2.md`.

## Checks

- Canonical index and NotebookLM export regenerated successfully.
- Strict validation: 66 artifacts, 0 errors, 0 warnings.
- Retrieval evaluation: 6 of 6 contracts passed.
- Unit tests: 34 passed.
