#!/usr/bin/env python3
"""Dependency-free maintenance harness for Learning Atlas."""

from __future__ import annotations

import argparse
import datetime as dt
import json
import re
import sys
import textwrap
import tomllib
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any, Iterable


ROOT = Path(__file__).resolve().parents[1]
CONFIG = tomllib.loads((ROOT / "atlas.toml").read_text(encoding="utf-8"))

CONTENT_DIRS = {
    "source": ROOT / "sources" / "notes",
    "claim": ROOT / "claims",
    "belief": ROOT / "beliefs",
    "principle": ROOT / "principles",
    "decision": ROOT / "decisions",
    "question": ROOT / "questions",
    "experiment": ROOT / "experiments",
    "discourse": ROOT / "discourse",
    "review": ROOT / "reviews",
}

PREFIXES = {
    "source": "S",
    "claim": "C",
    "belief": "B",
    "principle": "P",
    "decision": "D",
    "question": "Q",
    "experiment": "E",
    "discourse": "N",
    "review": "R",
}

TEMPLATES = {
    "source": "source-note.md",
    "claim": "claim.md",
    "belief": "belief.md",
    "principle": "principle.md",
    "decision": "decision.md",
    "question": "research-question.md",
    "experiment": "experiment.md",
    "discourse": "discourse-note.md",
}

SOURCE_PROFILE_TEMPLATES = {
    "empirical": "source-note.md",
    "media": "source-media.md",
    "book": "source-book.md",
    "dataset": "source-dataset.md",
}

REQUIRED = {
    "source": ("id", "type", "title", "citation_key", "source_kind", "year", "url", "status", "topics", "added", "last_reviewed"),
    "claim": ("id", "type", "title", "statement", "status", "confidence", "topics", "supporting_sources", "contradicting_sources", "boundary_conditions", "product_relevance", "last_reviewed"),
    "belief": ("id", "type", "title", "statement", "status", "confidence", "topics", "derived_from", "counterarguments", "would_change_my_mind", "last_reviewed"),
    "principle": ("id", "type", "title", "statement", "status", "confidence", "topics", "based_on", "applies_to", "exceptions", "falsifiers", "last_reviewed"),
    "decision": ("id", "type", "title", "status", "date", "topics", "principles"),
    "question": ("id", "type", "title", "question", "status", "priority", "topics", "related_claims", "last_reviewed"),
    "experiment": ("id", "type", "title", "status", "date", "topics", "tests_claims", "tests_beliefs", "tests_principles"),
    "discourse": ("id", "type", "title", "status", "topics", "sources", "last_reviewed"),
    "review": ("id", "type", "title", "status", "topics", "last_reviewed"),
}

REFERENCE_FIELDS = {
    "supporting_sources",
    "contradicting_sources",
    "derived_from",
    "based_on",
    "principles",
    "related_claims",
    "tests_claims",
    "tests_beliefs",
    "tests_principles",
    "sources",
    "supersedes",
}

DATE_FIELDS = {"added", "last_reviewed", "date"}
CONFIDENCE = {"low", "moderate", "high"}
EPISTEMIC_ROLES = {
    "empirical-study", "research-synthesis", "theoretical-argument", "expert-perspective",
    "firsthand-account", "normative-argument", "historical-source", "institutional-guidance",
    "product-claim", "dataset", "discovery-lead",
}
ID_RE = re.compile(r"^[SCBPDQENR]\d{3}$")
TOKEN_RE = re.compile(r"[a-z0-9][a-z0-9-]+")
STOPWORDS = {
    "a", "an", "and", "are", "as", "at", "be", "by", "can", "do", "does",
    "for", "from", "give", "how", "if", "in", "into", "is", "it", "of", "on",
    "or", "our", "should", "the", "their", "this", "to", "update", "we", "what",
    "when", "with", "work",
}
SYNONYM_GROUPS = (
    {"answer", "answers", "assistance", "assisted", "help", "hint", "hints", "scaffold", "tutor"},
    {"learn", "learning", "retention", "transfer", "capability"},
    {"mastery", "learner", "model", "modelling", "profile", "evidence"},
    {"measure", "assessment", "score", "judgment", "validity"},
    {"generate", "generated", "generative", "ai"},
    {"delay", "delayed", "later", "long-term", "durable"},
    {"adapt", "adaptive", "personalization", "personalized"},
    {"practice", "retrieve", "retrieval", "schedule", "scheduling", "space", "spaced", "spacing"},
)


