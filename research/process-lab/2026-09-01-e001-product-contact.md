# E001 product-contact pass — 2026-09-01

## Purpose

Put the Atlas's AI-mediated stewardship recommendation into contact with Orqestra's real learning data model, without mutating a dirty product checkout or prematurely turning a research construct into a learner score.

## What was inspected

Read-only inspection of `/Users/lorenzo.policar/Developer/emtech-noema`, branch `learning-upgrade`, focused on:

- `packages/noema-db/src/schema.ts` (`CourseEnrollment`, `AssessmentResult`);
- `apps/noema/lib/learn/assessment-scoring.ts` (course score, assessment aggregation, coarse maximum Bloom derivation);
- `apps/noema/lib/actions/learn/assessment-actions.ts` (pre/post persistence and learning-gain update).

The checkout contained substantial user-owned changes unrelated to this pass, so no Orqestra file was edited.

## Decision

Do not add stewardship fields to the existing summary records. Use a separate, append-only, research-flagged E001 event store with a pseudonymous identity boundary. Keep corrections as new events, make every event visible and contestable, and enforce prohibited uses in code before a learner pilot.

The [pilot package](../../experiments/E001-ai-mediated-stewardship-probe/pilot-package.md) now includes a JSON Schema `0.1.0`, an assisted trial, a delayed accessible-independent follow-up that preserves a screen reader, a learner-contested correction, Orqestra seam guidance, delivery gates and stop conditions.

## Verification

- All three fixtures passed `check-jsonschema` against draft 2020-12.
- Repository tests assert the pilot's non-negotiable boundaries: low stakes, no ranking/credential/employment/silent-mastery use, access support preservation, learner visibility and contestability.
- Conditional tests require provenance and pre/post decision state for AI-assisted observations, substantive generation removal for the delayed independent lane, and append-only reference for corrections.

## Lessons

1. **A schema is an epistemic intervention.** Requiring intended inference, prohibited inference, expiry and uncertainty prevents a convenient event log from silently becoming a trait model.
2. **Accessibility must be represented functionally.** The delayed-independent fixture retains screen-reader support and removes substantive generation; “no tools” would confound the construct.
3. **Correction semantics belong in the first version.** Adding contestability after scoring systems harden is much harder than making observations append-only from the pilot.
4. **Research instrumentation should have a separate product seam.** Extending familiar assessment tables would be faster but would invite downstream reuse before validity is established.
5. **Authored advice is the cleaner first manipulation.** A live model adds version, sampling and retrieval variance before the underlying stewardship measures have been tested.

## Limitations and next falsification step

The schema is synthetic and contract-valid, not learner-valid. No task bank, advisory-group review, comprehension test, privacy threat model, retention enforcement, powered analysis or Orqestra architecture review has happened. The next legitimate step is learner/domain/accessibility co-design followed by pre-registration. Product implementation before those steps would turn a design hypothesis into infrastructure too early.
