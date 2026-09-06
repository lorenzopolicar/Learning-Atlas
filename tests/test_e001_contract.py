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
        cls.inference_schema = json.loads((PACKAGE / "inference.schema.json").read_text(encoding="utf-8"))
        cls.inference = json.loads((PACKAGE / "inference.fixture.json").read_text(encoding="utf-8"))
        cls.events = {
            path.stem: json.loads(path.read_text(encoding="utf-8"))
            for path in sorted(FIXTURES.glob("*.json"))
        }

    def test_schema_declares_version_and_core_requirements(self) -> None:
        self.assertEqual(self.schema["$schema"], "https://json-schema.org/draft/2020-12/schema")
        self.assertEqual(self.schema["properties"]["schemaVersion"]["const"], "0.2.0")
        required = set(self.schema["required"])
        self.assertTrue(
            {
                "eventId",
                "eventType",
                "recordedAt",
                "learnerRef",
                "observer",
                "evidenceLane",
                "assistanceEnvelope",
                "outcome",
                "accessibility",
                "governance",
            }.issubset(required)
        )
        self.assertNotIn("intendedInference", self.schema["properties"])
        self.assertNotIn("inferenceBoundary", self.schema["properties"])

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
                self.assertEqual(event["schemaVersion"], "0.2.0")
                self.assertEqual(event["governance"]["stakes"], "low")
                self.assertTrue(prohibited.issubset(event["governance"]["prohibitedUses"]))
                self.assertTrue(event["accessibility"]["accessSupportsPreserved"])
                self.assertTrue(event["governance"]["learnerVisible"])
                self.assertTrue(event["governance"]["contestable"])
                self.assertIn("recordedAt", event)
                self.assertIn("observer", event)
                self.assertNotIn("intendedInference", event)
                self.assertNotIn("inferenceBoundary", event)

    def test_ai_assisted_events_preserve_the_decision_process(self) -> None:
        for name in ("ai-assisted-trial", "correction"):
            event = self.events[name]
            with self.subTest(fixture=name):
                self.assertEqual(event["evidenceLane"], "ai-assisted")
                self.assertEqual(event["assistanceEnvelope"]["substantiveGenerationState"], "used")
                self.assertEqual(
                    event["assistanceEnvelope"]["toolsDeclaredUsed"],
                    event["assistanceEnvelope"]["toolsObservedUsed"],
                )
                self.assertIn("useEvidenceBasis", event["assistanceEnvelope"])
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
        self.assertIn("screen-reader", event["assistanceEnvelope"]["toolsObservedUsed"])

    def test_self_reported_confidence_is_not_model_uncertainty(self) -> None:
        event = self.events["ai-assisted-trial"]
        confidence = event["preAdvice"]["selfReportedConfidence"]
        self.assertEqual(confidence["scaleMin"], 0)
        self.assertEqual(confidence["scaleMax"], 1)
        self.assertIn("elicitationMethod", confidence)
        self.assertNotIn("confidence", event["preAdvice"])

    def test_scored_outcomes_preserve_assertion_provenance(self) -> None:
        for name, event in self.events.items():
            with self.subTest(fixture=name):
                assertion = event["outcome"]["scoringAssertion"]
                self.assertIn("assertedBy", assertion)
                self.assertIn("rubricVersion", assertion)
                self.assertIn("evidenceRuleVersion", assertion)

    def test_inference_is_versioned_and_separate_from_observations(self) -> None:
        self.assertEqual(self.inference_schema["properties"]["schemaVersion"]["const"], "0.1.0")
        self.assertEqual(self.inference["schemaVersion"], "0.1.0")
        self.assertTrue(set(self.inference["derivedFrom"]).issubset({event["eventId"] for event in self.events.values()}))
        self.assertEqual(self.inference["temporalPolicy"]["basis"], "no-decay")
        self.assertIn("reviewAfter", self.inference["temporalPolicy"])
        self.assertIn("authorizedUntil", self.inference["governance"])
        self.assertIn("retentionUntil", self.events["ai-assisted-trial"]["governance"])

    def test_correction_is_append_only_and_references_the_original(self) -> None:
        original = self.events["ai-assisted-trial"]
        correction = self.events["correction"]
        self.assertEqual(correction["eventType"], "correction")
        self.assertEqual(correction["governance"]["correctionOf"], original["eventId"])
        self.assertNotEqual(correction["eventId"], original["eventId"])
        self.assertTrue(correction["governance"]["correctionReason"])


if __name__ == "__main__":
    unittest.main()
