#!/usr/bin/env python3
"""Minimal stdio MCP server for the Learning Atlas research gateway."""

from __future__ import annotations

import json
import sys
from typing import Any, Callable

import research_gateway as gateway


SERVER_INSTRUCTIONS = (
    "Discover and inspect sources, then stage normalized candidates. Staging is not evidence admission. "
    "Never promote claims from snippets, metadata, abstracts, or transcripts alone. Preserve pages/timestamps, "
    "epistemic role, rights, corrections, and uncertainty. Full text and transcripts stay in the gitignored inbox."
)


def object_schema(properties: dict[str, Any], required: list[str] | None = None) -> dict[str, Any]:
    return {"type": "object", "properties": properties, "required": required or [], "additionalProperties": False}


TOOLS: list[dict[str, Any]] = [
    {
        "name": "research_capabilities",
        "description": "Report configured providers, missing credentials, extraction fallbacks, and storage boundaries.",
        "inputSchema": object_schema({}),
        "annotations": {"readOnlyHint": True, "destructiveHint": False, "idempotentHint": True, "openWorldHint": False},
    },
    {
        "name": "discover_works",
        "description": "Discover scholarly source candidates through OpenAlex. Results are metadata leads, not admitted evidence.",
        "inputSchema": object_schema(
            {
                "query": {"type": "string", "minLength": 1},
                "limit": {"type": "integer", "minimum": 1, "maximum": 20, "default": 5},
                "from_year": {"type": "integer", "minimum": 1800, "maximum": 2200},
                "to_year": {"type": "integer", "minimum": 1800, "maximum": 2200},
            },
            ["query"],
        ),
        "annotations": {"readOnlyHint": True, "destructiveHint": False, "idempotentHint": True, "openWorldHint": True},
    },
    {
        "name": "verify_doi",
        "description": "Resolve a DOI in Crossref and check metadata plus update/correction/retraction relationships.",
        "inputSchema": object_schema({"doi": {"type": "string", "minLength": 4}}, ["doi"]),
        "annotations": {"readOnlyHint": True, "destructiveHint": False, "idempotentHint": True, "openWorldHint": True},
    },
    {
        "name": "resolve_scholarly_work",
        "description": "Resolve and deduplicate one DOI across Crossref, OpenAlex, and the configured lawful-access provider.",
        "inputSchema": object_schema({"doi": {"type": "string", "minLength": 4}}, ["doi"]),
        "annotations": {"readOnlyHint": True, "destructiveHint": False, "idempotentHint": True, "openWorldHint": True},
    },
    {
        "name": "citation_neighborhood",
        "description": "Retrieve works citing or referenced by an OpenAlex work for backward/forward citation chaining.",
        "inputSchema": object_schema(
            {
                "openalex_id": {"type": "string", "pattern": "^W[0-9]+$"},
                "direction": {"type": "string", "enum": ["cited_by", "references"], "default": "cited_by"},
                "limit": {"type": "integer", "minimum": 1, "maximum": 20, "default": 10},
            },
            ["openalex_id"],
        ),
        "annotations": {"readOnlyHint": True, "destructiveHint": False, "idempotentHint": True, "openWorldHint": True},
    },
    {
        "name": "find_open_access",
        "description": "Find a lawful open-access location for a DOI using Unpaywall when configured, otherwise OpenAlex.",
        "inputSchema": object_schema({"doi": {"type": "string", "minLength": 4}}, ["doi"]),
        "annotations": {"readOnlyHint": True, "destructiveHint": False, "idempotentHint": True, "openWorldHint": True},
    },
    {
        "name": "merge_source_candidates",
        "description": "Merge provider records for the same canonical source into one deduplicated candidate while preserving checks and warnings.",
        "inputSchema": object_schema(
            {"candidates": {"type": "array", "minItems": 2, "items": {"type": "object"}}},
            ["candidates"],
        ),
        "annotations": {"readOnlyHint": True, "destructiveHint": False, "idempotentHint": True, "openWorldHint": False},
    },
    {
        "name": "discover_podcasts",
        "description": "Discover podcast series through Podcast Index when configured, with Apple Podcasts as an explicit fallback.",
        "inputSchema": object_schema(
            {"query": {"type": "string", "minLength": 1}, "limit": {"type": "integer", "minimum": 1, "maximum": 20, "default": 5}},
            ["query"],
        ),
        "annotations": {"readOnlyHint": True, "destructiveHint": False, "idempotentHint": True, "openWorldHint": True},
    },
    {
        "name": "discover_captioned_videos",
        "description": "Discover captioned YouTube videos when YOUTUBE_API_KEY is configured; otherwise reports the safer fallback route.",
        "inputSchema": object_schema(
            {"query": {"type": "string", "minLength": 1}, "limit": {"type": "integer", "minimum": 1, "maximum": 20, "default": 5}},
            ["query"],
        ),
        "annotations": {"readOnlyHint": True, "destructiveHint": False, "idempotentHint": True, "openWorldHint": True},
    },
    {
        "name": "resolve_podcast_feed",
        "description": "Resolve recent episodes, media enclosures, and Podcasting 2.0 transcript links from a public RSS/Atom feed.",
        "inputSchema": object_schema(
            {
                "url": {"type": "string", "format": "uri"},
                "limit": {"type": "integer", "minimum": 1, "maximum": 50, "default": 10},
                "query": {"type": "string", "description": "Optional title/description terms used to find an older episode in the feed."},
            },
            ["url"],
        ),
        "annotations": {"readOnlyHint": True, "destructiveHint": False, "idempotentHint": True, "openWorldHint": True},
    },
    {
        "name": "inspect_source_url",
        "description": "Inspect a publisher page, detect transcript-like timestamps, hash retrieved content, and return a bounded candidate record.",
        "inputSchema": object_schema(
            {
                "url": {"type": "string", "format": "uri"},
                "source_type": {"type": "string", "enum": sorted(gateway.SOURCE_TYPES), "default": "web-essay"},
            },
            ["url"],
        ),
        "annotations": {"readOnlyHint": True, "destructiveHint": False, "idempotentHint": True, "openWorldHint": True},
    },
    {
        "name": "resolve_media_source",
        "description": "Inspect a publisher transcript page, resolve its RSS episode, and merge GUID, feed, enclosure, speakers, timestamps, and content provenance.",
        "inputSchema": object_schema({"url": {"type": "string", "format": "uri"}}, ["url"]),
        "annotations": {"readOnlyHint": True, "destructiveHint": False, "idempotentHint": True, "openWorldHint": True},
    },
    {
        "name": "extract_transcript",
        "description": "Inspect a local or publisher-provided VTT/SRT/text transcript and return hashes, timestamp coverage, and bounded excerpts.",
        "inputSchema": object_schema(
            {
                "source": {"type": "string", "minLength": 1},
                "max_excerpts": {"type": "integer", "minimum": 1, "maximum": 20, "default": 5},
                "max_segments": {"type": "integer", "minimum": 1, "maximum": 500, "default": 50},
            },
            ["source"],
        ),
        "annotations": {"readOnlyHint": True, "destructiveHint": False, "idempotentHint": True, "openWorldHint": True},
    },
    {
        "name": "extract_document",
        "description": "Extract a bounded navigation copy from an authorized local document using Docling, pdftotext, or plain text.",
        "inputSchema": object_schema(
            {
                "source": {"type": "string", "minLength": 1},
                "max_chars": {"type": "integer", "minimum": 500, "maximum": 20000, "default": 4000},
                "max_pages": {"type": "integer", "minimum": 1, "maximum": 100, "default": 20},
            },
            ["source"],
        ),
        "annotations": {"readOnlyHint": True, "destructiveHint": False, "idempotentHint": True, "openWorldHint": False},
    },
    {
        "name": "fetch_lawful_document",
        "description": "Fetch an openly licensed, public-domain, publisher-open, or user-authorized document into the gitignored inbox with a rights receipt and hash.",
        "inputSchema": object_schema(
            {
                "url": {"type": "string", "format": "uri"},
                "rights_basis": {"type": "string", "enum": sorted(gateway.RIGHTS_BASES)},
            },
            ["url", "rights_basis"],
        ),
        "annotations": {"readOnlyHint": False, "destructiveHint": False, "idempotentHint": True, "openWorldHint": True},
    },
    {
        "name": "transcribe_media",
        "description": "Transcribe an authorized local media file with OpenAI, optionally diarizing speakers; stores full output only in the gitignored inbox.",
        "inputSchema": object_schema(
            {
                "source": {"type": "string", "minLength": 1},
                "diarize": {"type": "boolean", "default": True},
                "language": {"type": "string", "minLength": 2, "maxLength": 10},
            },
            ["source"],
        ),
        "annotations": {"readOnlyHint": False, "destructiveHint": False, "idempotentHint": True, "openWorldHint": True},
    },
    {
        "name": "search_zotero",
        "description": "Search the user's local Zotero library read-only when the Zotero local API is enabled.",
        "inputSchema": object_schema(
            {"query": {"type": "string", "minLength": 1}, "limit": {"type": "integer", "minimum": 1, "maximum": 50, "default": 10}},
            ["query"],
        ),
        "annotations": {"readOnlyHint": True, "destructiveHint": False, "idempotentHint": True, "openWorldHint": False},
    },
    {
        "name": "stage_source_candidate",
        "description": "Write one normalized candidate to the gitignored inbox. This does not create a source note or change atlas maturity.",
        "inputSchema": object_schema({"candidate": {"type": "object"}}, ["candidate"]),
        "annotations": {"readOnlyHint": False, "destructiveHint": False, "idempotentHint": True, "openWorldHint": False},
    },
    {
        "name": "list_staged_candidates",
        "description": "List bounded metadata for locally staged candidates.",
        "inputSchema": object_schema({"limit": {"type": "integer", "minimum": 1, "maximum": 200, "default": 50}}),
        "annotations": {"readOnlyHint": True, "destructiveHint": False, "idempotentHint": True, "openWorldHint": False},
    },
]


