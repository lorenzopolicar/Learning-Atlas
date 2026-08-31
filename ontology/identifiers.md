# Identifiers and filenames

- Use the next unused three-digit ID for each type, such as `C009`.
- Filename format is `<ID>-<short-kebab-case-title>.md`.
- IDs are immutable and never recycled, including after retirement.
- A source’s `citation_key` should match the key in `sources/bibliography/references.bib` and Zotero.
- Dates use ISO 8601 (`YYYY-MM-DD`).
- Artifact metadata is JSON inside Markdown frontmatter. JSON is valid YAML and lets the dependency-free harness parse it deterministically.

Use `python3 scripts/atlas.py next-id claim` or `python3 scripts/atlas.py new claim <slug>` rather than guessing.
