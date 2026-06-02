import json
import subprocess
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
VALIDATOR = ROOT / "scripts" / "validate_card.py"


class ValidatorTests(unittest.TestCase):
    def run_validator(self, path: Path) -> subprocess.CompletedProcess[str]:
        return subprocess.run(
            [sys.executable, str(VALIDATOR), str(path)],
            cwd=ROOT,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            check=False,
        )

    def test_all_cards_are_valid(self) -> None:
        cards = sorted((ROOT / "cards").glob("**/*.yaml"))
        self.assertGreaterEqual(len(cards), 4)
        for card in cards:
            with self.subTest(card=card.relative_to(ROOT)):
                result = self.run_validator(card)
                self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_missing_required_section_fails(self) -> None:
        result = self.run_validator(ROOT / "tests" / "fixtures" / "invalid_missing_verifier_stack.yaml")
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("verifier_stack: missing required section", result.stdout)

    def test_empty_required_fields_fail(self) -> None:
        result = self.run_validator(ROOT / "tests" / "fixtures" / "invalid_empty_required_fields.yaml")
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("system_name: must be a non-empty string", result.stdout)
        self.assertIn("claim_type.description: must be a non-empty string", result.stdout)
        self.assertIn("human_signal_role.benchmarks_or_judges: must be a non-empty list", result.stdout)

    def test_schema_is_parseable_json(self) -> None:
        schema_path = ROOT / "cards" / "open_world_evaluation_card.schema.json"
        with schema_path.open(encoding="utf-8") as handle:
            schema = json.load(handle)
        self.assertEqual(schema["title"], "Open-World Evaluation Card")
        self.assertIn("verifier_stack", schema["required"])


if __name__ == "__main__":
    unittest.main()
