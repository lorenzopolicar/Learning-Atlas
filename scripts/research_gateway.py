#!/usr/bin/env python3
"""Normalized, provenance-first research gateway for Learning Atlas.

The gateway deliberately separates discovery from admission. It can inspect and
stage source candidates, but it cannot promote claims, beliefs, or principles.
It uses the Python standard library so the repository's integrity checks remain
portable; optional tools and credentials unlock richer providers.
"""

from __future__ import annotations

import argparse
import datetime as dt
import email.utils
import hashlib
import html
from html.parser import HTMLParser
import json
import mimetypes
import os
from pathlib import Path
import re
import shutil
import socket
import subprocess
import tempfile
import time
from typing import Any, Callable, Iterable
import urllib.error
import urllib.parse
import urllib.request
import uuid
import xml.etree.ElementTree as ET
import ipaddress


ROOT = Path(__file__).resolve().parents[1]
INBOX = ROOT / ".harness" / "inbox"
USER_AGENT = "LearningAtlasResearchGateway/1.0 (+https://github.com/lorenzopolicar/Learning-Atlas)"
MAX_HTTP_BYTES = 12 * 1024 * 1024
MAX_EXCERPT_CHARS = 4_000
RIGHTS_BASES = {"open-license", "public-domain", "publisher-open-access", "user-authorized"}
SOURCE_TYPES = {
    "journal-article",
    "conference-paper",
    "preprint",
    "systematic-review",
    "report",
    "book",
    "book-chapter",
    "podcast-series",
    "podcast-episode",
    "video",
    "lecture",
    "interview",
    "newsletter",
    "web-essay",
    "standard",
    "dataset",
    "product-evidence",
    "other",
}
EPISTEMIC_ROLES = {
    "empirical-study",
    "research-synthesis",
    "theoretical-argument",
    "expert-perspective",
    "firsthand-account",
    "normative-argument",
    "historical-source",
    "institutional-guidance",
    "product-claim",
    "dataset",
    "discovery-lead",
}
FEED_QUERY_STOPWORDS = {"a", "an", "and", "episode", "for", "in", "of", "on", "part", "the", "to", "with"}
FORBIDDEN_CANDIDATE_FIELDS = {"full_text", "full_transcript", "media_bytes", "document_bytes"}


class GatewayError(RuntimeError):
    """A bounded, user-facing research gateway failure."""


