import subprocess
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class QualityLinterTests(unittest.TestCase):
    def run_script(self, script: str, *args: str) -> subprocess.CompletedProcess[str]:
        return subprocess.run(
            [sys.executable, str(ROOT / "scripts" / script), *args],
            cwd=ROOT,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            check=False,
        )

    def test_example_cards_pass_quality_lint(self) -> None:
        cards = sorted((ROOT / "cards" / "examples").glob("**/*.yaml"))
        result = self.run_script("lint_card_quality.py", *[str(card) for card in cards])
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_placeholder_card_fails(self) -> None:
        result = self.run_script("lint_card_quality.py", "tests/fixtures/invalid_placeholder_card.yaml")
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("placeholder text remains", result.stdout)

    def test_vague_rollback_authority_fails(self) -> None:
        result = self.run_script("lint_card_quality.py", "tests/fixtures/invalid_no_rollback_authority.yaml")
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("revision_authority: authority is too vague", result.stdout)


if __name__ == "__main__":
    unittest.main()
