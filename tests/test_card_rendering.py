import subprocess
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class CardRenderingTests(unittest.TestCase):
    def test_render_card_markdown_outputs_expected_sections(self) -> None:
        result = subprocess.run(
            [
                sys.executable,
                "scripts/render_card_markdown.py",
                "cards/examples/coding_agent_card.yaml",
            ],
            cwd=ROOT,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            check=False,
        )
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn("# Open-World Evaluation Card:", result.stdout)
        self.assertIn("## Verifier Stack", result.stdout)
        self.assertIn("## Monitoring and Rollback", result.stdout)


if __name__ == "__main__":
    unittest.main()
