# Weekly research briefing — current-generation independent outcomes

Date: 2026-10-26  
Question: [Q001](../../questions/Q001-when-does-ai-performance-become-learning.md) — which current-generation controlled studies report both assisted and later unassisted GenAI outcomes?

## Decision summary

Admit three sources at the run cap: [S057], [S058] and [S059]. Revise [C001] with a current-system immediate-withdrawal anchor and a lower-confidence 48-hour programming signal. Revise [C002] with a current-system explicit-request null and metacognitive-feedback intervention. Keep both claims provisional in scope: no inspected current-system study establishes delayed novel independent capability, durable deskilling or a universal benefit from feedback.

## Source lanes and why they could change the answer

- **Current-system randomized withdrawal:** Liu et al. could establish whether the performance/independence gap survives stronger GPT-5 assistance and better causal controls.
- **Current-system component and null:** Maier et al. could falsify a simple “AI access causes harm” account and identify an interaction-policy candidate.
- **Delayed authentic task:** Bergh et al. could add a delayed signal outside online arithmetic, while testing whether the gap widens through forgetting.
- **Contradiction and replication:** nulls, positive delayed studies, historical RCTs and large quasi-experiments were actively sought rather than treating adverse results as the only relevant lane.
- **Public discourse:** stable LinkedIn activity IDs and an official APA podcast transcript were sampled because cognitive offloading is contested publicly; they were used to locate and contextualize empirical work, not as effect evidence.

## Search and citation chain

Bounded Atlas retrieval first recovered [C001], [C002], [C009], [C011], [P005], [Q001] and [R001]. The gateway capability check then established that OpenAlex and Crossref were available, while Unpaywall lacked an email, Exa was not callable here, and podcast/video/transcription providers were unavailable.

Gateway and native-web searches combined delayed-retention, independent/unaided performance, controlled design, withdrawal and cognitive-offloading terms in the 2025–2026 window. Exact queries and provider limits are recorded in the [R001 search strategy](../../reviews/R001-learning-performance-gap/search-strategy.md). The most useful backward chain was:

`Bastani / Barcauí / Shen and Tamkin -> Liu -> Maier`

Liu's forward citations did not reveal a delayed replication. Maier explicitly helps explain the disagreement: its assistant required an explicit request for complete answers, while Liu made correct complete answers available with minimal effort.

## Admitted evidence

### S057 — Liu et al., GPT-5 withdrawal experiments

Across three randomized US Prolific experiments, answer-ready GPT-5 improved assisted success. Immediate independent accuracy was then lower after withdrawal in fraction arithmetic and reading. Experiment 2 reduced experiment 1's exclusion and interface confounds; experiment 3 replicated across domain. The result is causal for brief acute withdrawal under this design, not evidence of durable deskilling.

### S058 — Maier et al., metacognitive feedback

In a preregistered five-arm RCT with 704 UK adults and exact GPT-OSS-120B endpoint reporting, AI-only did not significantly underperform no AI when complete answers required an explicit request. Contextual feedback reduced complete-answer offloading and modestly improved immediate unaided performance; a symbolic effort reward did neither. One-sided tests, a bundled intervention and no delayed outcome limit the inference.

### S059 — Bergh et al., programming cognition

Fifty-five analyzed first-year Australian computer-science students scored higher on coding with ChatGPT-4.5 but recalled less about the code immediately and after 48 hours. The group gap was stable, not a faster-forgetting effect. Pseudo-random allocation, no baseline, unequal exposure and uncontrolled answer-generation versus debugging strategies make this a lower-confidence historical-system signal.

## Held and rejected candidates

- **Barcauí, 45-day RCT:** held because the integrating lane could not obtain stable lawful full text from ScienceDirect or SSRN. It remains the most decision-relevant historical delayed candidate.
- **Bassner et al., programming null:** held pending full-article extraction and appraisal of substantial attrition and post-treatment non-use exclusions.
- **Autor et al., three-month patent RCT:** held at official-abstract status after NBER/SSRN access failures.
- **Rismanchian et al., large ALEKS panel:** held as ecological corroboration because AI exposure is inferred rather than observed or randomized.
- **Programming meta-analysis:** held because its search ends in 2025, heterogeneity is high and no-AI assessment effects pool different interventions and delays.
- **Alam thesis:** rejected for claim revision because the randomized sample is 13 with severe baseline imbalance.
- **Sezgünsay nursing pilot:** held as contextual counterevidence; ChatGPT-3.5 is bundled with peer discussion, guidelines, instructor correction and hands-on practice.
- **LinkedIn and podcast positions:** not admitted. Rohan Paul activity `7477277198882590720`, Peter Slattery activity `7479927204328603648`, and APA *Speaking of Psychology* episode 389 added discovery or interpretive context but no causal evidence.

