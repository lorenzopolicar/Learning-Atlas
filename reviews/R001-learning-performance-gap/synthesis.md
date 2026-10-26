# R001 seed synthesis

Status: provisional orientation synthesis; not exhaustive. Updated 2026-10-26.

## What we can say now

Ten comparative studies now make the early picture more heterogeneous. Unrestricted AI assistance can create large supported-performance gains while weakening later unaided performance [S001]. Three short GPT-5 experiments replicate an immediate post-removal accuracy penalty under maximally answer-ready assistance [S057], but do not measure retained learning. Yet ordinary GPT-4o access also improved immediate and one-week unaided performance in a time-held learning task [S015]. In programming, Copilot created a large supported speed/completion advantage without a reliable absolute advantage when the same learners repeated tasks alone one week later [S023]. A small ChatGPT-4.5 study found higher coding scores and lower cued recall immediately and 48 hours later [S059]; the gap was already present immediately, and design limitations prevent a mechanism claim. A tightly designed AI tutor can improve short-term learning relative to a specific active-learning lesson [S002], and a structured, teacher-supported programme can produce meaningful assessment gains in a low-resource secondary context [S005].

The first direct access-timing study reports that delayed access beat always-on access on an immediate independent test while matching no access [S024], but session assignment, exclusion and clustering problems make this a low-confidence component signal. A larger preregistered current-system experiment found no significant AI-only penalty when complete answers required an explicit request; contextual metacognitive feedback reduced answer offloading and improved immediate unaided performance, whereas a symbolic usage reward did neither [S058]. The feedback is bundled and all outcomes are same-session. In an authentic four-hospital South African clinical trial, minimally trained point-of-care GPT-4o access did not improve blinded bedside assessment performance despite high perceived helpfulness [S025]. This is evidence about workflow-bound performance, not a test of a practiced tutor or durable learning.

The synthesis is therefore not “AI helps” or “AI harms,” nor is it “guardrails always beat general access.” The more defensible current statement is that assisted success is not a reliable proxy for independent capability [C001]. Answer-ready access can create an immediate withdrawal penalty, while explicit-request friction plus feedback may alter offloading and same-session performance [C002]. General access can also produce short-delay learning under bounded conditions [C009]. Durability, transfer and the active interaction component remain unresolved.

## Candidate mechanisms

- answer provision may bypass retrieval, generation, error detection, and self-explanation;
- access timing may preserve an initial problem representation and effort before offloading, but transparent fixed timing has not yet been separated from adaptive machinery;
- progressive hints may preserve some of that cognitive work;
- task structure can focus attention and prevent plausible but pedagogically unhelpful responses;
- teacher facilitation may support prompting, interpretation, motivation, classroom management, and error correction;
- increased time-on-task or novelty may contribute to positive programme results;
- holding time fixed may reveal learning-per-unit-time gains that disappear when learners use AI to reduce total study time;
- learner-selected augmentation and automation may mark different mechanisms, but post-treatment use categories cannot establish their causal effects;
- making complete-answer requests explicit may add useful friction, while contextual feedback may interrupt repeated offloading; these components have not been independently randomized;
- assessments aligned closely to the intervention may overstate transfer.

These are mechanism hypotheses, not yet established components.

## Product direction

Build and test an explicit assistance policy rather than a monolithic chatbot. Log support state. Evaluate after support is removed. Preserve a legitimate performance-support mode, but do not use its outputs as silent proof of independent capability [P001, P005].

## What we do not know

- durability over months rather than days or weeks;
- far transfer and authentic performance;
- differential effects by prior knowledge, language, disability, motivation, and socioeconomic context;
- which guardrail components cause benefit;
- how learners adapt strategically over repeated use;
- whether a simple attempt threshold replicates the access-timing result and whether any adaptive policy adds value beyond it;
- whether dependence, calibration, and agency can be measured reliably;
- whether the positive one-week effect in [S015] replicates in ordinary coursework, longer horizons and less selective populations;
- the publication-bias and null-results landscape;
- full appraisal of the 275-participant programming null RCT and the 45-day retention RCT whose lawful full texts were not inspectable in this pass.
- delayed novel independent performance under a current-system answer-ready versus explicit-request versus feedback comparison.

## Next synthesis threshold

Do not strengthen [C002] beyond `provisional` until the review completes reproducible database/citation searches, direct full-text appraisal of the held null/adverse studies, formal risk-of-bias assessment, and at least one independent delayed replication or component ablation for the relevant interaction policy.
