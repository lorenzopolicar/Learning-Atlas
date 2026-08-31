---
{
  "id": "D001",
  "type": "decision",
  "title": "Use Git as the canonical synthesis store",
  "status": "active",
  "date": "2026-08-31",
  "topics": ["ethics-and-governance", "institutional-design"],
  "principles": ["P002", "P007"],
  "related_claims": ["C007", "C008"],
  "supersedes": []
}
---

# D001 — Use Git as the canonical synthesis store

## Context

The atlas needs durable provenance, agent-readable artifacts, human review, diffs, and a route into product repositories. Literature tools and conversational notebooks solve adjacent problems but do not provide the complete publication boundary.

## Decision

Git is canonical for original synthesis and typed relationships. Zotero is the canonical bibliographic/PDF/annotation record. NotebookLM is an optional, generated human exploration surface. Neither NotebookLM answers nor model summaries can write evidence directly into the atlas.

## Evidence and principles

This follows the evidence-ledger and research-traceability principles [P002, P007]. The same separation of observation from inference that protects a learner model [C007] protects the research system.

## Alternatives considered

- NotebookLM as source of truth: strong grounded conversation, weak versioned publication and write-back controls.
- Notion or Drive as source of truth: approachable collaboration, weaker deterministic validation and agent-native diffs.
- Zotero alone: excellent literature record, insufficient claim/belief/principle graph.

## Consequences and revisit trigger

Generated packs and indexes must remain reproducible from Git. Revisit if a knowledge platform can preserve typed provenance, local portability, review gates, and deterministic agent access with materially lower maintenance.
