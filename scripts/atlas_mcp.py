#!/usr/bin/env python3
"""Thin stdio MCP surface over the Learning Atlas research gateway."""

from __future__ import annotations

import json
import sys
from typing import Any, Callable

import research_gateway as gateway


SERVER_INSTRUCTIONS = (
    "Use these tools for deterministic transport, identity, provenance, lawful storage, and bounded extraction. "
    "The reviewing agent—not the gateway—decides relevance, epistemic role, source quality, contradictions, and admission. "
    "A staged candidate is not Atlas evidence. Never promote claims from snippets, metadata, abstracts, social popularity, "
    "or transcripts alone. Follow empirical references to originals and preserve pages, timestamps, rights, and uncertainty."
)


def object_schema(properties: dict[str, Any], required: list[str] | None = None) -> dict[str, Any]:
    return {"type": "object", "properties": properties, "required": required or [], "additionalProperties": False}


READ_ONLY = {"readOnlyHint": True, "destructiveHint": False, "idempotentHint": True, "openWorldHint": True}
LOCAL_READ = {**READ_ONLY, "openWorldHint": False}
WRITE_LOCAL = {"readOnlyHint": False, "destructiveHint": False, "idempotentHint": True, "openWorldHint": False}


TOOLS: list[dict[str, Any]] = [
    {
        "name": "research_capabilities",
        "description": "Report configured research providers, missing credentials, extraction fallbacks, and storage boundaries.",
        "inputSchema": object_schema({}),
        "annotations": LOCAL_READ,
    },
    {
        "name": "discover_sources",
        "description": "Find metadata leads in one explicit lane. Use native web or Exa for broad web, social, book, and discourse discovery.",
        "inputSchema": object_schema(
            {
                "lane": {"type": "string", "enum": ["scholarly", "podcasts", "videos"]},
                "query": {"type": "string", "minLength": 1},
                "limit": {"type": "integer", "minimum": 1, "maximum": 20, "default": 5},
                "from_year": {"type": "integer", "minimum": 1800, "maximum": 2200},
                "to_year": {"type": "integer", "minimum": 1800, "maximum": 2200},
            },
            ["lane", "query"],
        ),
        "annotations": READ_ONLY,
    },
    {
        "name": "resolve_source",
        "description": "Resolve one source through an agent-selected lane. Returns a candidate envelope; it does not assign evidentiary authority.",
        "inputSchema": object_schema(
            {
                "lane": {"type": "string", "enum": ["scholarly", "media", "feed", "web"]},
                "value": {"type": "string", "minLength": 1},
                "source_type": {"type": "string", "enum": sorted(gateway.SOURCE_TYPES), "default": "web-essay"},
                "limit": {"type": "integer", "minimum": 1, "maximum": 50, "default": 10},
                "query": {"type": "string", "description": "Optional episode terms when resolving a feed."},
            },
            ["lane", "value"],
        ),
        "annotations": READ_ONLY,
    },
    {
        "name": "explore_citations",
        "description": "Traverse one OpenAlex work backward or forward for citation chaining. Results remain discovery leads.",
        "inputSchema": object_schema(
            {
                "openalex_id": {"type": "string", "pattern": "^W[0-9]+$"},
                "direction": {"type": "string", "enum": ["cited_by", "references"], "default": "cited_by"},
                "limit": {"type": "integer", "minimum": 1, "maximum": 20, "default": 10},
            },
            ["openalex_id"],
        ),
        "annotations": READ_ONLY,
    },
    {
        "name": "extract_source",
        "description": "Return bounded navigation excerpts and locators from an authorized document or transcript.",
        "inputSchema": object_schema(
            {
                "kind": {"type": "string", "enum": ["document", "transcript"]},
                "source": {"type": "string", "minLength": 1},
                "max_excerpts": {"type": "integer", "minimum": 1, "maximum": 20, "default": 5},
                "max_segments": {"type": "integer", "minimum": 1, "maximum": 500, "default": 50},
                "max_chars": {"type": "integer", "minimum": 500, "maximum": 20000, "default": 4000},
                "max_pages": {"type": "integer", "minimum": 1, "maximum": 100, "default": 20},
            },
            ["kind", "source"],
        ),
        "annotations": READ_ONLY,
    },
    {
        "name": "fetch_lawful_document",
        "description": "Fetch a rights-cleared document into the gitignored inbox and write a hash-and-rights receipt.",
        "inputSchema": object_schema(
            {
                "url": {"type": "string", "format": "uri"},
                "rights_basis": {"type": "string", "enum": sorted(gateway.RIGHTS_BASES)},
            },
            ["url", "rights_basis"],
        ),
        "annotations": {**WRITE_LOCAL, "openWorldHint": True},
    },
    {
        "name": "transcribe_media",
        "description": "Transcribe authorized local audio/video; full output remains in the gitignored inbox and only bounded results should enter Git.",
        "inputSchema": object_schema(
            {
                "source": {"type": "string", "minLength": 1},
                "diarize": {"type": "boolean", "default": True},
                "language": {"type": "string", "minLength": 2, "maxLength": 10},
            },
            ["source"],
        ),
        "annotations": {**WRITE_LOCAL, "openWorldHint": True},
    },
    {
        "name": "search_zotero",
        "description": "Search the local Zotero library read-only when its local API is enabled.",
        "inputSchema": object_schema(
            {"query": {"type": "string", "minLength": 1}, "limit": {"type": "integer", "minimum": 1, "maximum": 50, "default": 10}},
            ["query"],
        ),
        "annotations": LOCAL_READ,
    },
    {
        "name": "candidate_inbox",
        "description": "Stage, list, or deterministically merge candidate envelopes. None of these actions admits a source to the Atlas.",
        "inputSchema": object_schema(
            {
                "action": {"type": "string", "enum": ["stage", "list", "merge"]},
                "candidate": {"type": "object"},
                "candidates": {"type": "array", "minItems": 2, "items": {"type": "object"}},
                "limit": {"type": "integer", "minimum": 1, "maximum": 200, "default": 50},
            },
            ["action"],
        ),
        "annotations": WRITE_LOCAL,
    },
]


