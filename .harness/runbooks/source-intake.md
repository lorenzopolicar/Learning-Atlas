# Source intake runbook

## Discovery

Use scholarly databases, DOI registries, publisher pages, institutional repositories, citation chains, trial registries, podcast feeds, official transcripts or captions, book catalogues, standards bodies, datasets, and relevant practitioner publications. Search engines and AI tools may help discover candidates; they are not evidence.

Start by calling `research_capabilities`, then route through `.agents/skills/atlas-research/references/tool-routing.md`. Use `candidate_inbox` with `action=stage` to create a local candidate record before admission. The inbox is gitignored and deliberately separate from canonical source notes.

## Canonical division of labour

- **Zotero:** bibliographic record, collections, full text, annotations, and citation key.
- **Git:** metadata needed for traceability, original appraisal, extracted context, claims, synthesis, and decisions.
- **NotebookLM:** optional generated reading/conversation surface for a human. It receives the research pack and selected lawful source materials; it does not write back as evidence.

Use Better BibTeX or an equivalent stable-key workflow if Zotero is adopted. Export metadata to `sources/bibliography/references.bib`. Never commit copyrighted PDFs.

## Admit a source

1. Verify title, creators or speakers, date, container, canonical identifier/URL, publication status, rights, and corrections or retractions when relevant. Classify technology dependence.
2. Inspect the actual content. For empirical work, describe design, population, intervention, comparator, outcomes, timing, and limitations. For discourse or testimony, describe the speaker's standing, context, argument, counterposition, and epistemic role.
3. Preserve a page, section, table, dataset-row, or timestamp locator for consequential observations. For model-dependent AI work, separately record exact system/version, data-collection period, assessed temporal relevance, review date, and which implications may not transfer to current systems.
4. Create a source note with the closest profile and add its bibliography entry:
   `python3 scripts/atlas.py new source <slug> --source-profile empirical|media|social|book|dataset`.
5. Fill the evidence profile for empirical work; `unclear` is valid. For other source types, record limitations and what the source cannot establish.
6. Add the narrowest candidate claim, belief, discourse tension, or question appropriate to the epistemic role.
7. If the source mentions research, resolve the original work before treating the statement as evidence.
8. If part of a review, update search, screening, and extraction records.
9. Run validation.

## Media-specific intake

- Prefer publisher transcripts or official captions. Label automatic transcripts with engine, version, date, language, and speaker/timestamp uncertainty.
- Store full transcripts and authorized media only in `.harness/inbox/`, Zotero, Drive, or another private lawful store. Never commit them.
- Use short excerpts only when needed for analysis and retain timestamp locators.
- A media source may revise a belief or open a question without supporting an empirical claim. That is legitimate progress.

## Social and practitioner intake

- Use native web or Exa for discovery. Public X and LinkedIn pages can be normalized as `social-post` candidates; use a signed-in browser only when public retrieval is incomplete and access is authorized.
- Record a stable post identifier, author, publication time, retrieval time, content hash, scope inspected, and snapshot limitations.
- Engagement may justify sampling a culturally influential position, but it never increases evidentiary weight.
- Follow linked papers, datasets, policies, products, and reports to their originals. A post can be admitted as argument or testimony while its empirical claims remain unresolved leads.

## NotebookLM workflow

Generate `exports/notebooklm/learning-atlas-research-pack.md` and upload it as one source. Add selected open-access originals or Drive documents separately when useful. Ask NotebookLM for disagreements, citations, missing boundary conditions, or questions—not new facts to paste unverified into Git.

If Google Drive is later connected, the generated pack may be mirrored there for convenient refresh. Git remains canonical because it preserves reviewable diffs and typed provenance.
