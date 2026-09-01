import json
import unittest
import uuid
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PACKAGE = ROOT / "experiments" / "E001-ai-mediated-stewardship-probe"
FIXTURES = PACKAGE / "fixtures"


class E001ContractTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.schema = json.loads((PACKAGE / "event.schema.json").read_text(encoding="utf-8"))
        cls.events = {
            path.stem: json.loads(path.read_text(encoding="utf-8"))
            for path in sorted(FIXTURES.glob("*.json"))
        }

    def test_schema_declares_version_and_core_requirements(self) -> None:
        self.assertEqual(self.schema["$schema"], "https://json-schema.org/draft/2020-12/schema")
        self.assertEqual(self.schema["properties"]["schemaVersion"]["const"], "0.1.0")
        required = set(self.schema["required"])
        self.assertTrue(
            {
                "eventId",
                "eventType",
                "learnerRef",
                "intendedInference",
                "evidenceLane",
                "assistanceEnvelope",
                "outcome",
                "accessibility",
                "inferenceBoundary",
                "governance",
            }.issubset(required)
        )

    def test_fixtures_preserve_pilot_governance_invariants(self) -> None:
        self.assertEqual(set(self.events), {"accessible-independent-followup", "ai-assisted-trial", "correction"})
        prohibited = {
            "learner-ranking",
            "credentialing",
            "employment-decision",
            "silent-mastery-update",
        }
        for name, event in self.events.items():
            with self.subTest(fixture=name):
                uuid.UUID(event["eventId"])
                self.assertEqual(event["schemaVersion"], "0.1.0")
                self.assertEqual(event["intendedInference"]["stakes"], "low")
                self.assertTrue(prohibited.issubset(event["intendedInference"]["prohibitedUses"]))
                self.assertTrue(event["accessibility"]["accessSupportsPreserved"])
                self.assertTrue(event["governance"]["learnerVisible"])
                self.assertTrue(event["governance"]["contestable"])
                self.assertIn("does not", event["inferenceBoundary"]["prohibitedInference"].lower())

    def test_ai_assisted_events_preserve_the_decision_process(self) -> None:
        for name in ("ai-assisted-trial", "correction"):
            event = self.events[name]
            with self.subTest(fixture=name):
                self.assertEqual(event["evidenceLane"], "ai-assisted")
                self.assertEqual(event["assistanceEnvelope"]["substantiveGenerationState"], "used")
                self.assertIn("systemProvenance", event)
                self.assertIn("preAdvice", event)
                self.assertIn("intervention", event)
                self.assertIn("postAdvice", event)

    def test_delayed_independent_fixture_keeps_access_support_but_removes_generation(self) -> None:
        event = self.events["accessible-independent-followup"]
        self.assertEqual(event["evidenceLane"], "accessible-independent")
        self.assertEqual(event["outcome"]["supportState"], "accessible-independent")
        self.assertEqual(event["outcome"]["delaySeconds"], 7 * 24 * 60 * 60)
        self.assertEqual(event["assistanceEnvelope"]["substantiveGenerationState"], "not-available")
        self.assertIn("screen-reader", event["assistanceEnvelope"]["toolsUsed"])

    def test_correction_is_append_only_and_references_the_original(self) -> None:
        original = self.events["ai-assisted-trial"]
        correction = self.events["correction"]
        self.assertEqual(correction["eventType"], "correction")
        self.assertEqual(correction["governance"]["correctionOf"], original["eventId"])
        self.assertNotEqual(correction["eventId"], original["eventId"])
        self.assertTrue(correction["governance"]["correctionReason"])


if __name__ == "__main__":
    unittest.main()