def relative(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def parse_markdown(path: Path) -> dict[str, Any]:
    raw = path.read_text(encoding="utf-8")
    if not raw.startswith("---\n"):
        raise ValueError("missing JSON frontmatter")
    end = raw.find("\n---\n", 4)
    if end < 0:
        raise ValueError("unterminated JSON frontmatter")
    try:
        metadata = json.loads(raw[4:end])
    except json.JSONDecodeError as exc:
        raise ValueError(f"invalid frontmatter JSON: {exc.msg} at line {exc.lineno}") from exc
    if not isinstance(metadata, dict):
        raise ValueError("frontmatter must be a JSON object")
    return {"meta": metadata, "body": raw[end + 5 :].strip(), "path": path}


def iter_artifact_paths() -> Iterable[Path]:
    for artifact_type, directory in CONTENT_DIRS.items():
        if not directory.exists():
            continue
        pattern = "*.md" if artifact_type != "review" else "**/*.md"
        for path in sorted(directory.glob(pattern)):
            if artifact_type == "review" and path.name != "protocol.md":
                continue
            yield path


def collect() -> tuple[list[dict[str, Any]], list[str]]:
    records: list[dict[str, Any]] = []
    errors: list[str] = []
    for path in iter_artifact_paths():
        try:
            records.append(parse_markdown(path))
        except ValueError as exc:
            errors.append(f"{relative(path)}: {exc}")
    return records, errors


def validate_records(records: list[dict[str, Any]]) -> tuple[list[str], list[str]]:
    errors: list[str] = []
    warnings: list[str] = []
    by_id: dict[str, dict[str, Any]] = {}
    stale_days = int(CONFIG["review"]["stale_after_days"])
    today = dt.date.today()
    allowed_status = set(CONFIG["status"]["allowed"])

    for record in records:
        meta = record["meta"]
        path = record["path"]
        label = relative(path)
        artifact_type = meta.get("type")
        artifact_id = meta.get("id")

        if artifact_type not in REQUIRED:
            errors.append(f"{label}: unknown artifact type {artifact_type!r}")
            continue
        missing = [field for field in REQUIRED[artifact_type] if field not in meta]
        if missing:
            errors.append(f"{label}: missing required fields: {', '.join(missing)}")

        expected_prefix = PREFIXES[artifact_type]
        if not isinstance(artifact_id, str) or not ID_RE.match(artifact_id):
            errors.append(f"{label}: invalid id {artifact_id!r}")
        elif not artifact_id.startswith(expected_prefix):
            errors.append(f"{label}: id {artifact_id} does not match type {artifact_type}")
        elif artifact_id in by_id:
            errors.append(f"{label}: duplicate id {artifact_id} also used by {relative(by_id[artifact_id]['path'])}")
        else:
            by_id[artifact_id] = record

        if artifact_type != "review" and isinstance(artifact_id, str) and not path.name.startswith(f"{artifact_id}-"):
            errors.append(f"{label}: filename must start with {artifact_id}-")

        if meta.get("status") not in allowed_status:
            errors.append(f"{label}: unsupported status {meta.get('status')!r}")
        if "confidence" in meta and meta["confidence"] not in CONFIDENCE:
            errors.append(f"{label}: confidence must be low, moderate, or high")
        if not isinstance(meta.get("topics", []), list):
            errors.append(f"{label}: topics must be a list")

        for field in DATE_FIELDS.intersection(meta):
            try:
                value = dt.date.fromisoformat(str(meta[field]))
            except ValueError:
                errors.append(f"{label}: {field} must be YYYY-MM-DD")
                continue
            if field == "last_reviewed" and (today - value).days > stale_days and meta.get("status") != "retired":
                warnings.append(f"{label}: last reviewed {(today - value).days} days ago")

        if artifact_type == "source":
            url = str(meta.get("url", ""))
            if not url.startswith(("https://", "http://")):
                errors.append(f"{label}: source URL must be absolute")
            if "..." in url or "example." in url:
                errors.append(f"{label}: placeholder source URL")
            if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", str(meta.get("source_kind", ""))):
                errors.append(f"{label}: source_kind must be lowercase kebab-case")
            roles = meta.get("epistemic_roles")
            if roles is not None:
                if not isinstance(roles, list):
                    errors.append(f"{label}: epistemic_roles must be a list")
                else:
                    unsupported = sorted(set(roles) - EPISTEMIC_ROLES)
                    if unsupported:
                        errors.append(f"{label}: unsupported epistemic_roles: {', '.join(unsupported)}")

        if artifact_type == "claim" and meta.get("status") in {"provisional", "contested", "established"}:
            if not meta.get("supporting_sources"):
                errors.append(f"{label}: mature claim needs supporting_sources")
            if not meta.get("boundary_conditions"):
                errors.append(f"{label}: mature claim needs boundary_conditions")
        if artifact_type == "belief" and meta.get("status") == "adopted":
            if not meta.get("derived_from") or not meta.get("would_change_my_mind"):
                errors.append(f"{label}: adopted belief needs evidence and revision criteria")
        if artifact_type == "principle" and meta.get("status") == "active":
            if not meta.get("based_on") or not meta.get("falsifiers"):
                errors.append(f"{label}: active principle needs evidence and falsifiers")

    known_ids = set(by_id)
    for record in records:
        meta = record["meta"]
        label = relative(record["path"])
        for field in REFERENCE_FIELDS.intersection(meta):
            values = meta[field]
            if not isinstance(values, list):
                errors.append(f"{label}: {field} must be a list")
                continue
            for value in values:
                if isinstance(value, str) and ID_RE.match(value) and value not in known_ids:
                    errors.append(f"{label}: {field} references missing artifact {value}")

    citation_keys = bibliography_keys()
    for record in records:
        meta = record["meta"]
        if meta.get("type") == "source" and meta.get("citation_key") not in citation_keys:
            errors.append(f"{relative(record['path'])}: citation key {meta.get('citation_key')!r} missing from references.bib")

    return sorted(errors), sorted(warnings)


def bibliography_keys() -> set[str]:
    path = ROOT / "sources" / "bibliography" / "references.bib"
    if not path.exists():
        return set()
    raw = path.read_text(encoding="utf-8")
    return set(re.findall(r"@\w+\s*\{\s*([^,\s]+)", raw))


def record_title(record: dict[str, Any]) -> str:
    meta = record["meta"]
    return str(meta.get("title") or meta.get("statement") or meta.get("question") or meta["id"])


def index_content(artifact_type: str, records: list[dict[str, Any]]) -> str:
    selected = sorted(
        (record for record in records if record["meta"].get("type") == artifact_type),
        key=lambda record: record["meta"]["id"],
    )
    plural = artifact_type[:-1] + "ies" if artifact_type.endswith("y") else artifact_type + "s"
    lines = ["<!-- generated by scripts/atlas.py; do not edit -->", "", f"# {plural.title()}", ""]
    if not selected:
        lines.extend(["_No artifacts yet._", ""])
        return "\n".join(lines)
    lines.extend(["| ID | Title | Status | Confidence | Topics |", "|---|---|---|---|---|"])
    for record in selected:
        meta = record["meta"]
        target = "../" + relative(record["path"])
        title = record_title(record).replace("|", "\\|")
        topics = ", ".join(meta.get("topics", [])).replace("|", "\\|")
        lines.append(
            f"| [{meta['id']}]({target}) | {title} | {meta.get('status', '')} | {meta.get('confidence', '')} | {topics} |"
        )
    lines.append("")
    return "\n".join(lines)


def graph_content(records: list[dict[str, Any]]) -> str:
    nodes = []
    edges = []
    for record in sorted(records, key=lambda item: item["meta"]["id"]):
        meta = record["meta"]
        nodes.append(
            {
                "id": meta["id"],
                "type": meta["type"],
                "title": record_title(record),
                "status": meta.get("status"),
                "path": relative(record["path"]),
            }
        )
        for field in sorted(REFERENCE_FIELDS.intersection(meta)):
            for target in meta[field] if isinstance(meta[field], list) else []:
                if isinstance(target, str) and ID_RE.match(target):
                    edges.append({"source": meta["id"], "target": target, "relation": field})
    return json.dumps({"nodes": nodes, "edges": edges}, indent=2, ensure_ascii=False) + "\n"


def desired_generated_files(records: list[dict[str, Any]]) -> dict[Path, str]:
    outputs = {
        ROOT / "indexes" / f"{artifact_type[:-1] + 'ies' if artifact_type.endswith('y') else artifact_type + 's'}.md": index_content(artifact_type, records)
        for artifact_type in CONTENT_DIRS
    }
    outputs[ROOT / "maps" / "graph.json"] = graph_content(records)
    outputs[ROOT / "exports" / "notebooklm" / "learning-atlas-research-pack.md"] = notebooklm_content(records)
    return outputs


def write_or_check(outputs: dict[Path, str], check: bool, selected: Iterable[Path] | None = None) -> int:
    paths = set(selected) if selected is not None else set(outputs)
    stale: list[str] = []
    for path in sorted(paths):
        content = outputs[path]
        if check:
            if not path.exists() or path.read_text(encoding="utf-8") != content:
                stale.append(relative(path))
        else:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(content, encoding="utf-8")
    if stale:
        print("Generated files are stale:")
        for path in stale:
            print(f"  - {path}")
        return 1
    if not check:
        print(f"Updated {len(paths)} generated file(s).")
    return 0


def notebooklm_content(records: list[dict[str, Any]]) -> str:
    included = {"source", "claim", "belief", "principle", "question"}
    lines = [
        "<!-- generated by scripts/atlas.py; do not edit -->",
        "",
        "# Learning Atlas research pack",
        "",
        "This is a generated exploration surface for NotebookLM or another source-grounded reading tool. The repository is authoritative. Follow source URLs for the original work; this pack contains original synthesis, not copyrighted papers.",
        "",
        "## How to interrogate this pack",
        "",
        "Ask for the evidence chain behind a principle, disagreements between sources, boundary conditions, missing evidence, and experiments that could change a belief. Do not treat generated answers as new atlas evidence.",
        "",
    ]
    order = {"source": 0, "claim": 1, "belief": 2, "principle": 3, "question": 4}
    for record in sorted(
        (r for r in records if r["meta"].get("type") in included),
        key=lambda r: (order[r["meta"]["type"]], r["meta"]["id"]),
    ):
        meta = record["meta"]
        lines.extend(
            [
                f"## {meta['id']} — {record_title(record)}",
                "",
                f"Type: {meta['type']}  ",
                f"Status: {meta.get('status', '')}  ",
                f"Topics: {', '.join(meta.get('topics', []))}  ",
                f"Canonical path: `{relative(record['path'])}`",
                "",
                record["body"],
                "",
            ]
        )
    return "\n".join(lines).rstrip() + "\n"


def validate_command(strict: bool) -> int:
    records, parse_errors = collect()
    errors, warnings = validate_records(records)
    errors = parse_errors + errors
    for error in errors:
        print(f"ERROR: {error}")
    for warning in warnings:
        print(f"WARNING: {warning}")
    if errors or (strict and warnings):
        print(f"Validation failed: {len(errors)} error(s), {len(warnings)} warning(s).")
        return 1
    print(f"Validated {len(records)} artifacts: {len(errors)} error(s), {len(warnings)} warning(s).")
    return 0


def tokenize(value: str) -> list[str]:
    return [token for token in TOKEN_RE.findall(value.lower()) if token not in STOPWORDS]


def expanded_terms(value: str) -> list[str]:
    original = set(tokenize(value))
    expanded = set(original)
    for group in SYNONYM_GROUPS:
        if original.intersection(group):
            expanded.update(group)
    return sorted(expanded)


def rank_records(query: str, records: list[dict[str, Any]], allowed_types: set[str]) -> list[tuple[int, str, dict[str, Any]]]:
    original = set(tokenize(query))
    terms = expanded_terms(query)
    scored: list[tuple[int, str, dict[str, Any]]] = []
    for record in records:
        meta = record["meta"]
        if meta.get("type") not in allowed_types:
            continue
        title_text = " ".join(
            str(meta.get(field, "")) for field in ("id", "title", "statement", "question", "product_relevance")
        ).lower()
        topic_text = " ".join(meta.get("topics", [])).lower()
        body_text = record["body"].lower()
        score = 0
        for term in terms:
            title_weight, topic_weight, body_cap = (18, 12, 8) if term in original else (3, 2, 2)
            score += title_weight * title_text.count(term)
            score += topic_weight * topic_text.count(term)
            score += min(body_cap, body_text.count(term))
        if score:
            scored.append((score, meta["id"], record))
    return sorted(scored, key=lambda item: (-item[0], item[1]))


def query_command(query: str, types: list[str], limit: int | None, max_chars: int | None) -> int:
    records, errors = collect()
    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1
    terms = expanded_terms(query)
    if not terms:
        print("Query must contain at least one searchable term.", file=sys.stderr)
        return 2
    allowed_types = set(types or CONTENT_DIRS)
    scored = rank_records(query, records, allowed_types)

    item_limit = limit or int(CONFIG["retrieval"]["max_items"])
    char_limit = max_chars or int(CONFIG["retrieval"]["max_chars"])
    rendered: list[str] = []
    used = 0
    for score, _, record in scored[:item_limit]:
        meta = record["meta"]
        summary = str(meta.get("statement") or meta.get("question") or first_prose(record["body"]))
        block = textwrap.dedent(
            f"""
            [{meta['id']}] {record_title(record)}
            type={meta['type']} status={meta.get('status', '')} confidence={meta.get('confidence', '')}
            path={relative(record['path'])}
            relevance={score}
            {summary}
            """
        ).strip()
        separator = "\n\n" if rendered else ""
        if used + len(separator) + len(block) > char_limit:
            break
        rendered.append(block)
        used += len(separator) + len(block)
    if not rendered:
        print("No matching atlas artifacts.")
        return 0
    print("\n\n".join(rendered))
    print(f"\n-- {len(rendered)} artifact(s), {used} characters --")
    return 0


def first_prose(body: str) -> str:
    for paragraph in re.split(r"\n\s*\n", body):
        cleaned = paragraph.strip()
        if cleaned and not cleaned.startswith(("#", "|", "- ")):
            return " ".join(cleaned.split())
    return "See artifact for details."


def status_command() -> int:
    records, errors = collect()
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    counts = Counter(record["meta"]["type"] for record in records)
    statuses: dict[str, Counter[str]] = defaultdict(Counter)
    for record in records:
        meta = record["meta"]
        statuses[meta["type"]][str(meta.get("status", "unknown"))] += 1
    print(f"Learning Atlas: {len(records)} artifacts")
    for artifact_type in CONTENT_DIRS:
        if counts[artifact_type]:
            detail = ", ".join(f"{key}={value}" for key, value in sorted(statuses[artifact_type].items()))
            print(f"  {artifact_type:10} {counts[artifact_type]:3}  {detail}")
    return 0


def eval_command() -> int:
    path = ROOT / ".harness" / "evals" / "cases.json"
    suite = json.loads(path.read_text(encoding="utf-8"))
    records, parse_errors = collect()
    if parse_errors:
        for error in parse_errors:
            print(f"ERROR: {error}")
        return 1
    failures = 0
    allowed = {"claim", "belief", "principle"}
    for case in suite["cases"]:
        ranked = rank_records(case["query"], records, allowed)[: int(CONFIG["retrieval"]["max_items"])]
        returned = {record["meta"]["id"] for _, _, record in ranked}
        corpus = " ".join(
            json.dumps(record["meta"], ensure_ascii=False) + " " + record["body"]
            for _, _, record in ranked
        ).lower()
        missing_ids = sorted(set(case["expected_ids"]) - returned)
        missing_concepts = sorted(concept for concept in case["required_concepts"] if concept.lower() not in corpus)
        if missing_ids or missing_concepts:
            failures += 1
            print(f"FAIL {case['id']}: missing IDs={missing_ids}, concepts={missing_concepts}")
        else:
            print(f"PASS {case['id']}: {len(ranked)} relevant artifacts")
    print(f"Evaluation: {len(suite['cases']) - failures} passed, {failures} failed.")
    return 1 if failures else 0


def next_id(artifact_type: str, records: list[dict[str, Any]]) -> str:
    prefix = PREFIXES[artifact_type]
    numbers = [int(record["meta"]["id"][1:]) for record in records if record["meta"].get("type") == artifact_type]
    return f"{prefix}{(max(numbers, default=0) + 1):03d}"


def new_command(artifact_type: str, slug: str, source_profile: str | None = None) -> int:
    if artifact_type not in TEMPLATES:
        print(f"Creation is not supported for {artifact_type}.", file=sys.stderr)
        return 2
    if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", slug):
        print("Slug must be lowercase kebab-case.", file=sys.stderr)
        return 2
    records, errors = collect()
    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1
    artifact_id = next_id(artifact_type, records)
    template_name = TEMPLATES[artifact_type]
    if artifact_type == "source" and source_profile:
        template_name = SOURCE_PROFILE_TEMPLATES[source_profile]
    template_path = ROOT / "templates" / template_name
    content = template_path.read_text(encoding="utf-8")
    content = content.replace(f"{PREFIXES[artifact_type]}000", artifact_id)
    content = content.replace("YYYY-MM-DD", dt.date.today().isoformat())
    destination = CONTENT_DIRS[artifact_type] / f"{artifact_id}-{slug}.md"
    if destination.exists():
        print(f"Refusing to overwrite {relative(destination)}", file=sys.stderr)
        return 1
    destination.write_text(content, encoding="utf-8")
    print(relative(destination))
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    subparsers = parser.add_subparsers(dest="command", required=True)

    validate_parser = subparsers.add_parser("validate", help="validate artifact schemas and links")
    validate_parser.add_argument("--strict", action="store_true", help="treat stale-review warnings as failures")

    index_parser = subparsers.add_parser("index", help="generate deterministic indexes and graph")
    index_parser.add_argument("--check", action="store_true", help="fail if generated files are stale")

    query_parser = subparsers.add_parser("query", help="retrieve a bounded, relevance-ranked context window")
    query_parser.add_argument("query")
    query_parser.add_argument("--type", action="append", choices=sorted(CONTENT_DIRS), default=[])
    query_parser.add_argument("--limit", type=int)
    query_parser.add_argument("--max-chars", type=int)

    subparsers.add_parser("status", help="show artifact counts and maturity")
    subparsers.add_parser("eval", help="run retrieval contract evaluations")

    next_parser = subparsers.add_parser("next-id", help="print the next ID for an artifact type")
    next_parser.add_argument("type", choices=sorted(PREFIXES))

    new_parser = subparsers.add_parser("new", help="create an artifact from a template")
    new_parser.add_argument("type", choices=sorted(TEMPLATES))
    new_parser.add_argument("slug")
    new_parser.add_argument(
        "--source-profile",
        choices=sorted(SOURCE_PROFILE_TEMPLATES),
        help="choose a source-specific template (only valid with type=source)",
    )

    export_parser = subparsers.add_parser("export", help="generate an external reading pack")
    export_parser.add_argument("target", choices=["notebooklm"])
    export_parser.add_argument("--check", action="store_true")

    args = parser.parse_args()
    if args.command == "validate":
        return validate_command(args.strict)

    records, errors = collect()
    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1

    if args.command == "index":
        outputs = desired_generated_files(records)
        index_paths = [path for path in outputs if path.parent == ROOT / "indexes" or path == ROOT / "maps" / "graph.json"]
        return write_or_check(outputs, args.check, index_paths)
    if args.command == "export":
        outputs = desired_generated_files(records)
        path = ROOT / "exports" / "notebooklm" / "learning-atlas-research-pack.md"
        return write_or_check(outputs, args.check, [path])
    if args.command == "query":
        return query_command(args.query, args.type, args.limit, args.max_chars)
    if args.command == "status":
        return status_command()
    if args.command == "eval":
        return eval_command()
    if args.command == "next-id":
        print(next_id(args.type, records))
        return 0
    if args.command == "new":
        if args.source_profile and args.type != "source":
            print("--source-profile is only valid when creating a source.", file=sys.stderr)
            return 2
        return new_command(args.type, args.slug, args.source_profile)
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
