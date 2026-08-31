import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
sys.path.insert(0, str(SCRIPTS))

import research_gateway as gateway  # noqa: E402


class ResearchGatewayTests(unittest.TestCase):
    def test_openalex_candidate_is_normalized_and_bounded(self) -> None:
        candidate = gateway.candidate_from_openalex(
            {
                "id": "https://openalex.org/W123",
                "doi": "https://doi.org/10.1234/example",
                "display_name": "A bounded study",
                "type": "article",
                "publication_date": "2026-01-02",
                "authorships": [{"author": {"display_name": "Ada Researcher"}}],
                "primary_location": {"source": {"display_name": "Journal of Tests", "type": "journal"}},
                "open_access": {"is_oa": True},
                "best_oa_location": {"pdf_url": "https://example.org/paper.pdf", "license": "cc-by"},
                "abstract_inverted_index": {"Learning": [0], "persists": [1]},
                "referenced_works": ["https://openalex.org/W1"],
                "cited_by_count": 4,
                "is_retracted": False,
            },
            "learning retention",
        )
        self.assertEqual(candidate["source_type"], "journal-article")
        self.assertEqual(candidate["canonical_identifiers"][0]["scheme"], "doi")
        self.assertEqual(candidate["summary"], "Learning persists")
        self.assertEqual(gateway.validate_candidate(candidate), [])

    def test_provider_records_for_same_doi_merge_without_fragmentation(self) -> None:
        openalex = gateway.candidate_from_openalex(
            {
                "id": "https://openalex.org/W123",
                "doi": "https://doi.org/10.1234/EXAMPLE",
                "display_name": "One work",
                "type": "article",
                "authorships": [],
                "open_access": {"is_oa": True},
                "best_oa_location": {"landing_page_url": "https://example.org/open"},
            }
        )
        crossref = gateway.candidate_from_crossref(
            {
                "title": ["One work"],
                "type": "journal-article",
                "URL": "https://doi.org/10.1234/example",
                "abstract": "<jats:p>A <jats:italic>clean</jats:italic> abstract.</jats:p>",
                "author": [{"given": "Ada", "family": "Researcher"}],
                "update-to": [],
            },
            "10.1234/example",
        )
        self.assertEqual(openalex["candidate_id"], crossref["candidate_id"])
        merged = gateway.merge_candidates(openalex, crossref)
        self.assertEqual(merged["candidate_id"], openalex["candidate_id"])
        self.assertEqual(merged["summary"], "A clean abstract.")
        self.assertEqual(merged["access"]["status"], "open")
        self.assertIn("crossref-doi-resolved", merged["verification"]["checks"])

    def test_candidate_identity_tokens_normalize_transcript_urls(self) -> None:
        episode = {"canonical_url": "https://example.org/episodes/learning"}
        transcript = {"canonical_url": "https://example.org/episodes/learning/transcript"}
        overlap = gateway.candidate_identity_tokens(episode).intersection(
            gateway.candidate_identity_tokens(transcript)
        )
        self.assertTrue(overlap)

    def test_feed_parser_preserves_episode_and_transcript_provenance(self) -> None:
        feed = b"""<?xml version="1.0"?>
        <rss xmlns:podcast="https://podcastindex.org/namespace/1.0" xmlns:itunes="http://www.itunes.com/dtds/podcast-1.0.dtd" version="2.0">
          <channel><title>Learning Signals</title>
            <item><title>Can AI help us learn?</title><guid>episode-7</guid>
              <link>https://example.org/episodes/7</link><pubDate>Sun, 30 Aug 2026 01:00:00 GMT</pubDate>
              <enclosure url="https://cdn.example.org/7.mp3" type="audio/mpeg" />
              <itunes:duration>00:42:10</itunes:duration>
              <podcast:transcript url="https://example.org/episodes/7.vtt" type="text/vtt" language="en" />
            </item>
          </channel>
        </rss>"""
        records = gateway.parse_feed(feed, "https://example.org/feed.xml")
        self.assertEqual(len(records), 1)
        self.assertEqual(records[0]["source_type"], "podcast-episode")
        self.assertEqual(records[0]["transcript"]["availability"], "publisher-provided")
        self.assertEqual(records[0]["transcript"]["url"], "https://example.org/episodes/7.vtt")
        self.assertIn("expert-perspective", records[0]["epistemic_roles"])
        self.assertEqual(gateway.parse_feed(feed, "https://example.org/feed.xml", query="not this episode"), [])

    def test_timed_transcript_returns_locators_not_a_full_transcript(self) -> None:
        transcript = """WEBVTT

00:00:01.000 --> 00:00:04.000
Host: Welcome to the show.

00:00:04.000 --> 00:00:09.000
Guest: Learning is more than completion.
"""
        segments = gateway.parse_timed_text(transcript)
        self.assertEqual(len(segments), 2)
        self.assertEqual(segments[1]["start"], "00:00:04.000")
        self.assertNotIn("full_transcript", segments[0])

    def test_speaker_timestamps_are_preserved_with_bounded_excerpts(self) -> None:
        text = "Host (00:01) Welcome. Guest (00:07) Learning is not completion. Host (00:15) Why?"
        locators = gateway._timestamp_locators(text)
        excerpts = gateway.timestamped_speaker_segments(text)
        self.assertEqual(locators[0]["label"], "Host")
        self.assertEqual(excerpts[1]["speaker"], "Guest")
        self.assertIn("Learning is not completion", excerpts[1]["excerpt"])

    def test_plain_podcast_transcript_keeps_speaker_and_bounded_text(self) -> None:
        source = "Andy (00:01)\nWelcome to the show.\n\nKelly (00:07)\nToday we discuss learning."
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "episode.txt"
            path.write_text(source, encoding="utf-8")
            result = gateway.extract_transcript(str(path), max_excerpts=1, max_segments=10)
        self.assertEqual(result["segment_count"], 2)
        self.assertEqual(result["excerpt_segments"][0]["speaker"], "Andy")
        self.assertEqual(result["excerpt_segments"][0]["text"], "Welcome to the show.")
        self.assertNotIn("Today we discuss learning.", json.dumps(result["excerpt_segments"]))

    def test_jsonld_metadata_extracts_episode_identity(self) -> None:
        metadata = gateway.jsonld_metadata(
            ['{"@type":"PodcastEpisode","name":"Learning with AI","datePublished":"2026-01-13","author":[{"name":"Ada"}],"duration":"PT23M"}']
        )
        self.assertEqual(metadata["title"], "Learning with AI")
        self.assertEqual(metadata["creators"], ["Ada"])

    def test_candidate_validation_rejects_nested_full_text(self) -> None:
        candidate = gateway.base_candidate(
            title="Unsafe candidate",
            source_type="web-essay",
            canonical_url="https://example.org/source",
            provider="test",
        )
        candidate["provider_payload"] = {"full_text": "copyrighted text"}
        errors = gateway.validate_candidate(candidate)
        self.assertTrue(any("full_text" in error for error in errors))

    def test_document_fetch_requires_explicit_rights_basis(self) -> None:
        with self.assertRaises(gateway.GatewayError):
            gateway.fetch_lawful_document("https://example.org/paper.pdf", "found-on-the-web")

    def test_local_extraction_is_bounded(self) -> None:
        temp_dir = Path(tempfile.gettempdir()) / "learning-atlas-tests"
        temp_dir.mkdir(exist_ok=True)
        path = temp_dir / "sample.txt"
        path.write_text("learning " * 2_000, encoding="utf-8")
        result = gateway.extract_document(str(path), max_chars=1_000)
        self.assertEqual(result["method"], "plain-text")
        self.assertLessEqual(len(result["excerpt"]), 1_000)

    def test_docling_markdown_does_not_leak_embedded_images(self) -> None:
        raw = "Before ![Figure](data:image/png;base64,AAAABBBB) after"
        cleaned = gateway.sanitize_extracted_markdown(raw)
        self.assertNotIn("base64", cleaned)
        self.assertIn("Image omitted", cleaned)

    def test_mcp_server_initializes_and_lists_tools(self) -> None:
        messages = [
            {"jsonrpc": "2.0", "id": 1, "method": "initialize", "params": {"protocolVersion": "2025-03-26"}},
            {"jsonrpc": "2.0", "method": "notifications/initialized", "params": {}},
            {"jsonrpc": "2.0", "id": 2, "method": "tools/list", "params": {}},
            {"jsonrpc": "2.0", "id": 3, "method": "tools/call", "params": {"name": "research_capabilities", "arguments": {}}},
        ]
        result = subprocess.run(
            [sys.executable, str(SCRIPTS / "atlas_mcp.py")],
            input="\n".join(json.dumps(item) for item in messages) + "\n",
            cwd=ROOT,
            check=False,
            capture_output=True,
            text=True,
            timeout=10,
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        responses = [json.loads(line) for line in result.stdout.splitlines()]
        self.assertEqual(responses[0]["result"]["serverInfo"]["name"], "learning-atlas-research")
        tools = responses[1]["result"]["tools"]
        self.assertIn("stage_source_candidate", {tool["name"] for tool in tools})
        self.assertFalse(responses[2]["result"]["isError"])

    def test_agent_mcp_configs_are_parseable(self) -> None:
        with (ROOT / ".codex" / "config.toml").open("rb") as handle:
            import tomllib

            codex_config = tomllib.load(handle)
        claude_config = json.loads((ROOT / ".mcp.json").read_text(encoding="utf-8"))
        self.assertIn("atlas_research", codex_config["mcp_servers"])
        self.assertIn("atlas-research", claude_config["mcpServers"])


if __name__ == "__main__":
    unittest.main()
