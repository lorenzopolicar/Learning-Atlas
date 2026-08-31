# Scheduled automations

The Codex desktop app owns execution and reporting. Times use the local Australia/Brisbane wall clock. Keep the desktop app running for local schedules.

| Automation | Schedule | Purpose |
|---|---|---|
| Learning Atlas weekly research scout | Sunday, 07:30 | Advance one queue item, admit at most three sources, update claims/review, publish a briefing and draft PR |
| Learning Atlas monthly synthesis | First Saturday, 09:00 | Review evidence changes, contradictions, beliefs, principles, Orqestra implications, and human decisions |
| Learning Atlas quarterly direction review | First Sunday every three months, 10:00 | Audit agenda, portfolio balance, staleness, graph integrity, and next-quarter direction |

Each scheduled run is instructed to use a dedicated Git worktree and unique branch, validate all generated views, report into the Scheduled inbox, and never merge its own pull request.

The automations currently run against the saved `Projects` parent in Codex and explicitly target `/Users/lorenzo.policar/Projects/learning-atlas`. If Learning Atlas is later saved as its own Codex project, retarget the automations to that project so Codex can provide native project worktree isolation.
