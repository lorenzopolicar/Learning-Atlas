@AGENTS.md

# Claude Code notes

Reusable workflows live in `.claude/skills`, which points to the canonical `.agents/skills` directory. Specialist agent definitions live in `.claude/agents`.

Shared research MCPs are declared in `.mcp.json`. Approve the project configuration when Claude Code asks. `atlas-research` is local and stages only into the gitignored inbox; Exa is an external discovery server. Credentials belong in the environment, never in `.mcp.json`.

Use the repository harness instead of scanning every Markdown file. Start with `python3 scripts/atlas.py query`, and run the checks in `AGENTS.md` before completing work.