def utc_now() -> str:
    return dt.datetime.now(dt.timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def compact_whitespace(value: str) -> str:
    return " ".join(html.unescape(value).split())


def bounded(value: str | None, limit: int = MAX_EXCERPT_CHARS) -> str:
    if not value:
        return ""
    cleaned = compact_whitespace(value)
    return cleaned if len(cleaned) <= limit else cleaned[: limit - 1].rstrip() + "…"


def sha256_bytes(value: bytes) -> str:
    return hashlib.sha256(value).hexdigest()


def candidate_id(record: dict[str, Any]) -> str:
    identifiers = record.get("canonical_identifiers") or []
    normalized = {
        str(item.get("scheme")): str(item.get("value"))
        for item in identifiers
        if isinstance(item, dict) and item.get("scheme") and item.get("value")
    }
    priority = ("doi", "isbn", "podcast-guid", "youtube", "openalex", "podcast-index", "apple-podcast", "rss-feed")
    identity = next((f"{scheme}:{normalized[scheme].lower()}" for scheme in priority if normalized.get(scheme)), "")
    identity = identity or str(record.get("canonical_url") or record.get("title") or "unknown")
    return "cand_" + hashlib.sha256(identity.encode("utf-8")).hexdigest()[:16]


def strip_markup(value: str | None) -> str:
    if not value:
        return ""
    return compact_whitespace(re.sub(r"<[^>]+>", " ", value))


def source_type_for_openalex(work_type: str, title: str = "") -> str:
    mapping = {
        "article": "journal-article",
        "journal-article": "journal-article",
        "review": "systematic-review" if "systematic" in title.lower() else "journal-article",
        "posted-content": "preprint",
        "preprint": "preprint",
        "proceedings-article": "conference-paper",
        "proceedings": "conference-paper",
        "book": "book",
        "book-chapter": "book-chapter",
        "dataset": "dataset",
        "report": "report",
    }
    return mapping.get(work_type, "other")


def reverse_abstract(index: dict[str, list[int]] | None) -> str:
    if not index:
        return ""
    positions: list[tuple[int, str]] = []
    for word, offsets in index.items():
        positions.extend((offset, word) for offset in offsets)
    return " ".join(word for _, word in sorted(positions))


def base_candidate(
    *,
    title: str,
    source_type: str,
    canonical_url: str,
    provider: str,
    query: str | None = None,
) -> dict[str, Any]:
    record: dict[str, Any] = {
        "schema_version": 1,
        "candidate_id": "",
        "source_type": source_type if source_type in SOURCE_TYPES else "other",
        "title": bounded(title, 1_000),
        "creators": [],
        "published_at": None,
        "canonical_url": canonical_url,
        "canonical_identifiers": [],
        "container": {},
        "discovery": {
            "provider": provider,
            "query": query,
            "retrieved_at": utc_now(),
        },
        "access": {"status": "unknown", "rights": "unknown", "content_url": None},
        "provenance": {
            "retrieved_at": utc_now(),
            "extractor": "learning-atlas-research-gateway/1",
            "content_sha256": None,
            "locator_basis": "metadata",
        },
        "locators": [],
        "epistemic_roles": ["discovery-lead"],
        "verification": {"status": "unverified", "checks": [], "warnings": []},
        "summary": "",
        "transcript": {"availability": "none", "kind": None, "url": None, "language": None},
        "provider_payload": {},
    }
    record["candidate_id"] = candidate_id(record)
    return record


def validate_candidate(record: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    required = {
        "schema_version",
        "candidate_id",
        "source_type",
        "title",
        "canonical_url",
        "discovery",
        "provenance",
        "epistemic_roles",
        "verification",
    }
    missing = sorted(required - set(record))
    if missing:
        errors.append("missing fields: " + ", ".join(missing))
    def walk_keys(value: Any) -> Iterable[str]:
        if isinstance(value, dict):
            for key, child in value.items():
                yield str(key)
                yield from walk_keys(child)
        elif isinstance(value, list):
            for child in value:
                yield from walk_keys(child)

    forbidden = sorted(FORBIDDEN_CANDIDATE_FIELDS.intersection(walk_keys(record)))
    if forbidden:
        errors.append("copyright-sensitive fields are forbidden: " + ", ".join(forbidden))
    if record.get("source_type") not in SOURCE_TYPES:
        errors.append(f"unsupported source_type {record.get('source_type')!r}")
    unknown_roles = sorted(set(record.get("epistemic_roles") or []) - EPISTEMIC_ROLES)
    if unknown_roles:
        errors.append("unsupported epistemic_roles: " + ", ".join(unknown_roles))
    url = str(record.get("canonical_url") or "")
    if url and not url.startswith(("https://", "http://")):
        errors.append("canonical_url must be HTTP(S)")
    if not str(record.get("candidate_id", "")).startswith("cand_"):
        errors.append("candidate_id must start with cand_")
    return errors


def _validate_public_url(url: str) -> None:
    parsed = urllib.parse.urlparse(url)
    if parsed.scheme not in {"https", "http"}:
        raise GatewayError("Only HTTP(S) URLs are supported")
    hostname = (parsed.hostname or "").lower()
    if not hostname or hostname == "localhost" or hostname.endswith(".local"):
        raise GatewayError("Local and private network URLs are not accepted by public research tools")
    try:
        addresses = {item[4][0] for item in socket.getaddrinfo(hostname, parsed.port or (443 if parsed.scheme == "https" else 80))}
    except socket.gaierror as exc:
        raise GatewayError(f"Could not resolve public research host {hostname}: {exc}") from exc
    for address in addresses:
        parsed_ip = ipaddress.ip_address(address)
        if not parsed_ip.is_global:
            raise GatewayError(f"Public research URL resolves to a non-public address: {hostname}")


class _PublicRedirectHandler(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, req: Any, fp: Any, code: int, msg: str, headers: Any, newurl: str) -> Any:
        _validate_public_url(newurl)
        return super().redirect_request(req, fp, code, msg, headers, newurl)


def _open_url(
    url: str,
    *,
    headers: dict[str, str] | None = None,
    max_bytes: int = MAX_HTTP_BYTES,
    timeout: int = 30,
) -> tuple[bytes, dict[str, str], str]:
    _validate_public_url(url)
    request_headers = {"User-Agent": USER_AGENT, "Accept": "*/*"}
    request_headers.update(headers or {})
    request = urllib.request.Request(url, headers=request_headers)
    try:
        opener = urllib.request.build_opener(_PublicRedirectHandler())
        with opener.open(request, timeout=timeout) as response:
            data = response.read(max_bytes + 1)
            if len(data) > max_bytes:
                raise GatewayError(f"Remote response exceeds the {max_bytes}-byte safety limit")
            normalized_headers = {key.lower(): value for key, value in response.headers.items()}
            return data, normalized_headers, response.geturl()
    except urllib.error.HTTPError as exc:
        detail = exc.read(1_000).decode("utf-8", errors="replace")
        raise GatewayError(f"HTTP {exc.code} for {url}: {bounded(detail, 500)}") from exc
    except urllib.error.URLError as exc:
        raise GatewayError(f"Could not retrieve {url}: {exc.reason}") from exc


def http_json(url: str, *, headers: dict[str, str] | None = None) -> Any:
    data, _, _ = _open_url(url, headers=headers)
    try:
        result = json.loads(data)
    except json.JSONDecodeError as exc:
        raise GatewayError(f"Provider returned invalid JSON for {url}") from exc
    return result


def candidate_from_openalex(work: dict[str, Any], query: str | None = None) -> dict[str, Any]:
    title = str(work.get("display_name") or work.get("title") or "Untitled work")
    doi = str(work.get("doi") or "").removeprefix("https://doi.org/")
    openalex_id = str(work.get("id") or "").rsplit("/", 1)[-1]
    canonical_url = str(work.get("doi") or work.get("id") or "")
    record = base_candidate(
        title=title,
        source_type=source_type_for_openalex(str(work.get("type") or ""), title),
        canonical_url=canonical_url,
        provider="openalex",
        query=query,
    )
    record["creators"] = [
        {"name": bounded(str(authorship.get("author", {}).get("display_name") or ""), 300), "role": "author"}
        for authorship in work.get("authorships") or []
        if authorship.get("author", {}).get("display_name")
    ]
    record["published_at"] = work.get("publication_date") or work.get("publication_year")
    record["canonical_identifiers"] = [
        item
        for item in (
            {"scheme": "doi", "value": doi} if doi else None,
            {"scheme": "openalex", "value": openalex_id} if openalex_id else None,
        )
        if item
    ]
    primary = work.get("primary_location") or {}
    source = primary.get("source") or {}
    record["container"] = {"title": source.get("display_name"), "type": source.get("type")}
    open_access = work.get("open_access") or {}
    best_oa = work.get("best_oa_location") or {}
    record["access"] = {
        "status": "open" if open_access.get("is_oa") else "metadata-only",
        "rights": best_oa.get("license") or "unknown",
        "content_url": best_oa.get("pdf_url") or best_oa.get("landing_page_url"),
    }
    record["summary"] = bounded(reverse_abstract(work.get("abstract_inverted_index")))
    record["verification"] = {
        "status": "metadata-verified",
        "checks": ["openalex-record-resolved"],
        "warnings": ["Full methods and outcomes have not been inspected."],
    }
    record["provider_payload"] = {
        "type": work.get("type"),
        "cited_by_count": work.get("cited_by_count"),
        "referenced_works_count": len(work.get("referenced_works") or []),
        "is_retracted": work.get("is_retracted"),
    }
    if work.get("is_retracted"):
        record["verification"]["warnings"].append("OpenAlex marks this work as retracted.")
    record["candidate_id"] = candidate_id(record)
    return record


def discover_works(query: str, limit: int = 5, from_year: int | None = None, to_year: int | None = None) -> list[dict[str, Any]]:
    if not query.strip():
        raise GatewayError("A non-empty query is required")
    limit = max(1, min(limit, 20))
    params: dict[str, str] = {"search": query, "per-page": str(limit)}
    filters: list[str] = []
    if from_year:
        filters.append(f"from_publication_date:{from_year}-01-01")
    if to_year:
        filters.append(f"to_publication_date:{to_year}-12-31")
    if filters:
        params["filter"] = ",".join(filters)
    if os.getenv("OPENALEX_EMAIL"):
        params["mailto"] = os.environ["OPENALEX_EMAIL"]
    url = "https://api.openalex.org/works?" + urllib.parse.urlencode(params)
    response = http_json(url, headers={"Accept": "application/json"})
    return [candidate_from_openalex(work, query) for work in response.get("results") or []]


def normalize_doi(value: str) -> str:
    doi = value.strip().removeprefix("https://doi.org/").removeprefix("http://doi.org/")
    if not doi.startswith("10.") or "/" not in doi:
        raise GatewayError(f"Not a plausible DOI: {value!r}")
    return doi


def candidate_from_crossref(message: dict[str, Any], doi: str) -> dict[str, Any]:
    title_values = message.get("title") or []
    title = str(title_values[0] if title_values else doi)
    source_type = source_type_for_openalex(str(message.get("type") or ""), title)
    record = base_candidate(
        title=title,
        source_type=source_type,
        canonical_url=str(message.get("URL") or f"https://doi.org/{doi}"),
        provider="crossref",
    )
    record["creators"] = [
        {
            "name": bounded(" ".join(part for part in (author.get("given"), author.get("family")) if part), 300),
            "role": "author",
            "orcid": str(author.get("ORCID") or "").removeprefix("https://orcid.org/") or None,
        }
        for author in message.get("author") or []
    ]
    date_parts = ((message.get("published") or message.get("issued") or {}).get("date-parts") or [[]])[0]
    if date_parts:
        record["published_at"] = "-".join(f"{part:02d}" if index else str(part) for index, part in enumerate(date_parts))
    record["canonical_identifiers"] = [{"scheme": "doi", "value": doi}]
    container = message.get("container-title") or []
    record["container"] = {"title": container[0] if container else None, "publisher": message.get("publisher")}
    record["summary"] = bounded(strip_markup(message.get("abstract")))
    updates = message.get("update-to") or []
    record["verification"] = {
        "status": "metadata-verified",
        "checks": ["crossref-doi-resolved", "crossref-update-metadata-checked"],
        "warnings": ["Full methods and outcomes have not been inspected."],
    }
    if updates:
        record["verification"]["warnings"].append("Crossref reports an update, correction, or retraction relationship.")
    record["provider_payload"] = {
        "type": message.get("type"),
        "subtype": message.get("subtype"),
        "update_to": updates,
        "relation": message.get("relation") or {},
        "reference_count": message.get("reference-count"),
        "is_referenced_by_count": message.get("is-referenced-by-count"),
    }
    record["candidate_id"] = candidate_id(record)
    return record


def merge_candidates(*records: dict[str, Any]) -> dict[str, Any]:
    if len(records) < 2:
        raise GatewayError("At least two candidate records are required for a merge")
    for record in records:
        errors = validate_candidate(record)
        if errors:
            raise GatewayError("Cannot merge invalid candidate: " + "; ".join(errors))
    identities = {candidate_id(record) for record in records}
    if len(identities) != 1:
        normalized_urls = {
            str(record.get("canonical_url") or "").rstrip("/").removesuffix("/transcript")
            for record in records
            if record.get("canonical_url")
        }
        if len(normalized_urls) != 1:
            raise GatewayError("Candidates do not share a canonical DOI, GUID, ISBN, platform ID, or publisher URL")
    merged = json.loads(json.dumps(records[0]))
    identifiers: dict[tuple[str, str], dict[str, Any]] = {}
    checks: set[str] = set()
    warnings: set[str] = set()
    provider_records: dict[str, Any] = {}
    for record in records:
        for item in record.get("canonical_identifiers") or []:
            if isinstance(item, dict) and item.get("scheme") and item.get("value"):
                identifiers[(str(item["scheme"]), str(item["value"]))] = item
        verification = record.get("verification") or {}
        checks.update(str(item) for item in verification.get("checks") or [])
        warnings.update(str(item) for item in verification.get("warnings") or [])
        provider = str((record.get("discovery") or {}).get("provider") or "unknown")
        provider_records[provider] = record.get("provider_payload") or {}
        if len(record.get("creators") or []) > len(merged.get("creators") or []):
            merged["creators"] = record["creators"]
        if record.get("published_at") and not merged.get("published_at"):
            merged["published_at"] = record["published_at"]
        if record.get("container") and not merged.get("container"):
            merged["container"] = record["container"]
        if "/transcript" in str(merged.get("canonical_url")) and "/transcript" not in str(record.get("canonical_url")):
            merged["canonical_url"] = record["canonical_url"]
        if "transcript:" in str(merged.get("title", "")).lower() and "transcript:" not in str(record.get("title", "")).lower():
            merged["title"] = record["title"]
        if len(str(record.get("summary") or "")) > len(str(merged.get("summary") or "")):
            merged["summary"] = record["summary"]
        access = record.get("access") or {}
        if access.get("status") == "open" and (merged.get("access") or {}).get("status") != "open":
            merged["access"] = access
    merged["canonical_identifiers"] = list(identifiers.values())
    content_inspected = any(
        (record.get("verification") or {}).get("status") == "content-inspected"
        for record in records
    )
    merged["verification"] = {
        "status": "content-inspected" if content_inspected else "metadata-verified",
        "checks": sorted(checks),
        "warnings": sorted(
            warning
            for warning in warnings
            if not (content_inspected and "has not been inspected" in warning.lower())
        ),
        "providers": sorted(provider_records),
    }
    merged["provider_payload"] = {"verification_records": provider_records}
    merged["candidate_id"] = candidate_id(merged)
    return merged


def verify_doi(value: str) -> dict[str, Any]:
    doi = normalize_doi(value)
    url = "https://api.crossref.org/works/" + urllib.parse.quote(doi, safe="")
    response = http_json(url, headers={"Accept": "application/json"})
    message = response.get("message")
    if not isinstance(message, dict):
        raise GatewayError(f"Crossref did not return a work for {doi}")
    return candidate_from_crossref(message, doi)


def citation_neighborhood(openalex_id: str, direction: str = "cited_by", limit: int = 10) -> list[dict[str, Any]]:
    work_id = openalex_id.strip().rsplit("/", 1)[-1]
    if not re.fullmatch(r"W\d+", work_id):
        raise GatewayError("OpenAlex work ID must look like W123456789")
    limit = max(1, min(limit, 20))
    if direction == "cited_by":
        params = {"filter": f"cites:{work_id}", "per-page": str(limit)}
        response = http_json("https://api.openalex.org/works?" + urllib.parse.urlencode(params))
        return [candidate_from_openalex(work, f"cites:{work_id}") for work in response.get("results") or []]
    if direction != "references":
        raise GatewayError("direction must be cited_by or references")
    work = http_json(f"https://api.openalex.org/works/{work_id}")
    identifiers = [item.rsplit("/", 1)[-1] for item in (work.get("referenced_works") or [])[:limit]]
    results: list[dict[str, Any]] = []
    for identifier in identifiers:
        results.append(candidate_from_openalex(http_json(f"https://api.openalex.org/works/{identifier}"), f"references:{work_id}"))
    return results


def find_open_access(value: str) -> dict[str, Any]:
    doi = normalize_doi(value)
    email = os.getenv("UNPAYWALL_EMAIL")
    if email:
        url = f"https://api.unpaywall.org/v2/{urllib.parse.quote(doi, safe='')}?" + urllib.parse.urlencode({"email": email})
        response = http_json(url)
        best = response.get("best_oa_location") or {}
        return {
            "provider": "unpaywall",
            "doi": doi,
            "is_open_access": response.get("is_oa"),
            "oa_status": response.get("oa_status"),
            "license": best.get("license"),
            "landing_page_url": best.get("url_for_landing_page"),
            "pdf_url": best.get("url_for_pdf"),
            "version": best.get("version"),
            "retrieved_at": utc_now(),
        }
    params = {"filter": f"doi:{doi}", "per-page": "1"}
    response = http_json("https://api.openalex.org/works?" + urllib.parse.urlencode(params))
    results = response.get("results") or []
    if not results:
        raise GatewayError(f"No OpenAlex record found for {doi}; set UNPAYWALL_EMAIL for a direct Unpaywall check")
    work = results[0]
    best = work.get("best_oa_location") or {}
    access = work.get("open_access") or {}
    return {
        "provider": "openalex-fallback",
        "doi": doi,
        "is_open_access": access.get("is_oa"),
        "oa_status": access.get("oa_status"),
        "license": best.get("license"),
        "landing_page_url": best.get("landing_page_url"),
        "pdf_url": best.get("pdf_url"),
        "version": best.get("version"),
        "retrieved_at": utc_now(),
        "warning": "UNPAYWALL_EMAIL is unset; result comes from OpenAlex rather than a direct Unpaywall query.",
    }


def resolve_scholarly_work(value: str) -> dict[str, Any]:
    doi = normalize_doi(value)
    crossref = verify_doi(doi)
    params = {"filter": f"doi:{doi}", "per-page": "1"}
    response = http_json("https://api.openalex.org/works?" + urllib.parse.urlencode(params))
    results = response.get("results") or []
    if not results:
        crossref["verification"]["warnings"].append("No matching OpenAlex record was found; citation and OA metadata are incomplete.")
        return crossref
    openalex = candidate_from_openalex(results[0], f"doi:{doi}")
    merged = merge_candidates(openalex, crossref)
    oa = find_open_access(doi)
    merged["access"] = {
        "status": "open" if oa.get("is_open_access") else "metadata-only",
        "rights": oa.get("license") or "unknown",
        "content_url": oa.get("pdf_url") or oa.get("landing_page_url"),
        "version": oa.get("version"),
        "provider": oa.get("provider"),
    }
    merged["verification"]["checks"].append("lawful-access-location-checked")
    if oa.get("warning"):
        merged["verification"]["warnings"].append(str(oa["warning"]))
    merged["verification"]["checks"] = sorted(set(merged["verification"]["checks"]))
    merged["verification"]["warnings"] = sorted(set(merged["verification"]["warnings"]))
    return merged


def _podcast_index_headers() -> dict[str, str]:
    key = os.getenv("PODCAST_INDEX_KEY")
    secret = os.getenv("PODCAST_INDEX_SECRET")
    if not key or not secret:
        raise GatewayError("Podcast Index credentials are unavailable")
    auth_date = str(int(time.time()))
    digest = hashlib.sha1(f"{key}{secret}{auth_date}".encode("utf-8")).hexdigest()
    return {"X-Auth-Key": key, "X-Auth-Date": auth_date, "Authorization": digest, "User-Agent": USER_AGENT}


def discover_podcasts(query: str, limit: int = 5) -> list[dict[str, Any]]:
    if not query.strip():
        raise GatewayError("A non-empty query is required")
    limit = max(1, min(limit, 20))
    if os.getenv("PODCAST_INDEX_KEY") and os.getenv("PODCAST_INDEX_SECRET"):
        params = urllib.parse.urlencode({"q": query, "max": str(limit), "clean": "true"})
        response = http_json("https://api.podcastindex.org/api/1.0/search/byterm?" + params, headers=_podcast_index_headers())
        records = []
        for feed in response.get("feeds") or []:
            record = base_candidate(
                title=str(feed.get("title") or "Untitled podcast"),
                source_type="podcast-series",
                canonical_url=str(feed.get("link") or feed.get("url") or ""),
                provider="podcast-index",
                query=query,
            )
            record["canonical_identifiers"] = [{"scheme": "podcast-index", "value": str(feed.get("id"))}]
            record["provider_payload"] = {"feed_url": feed.get("url"), "author": feed.get("author"), "episode_count": feed.get("episodeCount")}
            record["verification"] = {"status": "metadata-verified", "checks": ["podcast-index-feed-resolved"], "warnings": []}
            record["candidate_id"] = candidate_id(record)
            records.append(record)
        return records

    params = urllib.parse.urlencode({"term": query, "media": "podcast", "entity": "podcast", "limit": str(limit)})
    response = http_json("https://itunes.apple.com/search?" + params)
    records = []
    for feed in response.get("results") or []:
        record = base_candidate(
            title=str(feed.get("collectionName") or "Untitled podcast"),
            source_type="podcast-series",
            canonical_url=str(feed.get("collectionViewUrl") or feed.get("feedUrl") or ""),
            provider="apple-podcasts-fallback",
            query=query,
        )
        record["creators"] = [{"name": str(feed.get("artistName")), "role": "publisher"}] if feed.get("artistName") else []
        record["canonical_identifiers"] = [{"scheme": "apple-podcast", "value": str(feed.get("collectionId"))}]
        record["provider_payload"] = {"feed_url": feed.get("feedUrl"), "genres": feed.get("genres") or []}
        record["verification"] = {
            "status": "metadata-verified",
            "checks": ["apple-podcast-record-resolved"],
            "warnings": ["Podcast Index credentials are unset; Apple Search was used as a discovery fallback."],
        }
        record["candidate_id"] = candidate_id(record)
        records.append(record)
    return records


def discover_videos(query: str, limit: int = 5) -> list[dict[str, Any]]:
    key = os.getenv("YOUTUBE_API_KEY")
    if not key:
        raise GatewayError("YOUTUBE_API_KEY is unset; use Exa or native web search, then inspect the selected URL")
    params = urllib.parse.urlencode(
        {
            "part": "snippet",
            "q": query,
            "type": "video",
            "videoCaption": "closedCaption",
            "maxResults": str(max(1, min(limit, 20))),
            "key": key,
        }
    )
    response = http_json("https://www.googleapis.com/youtube/v3/search?" + params)
    records = []
    for item in response.get("items") or []:
        video_id = (item.get("id") or {}).get("videoId")
        snippet = item.get("snippet") or {}
        record = base_candidate(
            title=str(snippet.get("title") or "Untitled video"),
            source_type="video",
            canonical_url=f"https://www.youtube.com/watch?v={video_id}",
            provider="youtube-data-api",
            query=query,
        )
        record["creators"] = [{"name": str(snippet.get("channelTitle")), "role": "publisher"}]
        record["published_at"] = snippet.get("publishedAt")
        record["canonical_identifiers"] = [{"scheme": "youtube", "value": str(video_id)}]
        record["summary"] = bounded(snippet.get("description"))
        record["transcript"] = {"availability": "possible", "kind": "caption", "url": None, "language": None}
        record["candidate_id"] = candidate_id(record)
        records.append(record)
    return records


def _tag_value(element: ET.Element, local_name: str) -> str | None:
    for child in list(element):
        if child.tag.rsplit("}", 1)[-1].lower() == local_name.lower() and child.text:
            return compact_whitespace(child.text)
    return None


def _children(element: ET.Element, local_name: str) -> list[ET.Element]:
    return [child for child in list(element) if child.tag.rsplit("}", 1)[-1].lower() == local_name.lower()]


def _parse_published(value: str | None) -> str | None:
    if not value:
        return None
    try:
        parsed = email.utils.parsedate_to_datetime(value)
        return parsed.isoformat()
    except (TypeError, ValueError):
        return value


def parse_feed(data: bytes, feed_url: str, limit: int = 10, query: str | None = None) -> list[dict[str, Any]]:
    try:
        root = ET.fromstring(data)
    except ET.ParseError as exc:
        raise GatewayError(f"Invalid RSS/Atom feed: {exc}") from exc
    channel = next((child for child in root.iter() if child.tag.rsplit("}", 1)[-1].lower() == "channel"), root)
    series_title = _tag_value(channel, "title") or "Untitled podcast"
    items = [element for element in root.iter() if element.tag.rsplit("}", 1)[-1].lower() in {"item", "entry"}]
    records: list[dict[str, Any]] = []
    for item in items:
        title = _tag_value(item, "title") or "Untitled episode"
        link = _tag_value(item, "link") or ""
        if not link:
            link_element = next(iter(_children(item, "link")), None)
            if link_element is not None:
                link = link_element.attrib.get("href", "")
        guid = _tag_value(item, "guid") or _tag_value(item, "id") or link
        description = _tag_value(item, "description") or _tag_value(item, "summary") or ""
        if query:
            haystack = f"{title} {strip_markup(description)}".lower()
            terms = [term for term in re.findall(r"[a-z0-9]+", query.lower()) if term not in FEED_QUERY_STOPWORDS]
            if terms and not all(term in haystack for term in terms):
                continue
        enclosure = next(iter(_children(item, "enclosure")), None)
        content = next(iter(_children(item, "content")), None)
        media_url = None
        media_type = None
        for candidate in (enclosure, content):
            if candidate is not None and candidate.attrib.get("url"):
                media_url = candidate.attrib.get("url")
                media_type = candidate.attrib.get("type")
                break
        transcript_elements = _children(item, "transcript")
        transcript_url = transcript_elements[0].attrib.get("url") if transcript_elements else None
        transcript_type = transcript_elements[0].attrib.get("type") if transcript_elements else None
        record = base_candidate(
            title=title,
            source_type="podcast-episode",
            canonical_url=link or media_url or feed_url,
            provider="rss-feed",
            query=feed_url,
        )
        creator = _tag_value(item, "author") or _tag_value(item, "creator")
        record["creators"] = [{"name": creator, "role": "creator"}] if creator else []
        record["published_at"] = _parse_published(_tag_value(item, "pubDate") or _tag_value(item, "published"))
        record["canonical_identifiers"] = [
            {"scheme": "podcast-guid", "value": guid},
            {"scheme": "rss-feed", "value": feed_url},
        ]
        record["container"] = {"title": series_title, "feed_url": feed_url}
        record["summary"] = bounded(strip_markup(description))
        record["access"] = {"status": "open" if media_url else "metadata-only", "rights": "unknown", "content_url": media_url}
        record["transcript"] = {
            "availability": "publisher-provided" if transcript_url else "none",
            "kind": transcript_type,
            "url": transcript_url,
            "language": transcript_elements[0].attrib.get("language") if transcript_elements else None,
        }
        record["epistemic_roles"] = ["expert-perspective", "discovery-lead"]
        record["verification"] = {
            "status": "metadata-verified",
            "checks": ["rss-episode-resolved"],
            "warnings": ["Episode content has not been inspected; empirical claims require original-source follow-up."],
        }
        record["provider_payload"] = {"duration": _tag_value(item, "duration"), "media_type": media_type}
        record["candidate_id"] = candidate_id(record)
        records.append(record)
        if len(records) >= max(1, min(limit, 50)):
            break
    return records


def resolve_feed(feed_url: str, limit: int = 10, query: str | None = None) -> list[dict[str, Any]]:
    data, _, final_url = _open_url(feed_url, headers={"Accept": "application/rss+xml, application/atom+xml, application/xml, text/xml"})
    return parse_feed(data, final_url, limit, query)


class PageParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.title_parts: list[str] = []
        self.text_parts: list[str] = []
        self.meta: dict[str, str] = {}
        self.canonical: str | None = None
        self.jsonld_parts: list[str] = []
        self.feed_links: list[str] = []
        self._in_title = False
        self._in_jsonld = False
        self._suppressed = 0

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        values = {key.lower(): value or "" for key, value in attrs}
        if tag.lower() == "title":
            self._in_title = True
        if tag.lower() == "script" and values.get("type", "").lower() == "application/ld+json":
            self._in_jsonld = True
        if tag.lower() in {"script", "style", "noscript", "svg"}:
            self._suppressed += 1
        if tag.lower() == "meta":
            key = values.get("property") or values.get("name")
            if key and values.get("content"):
                self.meta[key.lower()] = values["content"]
        if tag.lower() == "link" and values.get("rel", "").lower() == "canonical":
            self.canonical = values.get("href")
        if tag.lower() == "link" and "alternate" in values.get("rel", "").lower() and "rss" in values.get("type", "").lower():
            if values.get("href"):
                self.feed_links.append(values["href"])

    def handle_endtag(self, tag: str) -> None:
        if tag.lower() == "title":
            self._in_title = False
        if tag.lower() == "script":
            self._in_jsonld = False
        if tag.lower() in {"script", "style", "noscript", "svg"} and self._suppressed:
            self._suppressed -= 1

    def handle_data(self, data: str) -> None:
        if self._in_jsonld:
            self.jsonld_parts.append(data)
            return
        if self._in_title:
            self.title_parts.append(data)
        if not self._suppressed and data.strip():
            self.text_parts.append(data)


def _normalized_speaker(label: str, standalone: set[str]) -> str:
    cleaned = re.sub(r"^(?:(?:Transcript|Show Notes|Episode)\s+)+", "", compact_whitespace(label), flags=re.I)
    parts = cleaned.split()
    if len(parts) > 1 and parts[-1] in standalone:
        return parts[-1]
    return cleaned


def _timestamp_locators(text: str, limit: int = 20) -> list[dict[str, Any]]:
    speaker_pattern = r"(?:Dr\.?\s+)?(?:[A-Z]\.|[A-Z][A-Za-zÀ-ÖØ-öø-ÿ'-]+)(?:\s+(?:[A-Z]\.|[A-Z][A-Za-zÀ-ÖØ-öø-ÿ'-]+)){0,4}"
    labelled = re.compile(rf"(?P<speaker>{speaker_pattern})\s*[\[(]\s*(?P<time>\d{{1,2}}:\d{{2}}(?::\d{{2}})?)\s*[\])]")
    unlabelled = re.compile(r"(?P<time>\d{1,2}:\d{2}(?::\d{2})?)")
    matches = list(labelled.finditer(text)) or list(unlabelled.finditer(text))
    raw_labels = [bounded(match.groupdict().get("speaker"), 80) for match in matches if match.groupdict().get("speaker")]
    standalone = {re.sub(r"^(?:Transcript|Show Notes|Episode)\s+", "", label, flags=re.I) for label in raw_labels if len(label.split()) == 1}
    locators: list[dict[str, Any]] = []
    seen: set[str] = set()
    for match in matches:
        timestamp = match.group("time")
        if timestamp in seen:
            continue
        seen.add(timestamp)
        speaker = match.groupdict().get("speaker")
        label = _normalized_speaker(speaker, standalone) if speaker else None
        locators.append({"kind": "timestamp", "start": timestamp, "label": label})
        if len(locators) >= limit:
            break
    return locators


def timestamped_speaker_segments(text: str, limit: int = 5, total_chars: int = 1_200) -> list[dict[str, str]]:
    speaker_pattern = r"(?:Dr\.?\s+)?(?:[A-Z]\.|[A-Z][A-Za-zÀ-ÖØ-öø-ÿ'-]+)(?:\s+(?:[A-Z]\.|[A-Z][A-Za-zÀ-ÖØ-öø-ÿ'-]+)){0,4}"
    marker = re.compile(rf"(?P<speaker>{speaker_pattern})\s*[\[(]\s*(?P<time>\d{{1,2}}:\d{{2}}(?::\d{{2}})?)\s*[\])]")
    matches = list(marker.finditer(text))
    raw_labels = [bounded(match.group("speaker"), 80) for match in matches]
    standalone = {re.sub(r"^(?:Transcript|Show Notes|Episode)\s+", "", label, flags=re.I) for label in raw_labels if len(label.split()) == 1}
    segments: list[dict[str, str]] = []
    used = 0
    for index, match in enumerate(matches[:limit]):
        end = matches[index + 1].start() if index + 1 < len(matches) else len(text)
        excerpt = bounded(text[match.end() : end], min(300, total_chars - used))
        if not excerpt:
            continue
        segments.append({"speaker": _normalized_speaker(match.group("speaker"), standalone), "start": match.group("time"), "excerpt": excerpt})
        used += len(excerpt)
        if used >= total_chars:
            break
    return segments


def jsonld_metadata(parts: list[str]) -> dict[str, Any]:
    objects: list[dict[str, Any]] = []

    def collect(value: Any) -> None:
        if isinstance(value, dict):
            objects.append(value)
            for key in ("@graph", "mainEntity", "subjectOf"):
                if key in value:
                    collect(value[key])
        elif isinstance(value, list):
            for item in value:
                collect(item)

    for part in parts:
        try:
            collect(json.loads(part))
        except json.JSONDecodeError:
            continue
    preferred = next(
        (
            item
            for item in objects
            if str(item.get("@type", "")).lower() in {"podcastepisode", "episode", "audioobject", "videoobject", "article", "newsarticle"}
        ),
        objects[0] if objects else {},
    )

    def names(value: Any) -> list[str]:
        if isinstance(value, dict):
            return [str(value.get("name"))] if value.get("name") else []
        if isinstance(value, list):
            result: list[str] = []
            for item in value:
                result.extend(names(item))
            return result
        return [str(value)] if isinstance(value, str) else []

    series = preferred.get("partOfSeries") or preferred.get("isPartOf") or {}
    return {
        "title": preferred.get("name") or preferred.get("headline"),
        "published_at": preferred.get("datePublished") or preferred.get("uploadDate"),
        "creators": names(preferred.get("author") or preferred.get("creator")),
        "duration": preferred.get("duration"),
        "series": names(series)[0] if names(series) else None,
        "identifier": preferred.get("identifier"),
    }


def visible_page_metadata(text: str) -> dict[str, Any]:
    published_at = None
    date_match = re.search(
        r"\b(January|February|March|April|May|June|July|August|September|October|November|December)\s+([0-3]?\d),\s+(20\d{2})\b",
        text,
    )
    if date_match:
        published_at = dt.datetime.strptime(date_match.group(0), "%B %d, %Y").date().isoformat()
    duration_match = re.search(r"\b(\d{1,3})\s+Minutes?\b", text, flags=re.I)
    return {
        "published_at": published_at,
        "duration": f"PT{duration_match.group(1)}M" if duration_match else None,
    }


def inspect_url(url: str, source_type: str = "web-essay") -> dict[str, Any]:
    data, headers, final_url = _open_url(url, headers={"Accept": "text/html, text/plain, application/json"})
    content_type = headers.get("content-type", "").split(";", 1)[0].lower()
    encoding = "utf-8"
    charset = re.search(r"charset=([^; ]+)", headers.get("content-type", ""), re.I)
    if charset:
        encoding = charset.group(1).strip('"')
    text = data.decode(encoding, errors="replace")
    if content_type == "text/html" or "<html" in text[:1_000].lower():
        parser = PageParser()
        parser.feed(text)
        structured = jsonld_metadata(parser.jsonld_parts)
        visible = compact_whitespace(" ".join(parser.text_parts))
        visible_metadata = visible_page_metadata(visible)
        title = structured.get("title") or parser.meta.get("og:title") or compact_whitespace(" ".join(parser.title_parts)) or final_url
        canonical = urllib.parse.urljoin(final_url, parser.canonical) if parser.canonical else final_url
        published = structured.get("published_at") or parser.meta.get("article:published_time") or parser.meta.get("date") or visible_metadata.get("published_at")
        description = parser.meta.get("description") or parser.meta.get("og:description") or visible
        authors = structured.get("creators") or ([parser.meta.get("author")] if parser.meta.get("author") else [])
    else:
        visible = compact_whitespace(text)
        title = Path(urllib.parse.urlparse(final_url).path).name or final_url
        canonical = final_url
        published = None
        description = visible
        authors = []
        structured = {}
        visible_metadata = {}
    record = base_candidate(title=title, source_type=source_type, canonical_url=canonical, provider="direct-url")
    record["creators"] = [{"name": author, "role": "speaker-or-author"} for author in authors]
    record["published_at"] = published
    record["summary"] = bounded(description)
    record["provenance"].update(
        {"content_sha256": sha256_bytes(data), "locator_basis": "publisher-page", "content_type": content_type}
    )
    record["locators"] = _timestamp_locators(visible)
    if record["locators"] or "transcript" in title.lower() or "transcript" in visible[:5_000].lower():
        record["transcript"] = {"availability": "publisher-provided", "kind": "html", "url": canonical, "language": None}
        if source_type == "web-essay":
            record["source_type"] = "podcast-episode"
        record["epistemic_roles"] = ["expert-perspective", "discovery-lead"]
        segments = timestamped_speaker_segments(visible)
        if not record["creators"]:
            speakers = list(dict.fromkeys(item["label"] for item in record["locators"] if item.get("label")))
            record["creators"] = [{"name": speaker, "role": "speaker"} for speaker in speakers]
        record["provider_payload"] = {
            "series": structured.get("series") or (title.split("|", 1)[0].strip() if "|" in title else None),
            "duration": structured.get("duration") or visible_metadata.get("duration"),
            "feed_urls": [urllib.parse.urljoin(final_url, item) for item in parser.feed_links],
            "transcript_excerpt_segments": segments,
        }
    record["verification"] = {
        "status": "content-inspected",
        "checks": ["canonical-url-resolved", "content-hash-recorded"],
        "warnings": ["Only a bounded extraction was returned; verify quotations against the publisher page or audio."],
    }
    record["candidate_id"] = candidate_id(record)
    return record


def resolve_media_source(url: str) -> dict[str, Any]:
    inspected = inspect_url(url, "podcast-episode")
    feed_urls = ((inspected.get("provider_payload") or {}).get("feed_urls") or [])
    target = str(inspected.get("canonical_url") or "").rstrip("/").removesuffix("/transcript")
    for feed_url in feed_urls:
        for episode in resolve_feed(feed_url, limit=50):
            episode_url = str(episode.get("canonical_url") or "").rstrip("/").removesuffix("/transcript")
            if episode_url == target:
                return merge_candidates(inspected, episode)
    inspected["verification"]["warnings"].append(
        "No matching episode was resolved from the publisher feed; GUID, media enclosure, or series metadata may be incomplete."
    )
    return inspected


TIMECODE_RE = re.compile(
    r"(?P<start>\d{1,2}:\d{2}(?::\d{2})?[.,]\d{3})\s*-->\s*(?P<end>\d{1,2}:\d{2}(?::\d{2})?[.,]\d{3})"
)


def parse_timed_text(text: str) -> list[dict[str, str]]:
    lines = text.replace("\r\n", "\n").split("\n")
    segments: list[dict[str, str]] = []
    index = 0
    while index < len(lines):
        match = TIMECODE_RE.search(lines[index])
        if not match:
            index += 1
            continue
        index += 1
        content: list[str] = []
        while index < len(lines) and lines[index].strip():
            cleaned = re.sub(r"<[^>]+>", "", lines[index]).strip()
            if cleaned and cleaned not in content:
                content.append(cleaned)
            index += 1
        if content:
            segments.append(
                {
                    "start": match.group("start").replace(",", "."),
                    "end": match.group("end").replace(",", "."),
                    "text": bounded(" ".join(content), 500),
                }
            )
    return segments


def _allowed_local_path(value: str) -> Path:
    path = Path(value).expanduser().resolve()
    allowed = [ROOT.resolve(), Path(tempfile.gettempdir()).resolve()]
    for extra in os.getenv("ATLAS_RESEARCH_ALLOWED_PATHS", "").split(os.pathsep):
        if extra:
            allowed.append(Path(extra).expanduser().resolve())
    if not any(path == base or base in path.parents for base in allowed):
        raise GatewayError("Local research files must be inside the repository, system temp directory, or ATLAS_RESEARCH_ALLOWED_PATHS")
    if not path.is_file():
        raise GatewayError(f"Research input is not a file: {path}")
    return path


def extract_transcript(value: str, max_excerpts: int = 5, max_segments: int = 50) -> dict[str, Any]:
    max_excerpts = max(1, min(max_excerpts, 20))
    max_segments = max(max_excerpts, min(max_segments, 500))
    if value.startswith(("https://", "http://")):
        data, headers, final = _open_url(value)
        label = final
        content_type = headers.get("content-type", "")
    else:
        path = _allowed_local_path(value)
        data = path.read_bytes()
        if len(data) > MAX_HTTP_BYTES:
            raise GatewayError("Transcript exceeds the local safety limit")
        label = str(path)
        content_type = mimetypes.guess_type(path.name)[0] or "text/plain"
    text = data.decode("utf-8", errors="replace")
    segments = parse_timed_text(text)
    if not segments:
        speaker_segments = timestamped_speaker_segments(
            text,
            limit=max_segments,
            total_chars=max_segments * 500,
        )
        segments = [
            {
                "start": item["start"],
                "end": "",
                "speaker": item["speaker"],
                "text": item["excerpt"],
            }
            for item in speaker_segments
        ]
    if not segments:
        locators = _timestamp_locators(text, limit=max_segments)
        segments = [{"start": item["start"], "end": "", "text": item.get("label") or ""} for item in locators]
    segment_count = len(segments)
    excerpts = [segment for segment in segments[:max_excerpts]]
    return {
        "source": label,
        "content_type": content_type,
        "sha256": sha256_bytes(data),
        "segment_count": segment_count,
        "has_timestamps": bool(segments),
        "excerpt_segments": excerpts,
        "warning": "Only bounded excerpts are returned. Verify consequential quotations against the original audio or publisher transcript.",
    }


def _docling_executable() -> str | None:
    discovered = shutil.which("docling")
    if discovered:
        return discovered
    uv_tool = Path.home() / ".local" / "bin" / "docling"
    return str(uv_tool) if uv_tool.is_file() and os.access(uv_tool, os.X_OK) else None


def sanitize_extracted_markdown(value: str) -> str:
    value = re.sub(r"!\[[^\]]*\]\([^\n)]*\)", "[Image omitted; inspect original]", value)
    value = re.sub(r"data:image/[^\s)]+", "[embedded image omitted]", value)
    value = re.sub(r"<!--\s*image\s*-->", "[Image omitted; inspect original]", value, flags=re.I)
    return value


def _extract_with_docling(path: Path, max_chars: int, max_pages: int) -> tuple[str, str] | None:
    executable = _docling_executable()
    if not executable:
        return None
    with tempfile.TemporaryDirectory(prefix="atlas-docling-") as temp_dir:
        command = [
            executable,
            "convert",
            str(path),
            "--to",
            "md",
            "--no-ocr",
            "--image-export-mode",
            "placeholder",
            "--page-range",
            f"1-{max(1, min(max_pages, 100))}",
            "--output",
            temp_dir,
            "--quiet",
        ]
        result = subprocess.run(command, check=False, capture_output=True, text=True, timeout=300)
        if result.returncode:
            raise GatewayError(f"Docling failed: {bounded(result.stderr or result.stdout, 1_000)}")
        outputs = sorted(Path(temp_dir).glob("*.md"))
        if not outputs:
            raise GatewayError("Docling completed without producing Markdown")
        markdown = sanitize_extracted_markdown(outputs[0].read_text(encoding="utf-8", errors="replace"))
        return markdown[:max_chars], "docling"


def extract_document(value: str, max_chars: int = MAX_EXCERPT_CHARS, max_pages: int = 20) -> dict[str, Any]:
    path = _allowed_local_path(value)
    max_chars = max(500, min(max_chars, 20_000))
    if path.suffix.lower() in {".md", ".txt", ".html", ".htm", ".vtt", ".srt"}:
        text, method = path.read_text(encoding="utf-8", errors="replace")[:max_chars], "plain-text"
        extracted = None
    else:
        extracted = _extract_with_docling(path, max_chars, max_pages)
    if extracted:
        text, method = extracted
    elif path.suffix.lower() == ".pdf" and shutil.which("pdftotext"):
        result = subprocess.run(
            ["pdftotext", "-f", "1", "-l", str(max(1, min(max_pages, 100))), str(path), "-"],
            check=False,
            capture_output=True,
            text=True,
            timeout=120,
        )
        if result.returncode:
            raise GatewayError(f"pdftotext failed: {bounded(result.stderr, 1_000)}")
        text, method = result.stdout[:max_chars], "pdftotext-fallback"
    elif path.suffix.lower() not in {".md", ".txt", ".html", ".htm", ".vtt", ".srt"}:
        raise GatewayError("No extractor is available for this format; install Docling or provide PDF/plain text")
    data = path.read_bytes()
    return {
        "source": str(path),
        "method": method,
        "sha256": sha256_bytes(data),
        "file_size": len(data),
        "excerpt": bounded(text, max_chars),
        "warning": "Extraction is a navigation aid. Inspect the original layout, tables, notes, and methods before admitting evidence.",
    }


def fetch_lawful_document(url: str, rights_basis: str) -> dict[str, Any]:
    if rights_basis not in RIGHTS_BASES:
        raise GatewayError("rights_basis must be open-license, public-domain, publisher-open-access, or user-authorized")
    data, headers, final_url = _open_url(
        url,
        headers={"Accept": "application/pdf, application/epub+zip, text/plain, text/html"},
        max_bytes=25 * 1024 * 1024,
        timeout=60,
    )
    content_type = headers.get("content-type", "").split(";", 1)[0].lower()
    extension = mimetypes.guess_extension(content_type) or Path(urllib.parse.urlparse(final_url).path).suffix or ".bin"
    if extension == ".jpe":
        extension = ".jpg"
    digest = sha256_bytes(data)
    destination_dir = INBOX / "documents"
    destination_dir.mkdir(parents=True, exist_ok=True)
    destination = destination_dir / f"{digest[:16]}{extension}"
    destination.write_bytes(data)
    receipt = {
        "source_url": final_url,
        "rights_basis": rights_basis,
        "retrieved_at": utc_now(),
        "content_type": content_type,
        "size": len(data),
        "sha256": digest,
        "path": str(destination.relative_to(ROOT)),
        "gitignored": True,
    }
    receipt_path = destination.with_suffix(destination.suffix + ".receipt.json")
    receipt_path.write_text(json.dumps(receipt, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    return receipt


def _multipart_body(fields: dict[str, str], file_path: Path) -> tuple[bytes, str]:
    boundary = "----LearningAtlas" + uuid.uuid4().hex
    chunks: list[bytes] = []
    for name, value in fields.items():
        chunks.extend(
            [
                f"--{boundary}\r\n".encode(),
                f'Content-Disposition: form-data; name="{name}"\r\n\r\n'.encode(),
                value.encode(),
                b"\r\n",
            ]
        )
    mime = mimetypes.guess_type(file_path.name)[0] or "application/octet-stream"
    chunks.extend(
        [
            f"--{boundary}\r\n".encode(),
            f'Content-Disposition: form-data; name="file"; filename="{file_path.name}"\r\n'.encode(),
            f"Content-Type: {mime}\r\n\r\n".encode(),
            file_path.read_bytes(),
            b"\r\n",
            f"--{boundary}--\r\n".encode(),
        ]
    )
    return b"".join(chunks), boundary


def transcribe_media(value: str, diarize: bool = True, language: str | None = None) -> dict[str, Any]:
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise GatewayError("OPENAI_API_KEY is unset; use a publisher transcript/captions or configure the transcription provider")
    path = _allowed_local_path(value)
    if path.stat().st_size > 24 * 1024 * 1024:
        raise GatewayError("Media file exceeds the gateway's 24 MiB request limit; chunk it with ffmpeg first")
    model = "gpt-4o-transcribe-diarize" if diarize else "gpt-4o-transcribe"
    fields = {"model": model, "response_format": "diarized_json" if diarize else "json"}
    if diarize:
        fields["chunking_strategy"] = "auto"
    if language:
        fields["language"] = language
    body, boundary = _multipart_body(fields, path)
    request = urllib.request.Request(
        "https://api.openai.com/v1/audio/transcriptions",
        data=body,
        method="POST",
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": f"multipart/form-data; boundary={boundary}",
            "User-Agent": USER_AGENT,
        },
    )
    try:
        with urllib.request.urlopen(request, timeout=600) as response:
            payload = json.loads(response.read())
    except urllib.error.HTTPError as exc:
        detail = exc.read(2_000).decode("utf-8", errors="replace")
        raise GatewayError(f"Transcription API returned HTTP {exc.code}: {bounded(detail, 1_000)}") from exc
    output_dir = INBOX / "transcripts"
    output_dir.mkdir(parents=True, exist_ok=True)
    digest = sha256_bytes(path.read_bytes())[:16]
    output_path = output_dir / f"{digest}.json"
    output_path.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    segments = payload.get("segments") or []
    return {
        "source": str(path),
        "model": model,
        "transcript_path": str(output_path.relative_to(ROOT)),
        "segment_count": len(segments),
        "excerpt_segments": segments[:5],
        "sha256": digest,
        "warning": "The full transcript is stored only in the gitignored local inbox. Verify uncertain quotations against audio.",
    }


def zotero_search(query: str, limit: int = 10) -> list[dict[str, Any]]:
    params = urllib.parse.urlencode({"q": query, "limit": str(max(1, min(limit, 50))), "format": "json", "include": "data,bib"})
    request = urllib.request.Request(
        "http://127.0.0.1:23119/api/users/0/items?" + params,
        headers={"User-Agent": USER_AGENT, "Zotero-API-Version": "3"},
    )
    try:
        with urllib.request.urlopen(request, timeout=5) as response:
            items = json.loads(response.read())
    except (urllib.error.URLError, json.JSONDecodeError) as exc:
        raise GatewayError("Zotero local API is unavailable; open Zotero and enable 'Allow other applications'") from exc
    if not isinstance(items, list):
        raise GatewayError("Unexpected Zotero local API response")
    return items


def candidate_identity_tokens(record: dict[str, Any]) -> set[str]:
    tokens = {
        f"{item.get('scheme')}:{str(item.get('value')).strip().lower()}"
        for item in record.get("canonical_identifiers") or []
        if isinstance(item, dict) and item.get("scheme") and item.get("value")
    }
    url = str(record.get("canonical_url") or "").rstrip("/").removesuffix("/transcript")
    if url:
        tokens.add("url:" + url.lower())
    return tokens


def stage_candidate(record: dict[str, Any]) -> dict[str, Any]:
    errors = validate_candidate(record)
    if errors:
        raise GatewayError("Invalid candidate: " + "; ".join(errors))
    expected_id = candidate_id(record)
    record = json.loads(json.dumps(record))
    record["candidate_id"] = expected_id
    date_dir = INBOX / "candidates" / dt.date.today().isoformat()
    date_dir.mkdir(parents=True, exist_ok=True)
    destination = date_dir / f"{expected_id}.json"
    identity_tokens = candidate_identity_tokens(record)
    possible_duplicates: list[str] = []
    for existing_path in (INBOX / "candidates").glob("*/*.json"):
        try:
            existing = json.loads(existing_path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError):
            continue
        existing_id = str(existing.get("candidate_id") or "")
        if existing_id and existing_id != expected_id and identity_tokens.intersection(candidate_identity_tokens(existing)):
            possible_duplicates.append(existing_id)
    destination.write_text(json.dumps(record, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    return {
        "candidate_id": expected_id,
        "path": str(destination.relative_to(ROOT)),
        "verification_status": record["verification"]["status"],
        "possible_duplicate_ids": sorted(set(possible_duplicates)),
        "next_step": "Inspect the original content, assign the correct epistemic role, then create a seed source note. Staging is not admission.",
    }


def list_candidates(limit: int = 50) -> list[dict[str, Any]]:
    paths = sorted((INBOX / "candidates").glob("*/*.json"), reverse=True) if (INBOX / "candidates").exists() else []
    records = []
    for path in paths[: max(1, min(limit, 200))]:
        record = json.loads(path.read_text(encoding="utf-8"))
        records.append(
            {
                "candidate_id": record.get("candidate_id"),
                "title": record.get("title"),
                "source_type": record.get("source_type"),
                "verification_status": (record.get("verification") or {}).get("status"),
                "path": str(path.relative_to(ROOT)),
            }
        )
    return records


def capabilities() -> dict[str, Any]:
    return {
        "schema_version": 1,
        "providers": {
            "openalex": {"available": True, "purpose": "scholarly discovery and citation graph"},
            "crossref": {"available": True, "purpose": "DOI metadata and update relationships"},
            "unpaywall": {"available": bool(os.getenv("UNPAYWALL_EMAIL")), "requires": "UNPAYWALL_EMAIL", "fallback": "OpenAlex OA metadata"},
            "exa": {"available": "configured-as-separate-mcp", "purpose": "semantic web discovery"},
            "podcast_index": {"available": bool(os.getenv("PODCAST_INDEX_KEY") and os.getenv("PODCAST_INDEX_SECRET")), "requires": "PODCAST_INDEX_KEY and PODCAST_INDEX_SECRET", "fallback": "Apple Podcasts Search plus RSS"},
            "youtube": {"available": bool(os.getenv("YOUTUBE_API_KEY")), "requires": "YOUTUBE_API_KEY", "fallback": "Exa/native web plus direct URL inspection"},
            "zotero_local": {"available": "runtime-probe", "requires": "Zotero local API enabled"},
            "docling": {"available": bool(_docling_executable()), "fallback": "pdftotext/plain text"},
            "openai_transcription": {"available": bool(os.getenv("OPENAI_API_KEY")), "requires": "OPENAI_API_KEY", "fallback": "publisher transcript or captions"},
            "ffmpeg": {"available": bool(shutil.which("ffmpeg")), "purpose": "user-authorized media chunking"},
            "yt_dlp": {"available": bool(shutil.which("yt-dlp")), "purpose": "publisher captions when terms and access permit"},
        },
        "storage": {
            "inbox": str(INBOX.relative_to(ROOT)),
            "gitignored": True,
            "canonical_store": "Git source notes only after human-reviewed admission",
        },
    }


def _render(value: Any) -> None:
    print(json.dumps(value, indent=2, ensure_ascii=False))


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    subparsers = parser.add_subparsers(dest="command", required=True)

    subparsers.add_parser("capabilities")

    discover = subparsers.add_parser("discover")
    discover.add_argument("kind", choices=["works", "podcasts", "videos"])
    discover.add_argument("query")
    discover.add_argument("--limit", type=int, default=5)
    discover.add_argument("--from-year", type=int)
    discover.add_argument("--to-year", type=int)

    verify = subparsers.add_parser("verify-doi")
    verify.add_argument("doi")

    resolve_paper = subparsers.add_parser("resolve-paper")
    resolve_paper.add_argument("doi")
    resolve_paper.add_argument("--stage", action="store_true")

    citations = subparsers.add_parser("citations")
    citations.add_argument("openalex_id")
    citations.add_argument("--direction", choices=["cited_by", "references"], default="cited_by")
    citations.add_argument("--limit", type=int, default=10)

    oa = subparsers.add_parser("find-open-access")
    oa.add_argument("doi")

    feed = subparsers.add_parser("resolve-feed")
    feed.add_argument("url")
    feed.add_argument("--limit", type=int, default=10)
    feed.add_argument("--query")

    inspect = subparsers.add_parser("inspect-url")
    inspect.add_argument("url")
    inspect.add_argument("--source-type", choices=sorted(SOURCE_TYPES), default="web-essay")
    inspect.add_argument("--stage", action="store_true")

    resolve_media = subparsers.add_parser("resolve-media")
    resolve_media.add_argument("url")
    resolve_media.add_argument("--stage", action="store_true")

    transcript = subparsers.add_parser("extract-transcript")
    transcript.add_argument("source")
    transcript.add_argument("--max-excerpts", type=int, default=5)
    transcript.add_argument("--max-segments", type=int, default=50)

    document = subparsers.add_parser("extract-document")
    document.add_argument("source")
    document.add_argument("--max-chars", type=int, default=MAX_EXCERPT_CHARS)
    document.add_argument("--max-pages", type=int, default=20)

    fetch = subparsers.add_parser("fetch-document")
    fetch.add_argument("url")
    fetch.add_argument("--rights-basis", choices=sorted(RIGHTS_BASES), required=True)

    transcribe = subparsers.add_parser("transcribe")
    transcribe.add_argument("source")
    transcribe.add_argument("--no-diarize", action="store_true")
    transcribe.add_argument("--language")

    zotero = subparsers.add_parser("zotero-search")
    zotero.add_argument("query")
    zotero.add_argument("--limit", type=int, default=10)

    stage = subparsers.add_parser("stage")
    stage.add_argument("json_file")

    listing = subparsers.add_parser("list-candidates")
    listing.add_argument("--limit", type=int, default=50)

    args = parser.parse_args()
    try:
        if args.command == "capabilities":
            result = capabilities()
        elif args.command == "discover" and args.kind == "works":
            result = discover_works(args.query, args.limit, args.from_year, args.to_year)
        elif args.command == "discover" and args.kind == "podcasts":
            result = discover_podcasts(args.query, args.limit)
        elif args.command == "discover":
            result = discover_videos(args.query, args.limit)
        elif args.command == "verify-doi":
            result = verify_doi(args.doi)
        elif args.command == "resolve-paper":
            candidate = resolve_scholarly_work(args.doi)
            result = {"candidate": candidate, "staged": stage_candidate(candidate)} if args.stage else candidate
        elif args.command == "citations":
            result = citation_neighborhood(args.openalex_id, args.direction, args.limit)
        elif args.command == "find-open-access":
            result = find_open_access(args.doi)
        elif args.command == "resolve-feed":
            result = resolve_feed(args.url, args.limit, args.query)
        elif args.command == "inspect-url":
            candidate = inspect_url(args.url, args.source_type)
            result = {"candidate": candidate, "staged": stage_candidate(candidate)} if args.stage else candidate
        elif args.command == "resolve-media":
            candidate = resolve_media_source(args.url)
            result = {"candidate": candidate, "staged": stage_candidate(candidate)} if args.stage else candidate
        elif args.command == "extract-transcript":
            result = extract_transcript(args.source, args.max_excerpts, args.max_segments)
        elif args.command == "extract-document":
            result = extract_document(args.source, args.max_chars, args.max_pages)
        elif args.command == "fetch-document":
            result = fetch_lawful_document(args.url, args.rights_basis)
        elif args.command == "transcribe":
            result = transcribe_media(args.source, not args.no_diarize, args.language)
        elif args.command == "zotero-search":
            result = zotero_search(args.query, args.limit)
        elif args.command == "stage":
            record = json.loads(_allowed_local_path(args.json_file).read_text(encoding="utf-8"))
            result = stage_candidate(record)
        elif args.command == "list-candidates":
            result = list_candidates(args.limit)
        else:
            raise GatewayError(f"Unsupported command {args.command}")
        _render(result)
        return 0
    except (GatewayError, json.JSONDecodeError) as exc:
        _render({"error": str(exc), "command": args.command})
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