def call_tool(name: str, arguments: dict[str, Any]) -> Any:
    calls: dict[str, Callable[[], Any]] = {
        "research_capabilities": lambda: gateway.capabilities(),
        "discover_works": lambda: gateway.discover_works(
            arguments["query"], arguments.get("limit", 5), arguments.get("from_year"), arguments.get("to_year")
        ),
        "verify_doi": lambda: gateway.verify_doi(arguments["doi"]),
        "resolve_scholarly_work": lambda: gateway.resolve_scholarly_work(arguments["doi"]),
        "citation_neighborhood": lambda: gateway.citation_neighborhood(
            arguments["openalex_id"], arguments.get("direction", "cited_by"), arguments.get("limit", 10)
        ),
        "find_open_access": lambda: gateway.find_open_access(arguments["doi"]),
        "merge_source_candidates": lambda: gateway.merge_candidates(*(arguments["candidates"])),
        "discover_podcasts": lambda: gateway.discover_podcasts(arguments["query"], arguments.get("limit", 5)),
        "discover_captioned_videos": lambda: gateway.discover_videos(arguments["query"], arguments.get("limit", 5)),
        "resolve_podcast_feed": lambda: gateway.resolve_feed(
            arguments["url"], arguments.get("limit", 10), arguments.get("query")
        ),
        "inspect_source_url": lambda: gateway.inspect_url(arguments["url"], arguments.get("source_type", "web-essay")),
        "resolve_media_source": lambda: gateway.resolve_media_source(arguments["url"]),
        "extract_transcript": lambda: gateway.extract_transcript(
            arguments["source"], arguments.get("max_excerpts", 5), arguments.get("max_segments", 50)
        ),
        "extract_document": lambda: gateway.extract_document(
            arguments["source"], arguments.get("max_chars", 4_000), arguments.get("max_pages", 20)
        ),
        "fetch_lawful_document": lambda: gateway.fetch_lawful_document(arguments["url"], arguments["rights_basis"]),
        "transcribe_media": lambda: gateway.transcribe_media(
            arguments["source"], arguments.get("diarize", True), arguments.get("language")
        ),
        "search_zotero": lambda: gateway.zotero_search(arguments["query"], arguments.get("limit", 10)),
        "stage_source_candidate": lambda: gateway.stage_candidate(arguments["candidate"]),
        "list_staged_candidates": lambda: gateway.list_candidates(arguments.get("limit", 50)),
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
                "serverInfo": {"name": "learning-atlas-research", "version": "1.0.0"},
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
        try:
            message = json.loads(raw)
            if not isinstance(message, dict):
                raise ValueError("JSON-RPC message must be an object")
            response = handle(message)
        except (json.JSONDecodeError, ValueError) as exc:
            response = error_message(None, -32700, f"Parse error: {exc}")
        except Exception as exc:  # Keep the stdio transport alive while surfacing a bounded error.
            response = error_message(message.get("id") if isinstance(message, dict) else None, -32603, str(exc))
        if response is not None:
            sys.stdout.write(json.dumps(response, separators=(",", ":"), ensure_ascii=False) + "\n")
            sys.stdout.flush()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
