# Orqestra bridge

Learning Atlas supplies the evidence and design reasoning for the learning engine in `/Users/lorenzo.policar/Developer/emtech-noema`. It does not couple itself to Noema’s implementation or write into that repository during autonomous research.

## Shared thesis

Orqestra can connect person, context, work, observed gaps, intervention, later performance, and an updated learner model. The scarce asset is an evidence-backed representation of capability and how it changes—not generated course volume.

## Current map

| Orqestra concern | Atlas guidance | Design question |
|---|---|---|
| learning generation | [P001], [P003], [P004] | Does generated material preserve the work required for the target capability and adapt/fade support? |
| learning domain and capability model | [P002], [P006], [B003], [B004] | Are observations separated from inferences, including assistance state, context, uncertainty, and permitted use? |
| learning runtime | [P001], [P004], [P005] | Does orchestration support attempts, retrieval, revisits, and later independent checks? |
| personalization | [P003], [B005] | Does adaptation beat a strong transparent default on a declared outcome? |
| assessment and evidence | [P005], [P006] | Are supported performance, independent capability, delay, and transfer visibly distinguished? |
| product analytics | [C001], [P005] | Are completion, engagement, and assisted correctness being mistaken for learning? |
| human-AI capability | [B004], [C009], [N001] | What must the learner notice, decide, justify, and recover from for delegation to count as responsible capability? |
| AI literacy coverage | [S016], [N001] | Does the experience develop critical engagement, creation, task allocation, evaluation, agency, and the ability to shape systems—not only tool fluency? |

## Consult from Noema

The repository skill `.agents/skills/consult-learning-atlas` can be linked into the user-level agent skill directory so Codex and Claude can activate it from either project.

Direct query:

```bash
python3 /Users/lorenzo.policar/Projects/learning-atlas/scripts/atlas.py query \
  "adaptive feedback learner evidence delayed transfer" \
  --type claim --type belief --type principle
```

For Claude Code, add the atlas as an additional directory when a deeper consultation is explicitly needed:

```bash
claude --add-dir /Users/lorenzo.policar/Projects/learning-atlas
```

Do not make the full atlas an unconditional Noema prompt dependency. Use the bounded query first, cite selected IDs in a Noema decision or implementation plan, and keep the source context available by path.

## Feedback from product to research

Noema can contribute:

- anonymized aggregate experiment results;
- operational boundary conditions and failure modes;
- questions created by implementation;
- evidence that a recommendation changes behaviour but not learning;
- comparative results for simple versus personalized policies.

No learner-identifiable data enters the public atlas. A product result should include intervention, comparator, outcome, support state, timing, exclusions, and context before it can challenge a claim.

## First product experiments

1. Progressive hints versus answer-first support, measured on a later unaided task [P001, P005].
2. Simple fixed scaffold versus evidence-based fading [P003, B005].
3. Learner evidence ledger versus current state representation, evaluated for auditability, correction, and recommendation quality [P002].
4. Separate independent and AI-assisted capability estimates, evaluated for calibration and decision usefulness [B004, P006].
5. Capability-sovereignty probe: compare an artifact-only assessment with evidence of task decomposition, rejected AI outputs, justification, and recovery after tool removal [N001, C008].
