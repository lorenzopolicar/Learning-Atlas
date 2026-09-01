# How to work with the Learning Atlas

The Atlas supports two complementary modes: use what it already knows, or ask it to improve what it knows. You do not need to translate your question into repository commands first. Start with the decision, curiosity, or product problem in plain language.

## See what changed

Run:

```bash
python3 scripts/atlas.py recent --limit 5
```

This is the compact change feed: recent research passes, the question each pass addressed, sources admitted, the briefing, and the interpretation of what changed. For a quick maturity snapshot, use `python3 scripts/atlas.py status`.

Useful prompts for an agent include:

- “What has the Learning Atlas learned since I last checked? Focus on belief or product-principle changes.”
- “Give me the newest evidence, contradictions, and open questions about learner agency.”
- “Show only recent work that could change Orqestra product decisions.”

The run ledger in `.harness/state/research-state.json` is authoritative. Briefings explain the change; source and claim artifacts carry the evidence chain.

## Consult it for a product decision

Ask Codex or Claude to use the `consult-learning-atlas` skill and describe the actual design decision. Good requests name the learner, task, desired capability, and decision horizon.

Example:

> Use the Learning Atlas to review a feature that gives students an AI-generated answer after one failed attempt. I want durable independent performance, not just task completion. Return the relevant principles, evidence boundaries, risks, instrumentation, and a falsification plan.

The consultation should return a bounded set of artifact IDs and explicit uncertainty. It should not load the whole repository or silently treat an Atlas belief as settled fact.

## Explore an idea or learn a topic

Start with what you are trying to understand and why. The agent should query the local Atlas before searching externally, distinguish what is already known from the gap, and leave you with a map rather than a pile of links.

Example:

> I want to develop my thinking about whether struggle is necessary for learning in AI-mediated environments. Map the strongest positions, what evidence distinguishes them, and the implications for tutor behavior. Do not change the Atlas yet.

If the exploration becomes valuable, follow with:

> Turn the unresolved parts of that map into candidate questions in the research queue. Explain what would make each question worth promoting.

## Commission a research pass

Invoke the `atlas-research` skill explicitly when you want canonical knowledge to change.

Example:

> Use atlas-research to investigate whether progressively revealing hints improve later unassisted transfer compared with answer-giving. Inspect primary sources, seek nulls and contradictions, admit at most three sources, update only warranted claims, publish a briefing, and leave maturity promotions for review.

A full pass should query the existing corpus, state the gap, inspect the real sources, preserve lawful provenance, synthesize rather than merely collect, update the run ledger, regenerate derived views, and pass validation and tests.

## Give it a seed

A seed can be a paper, book, dataset, podcast episode, talk, X thread, LinkedIn post, observation, or hunch. Say what drew your attention and whether you want intake, exploration, or canonical synthesis.

Examples:

- “Capture this podcast as a candidate. Verify the episode and transcript, extract timestamped positions, but do not treat expert commentary as causal evidence.”
- “Trace the empirical studies behind this LinkedIn claim and tell me whether the post represents them fairly.”
- “This learner behavior surprised me. Record it as a signal and propose competing explanations without generalizing from one observation.”

Public discourse and media can reveal language, mechanisms, lived experience, and discovery leads. Their evidentiary role stays explicit; popularity never substitutes for study quality.

## Evolve the agenda

The agenda is a revisable portfolio, not a static syllabus. Add or reprioritize work when product decisions, evidence gaps, contradictions, field changes, neglected populations, or promising falsification opportunities warrant it. Material direction changes go in `research/agenda-ledger.md`; the near-term execution order lives in `research/queue.md`.

Ask for an agenda review when the portfolio feels stale or over-concentrated:

> Review the Atlas agenda against current Orqestra decisions and recent research. Identify blind spots, duplicated questions, neglected source lanes and populations, and questions whose answers would no longer change a decision. Propose changes; do not apply material programme changes without my review.

## Publication boundary

Agents may capture, research, challenge, synthesize, and propose. They may not silently turn a fragile result into an established claim, collapse normative judgment into empirical fact, or merge their own maturity changes. The Atlas is designed to accumulate judgment, not just content; human review remains the boundary for consequential belief, principle, and agenda changes.
