import subprocess
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CLI = [sys.executable, str(ROOT / "scripts" / "atlas.py")]


class AtlasHarnessTests(unittest.TestCase):
    def run_cli(self, *args: str) -> subprocess.CompletedProcess[str]:
        return subprocess.run(
            [*CLI, *args],
            cwd=ROOT,
            check=False,
            capture_output=True,
            text=True,
        )

    def test_repository_is_valid(self) -> None:
        result = self.run_cli("validate", "--strict")
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_generated_views_are_current(self) -> None:
        result = self.run_cli("index", "--check")
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        result = self.run_cli("export", "notebooklm", "--check")
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_query_is_bounded_and_returns_traceable_ids(self) -> None:
        result = self.run_cli(
            "query",
            "learning performance",
            "--type",
            "claim",
            "--type",
            "principle",
            "--limit",
            "2",
            "--max-chars",
            "1200",
        )
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn("artifact(s)", result.stdout)
        self.assertLessEqual(len(result.stdout), 1400)

    def test_next_id_is_deterministic(self) -> None:
        first = self.run_cli("next-id", "claim")
        second = self.run_cli("next-id", "claim")
        self.assertEqual(first.returncode, 0, first.stderr)
        self.assertEqual(first.stdout, second.stdout)
        self.assertRegex(first.stdout.strip(), r"^C\d{3}$")

    def test_source_profiles_are_available(self) -> None:
        result = self.run_cli("new", "source", "not-a-real-source", "--source-profile", "media", "--help")
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn("--source-profile", result.stdout)

    def test_retrieval_contract_evaluations(self) -> None:
        result = self.run_cli("eval")
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn("0 failed", result.stdout)


if __name__ == "__main__":
    unittest.main()