def _discover(arguments: dict[str, Any]) -> Any:
    lane = arguments["lane"]
    if lane == "scholarly":
        return gateway.discover_works(
            arguments["query"], arguments.get("limit", 5), arguments.get("from_year"), arguments.get("to_year")
        )
    if lane == "podcasts":
        return gateway.discover_podcasts(arguments["query"], arguments.get("limit", 5))
    return gateway.discover_videos(arguments["query"], arguments.get("limit", 5))


def _resolve(arguments: dict[str, Any]) -> Any:
    lane, value = arguments["lane"], arguments["value"]
    if lane == "scholarly":
        return gateway.resolve_scholarly_work(value)
    if lane == "media":
        return gateway.resolve_media_source(value)
    if lane == "feed":
        return gateway.resolve_feed(value, arguments.get("limit", 10), arguments.get("query"))
    return gateway.inspect_url(value, arguments.get("source_type", "web-essay"))


def _extract(arguments: dict[str, Any]) -> Any:
    if arguments["kind"] == "transcript":
        return gateway.extract_transcript(
            arguments["source"], arguments.get("max_excerpts", 5), arguments.get("max_segments", 50)
        )
    return gateway.extract_document(arguments["source"], arguments.get("max_chars", 4_000), arguments.get("max_pages", 20))


def _candidate_inbox(arguments: dict[str, Any]) -> Any:
    action = arguments["action"]
    if action == "list":
        return gateway.list_candidates(arguments.get("limit", 50))
    if action == "stage":
        if not isinstance(arguments.get("candidate"), dict):
            raise gateway.GatewayError("candidate is required when action=stage")
        return gateway.stage_candidate(arguments["candidate"])
    candidates = arguments.get("candidates")
    if not isinstance(candidates, list) or len(candidates) < 2:
        raise gateway.GatewayError("at least two candidates are required when action=merge")
    return gateway.merge_candidates(*candidates)


def call_tool(name: str, arguments: dict[str, Any]) -> Any:
    calls: dict[str, Callable[[], Any]] = {
        "research_capabilities": gateway.capabilities,
        "discover_sources": lambda: _discover(arguments),
        "resolve_source": lambda: _resolve(arguments),
        "explore_citations": lambda: gateway.citation_neighborhood(
            arguments["openalex_id"], arguments.get("direction", "cited_by"), arguments.get("limit", 10)
        ),
        "extract_source": lambda: _extract(arguments),
        "fetch_lawful_document": lambda: gateway.fetch_lawful_document(arguments["url"], arguments["rights_basis"]),
        "transcribe_media": lambda: gateway.transcribe_media(
            arguments["source"], arguments.get("diarize", True), arguments.get("language")
        ),
        "search_zotero": lambda: gateway.zotero_search(arguments["query"], arguments.get("limit", 10)),
        "candidate_inbox": lambda: _candidate_inbox(arguments),
    }
    if name not in calls:
        raise gateway.GatewayError(f"Unknown tool: {name}")
    return calls[name]()


def result_message(request_id: Any, result: Any) -> dict[str, Any]:
    return {"jsonrpc": "2.0", "id": request_id, "result": result}


def error_message(request_id: Any, code: int, message: str) -> dict[str, Any]:
    return {"jsonrpc": "2.0", "id": request_id, "error": {"code": code, "message": message}}


def handle(message: dict[str, Any]) -> dict[str, Any] | None:
    method = message.get("method")
    request_id = message.get("id")
    if method == "notifications/initialized":
        return None
    if method == "ping":
        return result_message(request_id, {})
    if method == "initialize":
        requested = (message.get("params") or {}).get("protocolVersion")
        return result_message(
            request_id,
            {
                "protocolVersion": requested or "2025-03-26",
                "capabilities": {"tools": {"listChanged": False}},
                "serverInfo": {"name": "learning-atlas-research", "version": "2.0.0"},
                "instructions": SERVER_INSTRUCTIONS,
            },
        )
    if method == "tools/list":
        return result_message(request_id, {"tools": TOOLS})
    if method == "tools/call":
        params = message.get("params") or {}
        try:
            payload = call_tool(str(params.get("name") or ""), params.get("arguments") or {})
            return result_message(
                request_id,
                {"content": [{"type": "text", "text": json.dumps(payload, indent=2, ensure_ascii=False)}], "isError": False},
            )
        except (gateway.GatewayError, KeyError, TypeError, ValueError) as exc:
            return result_message(
                request_id,
                {"content": [{"type": "text", "text": json.dumps({"error": str(exc)}, ensure_ascii=False)}], "isError": True},
            )
    if request_id is None:
        return None
    return error_message(request_id, -32601, f"Method not found: {method}")


def main() -> int:
    for raw in sys.stdin:
        if not raw.strip():
            continue
        message: dict[str, Any] = {}
        try:
            message = json.loads(raw)
            if not isinstance(message, dict):
                raise ValueError("JSON-RPC message must be an object")
            response = handle(message)
        except (json.JSONDecodeError, ValueError) as exc:
            response = error_message(None, -32700, f"Parse error: {exc}")
        except Exception as exc:  # Keep stdio alive while surfacing a bounded error.
            response = error_message(message.get("id"), -32603, str(exc))
        if response is not None:
            sys.stdout.write(json.dumps(response, separators=(",", ":"), ensure_ascii=False) + "\n")
            sys.stdout.flush()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
