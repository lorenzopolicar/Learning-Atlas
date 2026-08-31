# Source intake runbook

## Discovery

Use scholarly databases, DOI registries, publisher pages, institutional repositories, citation chains, and trial registries. Search engines and AI tools may help discover candidates; they are not evidence.

## Canonical division of labour

- **Zotero:** bibliographic record, collections, full text, annotations, and citation key.
- **Git:** metadata needed for traceability, original appraisal, extracted context, claims, synthesis, and decisions.
- **NotebookLM:** optional generated reading/conversation surface for a human. It receives the research pack and selected lawful source materials; it does not write back as evidence.

Use Better BibTeX or an equivalent stable-key workflow if Zotero is adopted. Export metadata to `sources/bibliography/references.bib`. Never commit copyrighted PDFs.

## Admit a source

1. Verify title, author list, year, venue, DOI/URL, publication status, and corrections or retractions.
2. Read enough of the actual work to describe design, population, intervention, comparator, outcomes, timing, and limitations.
3. Create a source note from the template and add its bibliography entry.
4. Fill the evidence profile with reasons; `unclear` is valid.
5. Add the narrowest candidate claim. Do not let the paper’s title determine claim wording.
6. If part of a review, update search, screening, and extraction records.
7. Run validation.

## NotebookLM workflow

Generate `exports/notebooklm/learning-atlas-research-pack.md` and upload it as one source. Add selected open-access originals or Drive documents separately when useful. Ask NotebookLM for disagreements, citations, missing boundary conditions, or questions—not new facts to paste unverified into Git.

If Google Drive is later connected, the generated pack may be mirrored there for convenient refresh. Git remains canonical because it preserves reviewable diffs and typed provenance.