## Agent comparison and epistemic judgment

All three independent read-heavy lanes prioritized Liu. The research scout and evidence analyst also prioritized Maier; the contrarian preferred Barcauí for its 45-day outcome and warned that Bassner's null may be biased by post-treatment exclusions. The scout preferred Bergh as the best fully inspected delayed authentic-task signal. The integrating judgment admitted Liu, Maier and Bergh because together they distinguish immediate harm, immediate null/intervention and delayed weak evidence using full inspected works. Barcauí was not promoted from blocked full-text status.

The disagreement changes the claim boundary: evidence supports “answer-ready assistance can create an immediate or short-delay independent-performance penalty under specific conditions,” not “AI use erodes durable capability generally.”

## Claim-level change

- [C001] now has a current-system causal anchor but explicitly separates acute post-removal performance from retained learning and cumulative deskilling.
- [C002] now has a current-system component anchor. Explicit-request friction and contextual feedback are testable candidates, not a validated recipe.
- [Q001] and queue item 2 now call for a preregistered, multi-session ablation with matched exposure, delayed novel independent tasks and two-sided inference.

## Orqestra relevance

Orqestra should continue to record assistance state and measure independent capability separately from assisted completion. The next product experiment should compare answer-ready help, explicit-request complete answers and contextual feedback while holding task, time and interface transitions constant. Log help tier and complete-answer requests, but do not treat learner-selected usage categories as causal. No production policy change is warranted from this review alone.

## Uncertainty and capability limitations

The evidence base is still dominated by immediate, near tasks. The only admitted 48-hour source is small, historical-system and uses cued recall rather than novel independent coding. No source tests months of ordinary use, far transfer or differential effects for accessibility and prior knowledge.

The intended Atlas intent-level MCP and Exa path were unavailable, so the run used the repository gateway and native web. Unpaywall, Podcast Index, YouTube and transcription providers were unavailable. ScienceDirect and SSRN blocked automated full-text access; no CAPTCHA was bypassed. Docling produced no usable thesis extraction, so lawful local PDF text extraction was used. These failures constrain coverage, not the reported results of inspected works.

## Process lesson and observation state

The fresh `origin/main` base was clean but lagged six open draft research PRs. The integrating lane audited that stack before reserving S057–S059, preserving unrelated checkouts and avoiding collisions. Independent discovery overlapped strongly on Liu and Maier; the main useful disagreement concerned whether to spend the third admission on delayed but weaker evidence.

The first-three scheduled-observation target was already completed in the open draft stack on 2026-09-06, 2026-09-14 and 2026-09-22. This branch reconciles the stale main-base counter to 3/3 and does not manufacture a fourth observation. See the [reconciliation note](../../research/process-lab/2026-10-26-scheduled-observation-counter-reconciliation.md).

## Checks

- `python3 scripts/atlas.py index` — passed; generated indexes and graph refreshed.
- `python3 scripts/atlas.py export notebooklm` — passed.
- `python3 scripts/atlas.py validate --strict` — passed with 60 artifacts, zero errors and zero warnings.
- `python3 scripts/atlas.py eval` — 6/6 retrieval cases passed.
- `python3 -m unittest discover -s tests -v` — 31/31 tests passed.

The freshness-register test was updated from 7 to 10 model-dependent sources, matching the three admissions. The pull request remains draft for human review and will not be merged by the automation.

## Human decisions requested

1. Accept or reject the bounded C001/C002 revisions without promoting either claim beyond provisional scope.
2. Decide whether the next Orqestra research flag should fund the delayed component experiment or first complete formal RoB 2 appraisal of the existing studies.
3. Decide whether to merge the older draft research PR stack before this independent branch so observation history and source identifiers become linear on `main`.

[S057]: ../../sources/notes/S057-liu-ai-assistance-persistence.md
[S058]: ../../sources/notes/S058-maier-metacognitive-feedback.md
[S059]: ../../sources/notes/S059-bergh-programming-cognition.md
[C001]: ../../claims/C001-assisted-performance-is-not-learning.md
[C002]: ../../claims/C002-pedagogical-structure-changes-ai-learning-outcomes.md
