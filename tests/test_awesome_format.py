import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class AwesomeFormatTests(unittest.TestCase):
    def test_awesome_entries_are_well_formed(self) -> None:
        result = subprocess.run(
            [sys.executable, "scripts/check_awesome_entries.py"],
            cwd=ROOT,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            check=False,
        )
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def run_checker_on_text(self, files: dict[str, str]) -> subprocess.CompletedProcess[str]:
        with tempfile.TemporaryDirectory() as tmpdir:
            root = Path(tmpdir)
            for relative_path, text in files.items():
                path = root / relative_path
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_text(text, encoding="utf-8")
            return subprocess.run(
                [sys.executable, str(ROOT / "scripts/check_awesome_entries.py"), str(root)],
                cwd=ROOT,
                text=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                check=False,
            )

    def test_nested_awesome_entries_are_checked(self) -> None:
        result = self.run_checker_on_text(
            {
                "nested/page.md": "# Page\n\n- [Resource](https://example.com/resource): relevance note.\n",
            }
        )
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn("checked 1 awesome resources", result.stdout)

    def test_duplicate_external_urls_fail(self) -> None:
        result = self.run_checker_on_text(
            {
                "a.md": "- [A](https://example.com/resource): first note.\n",
                "nested/b.md": "- [B](https://example.com/resource#section): second note.\n",
            }
        )
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("duplicate resource URL", result.stdout)

    def test_tracking_query_parameters_fail(self) -> None:
        result = self.run_checker_on_text(
            {
                "a.md": "- [A](https://example.com/resource?utm_source=test): note.\n",
            }
        )
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("tracking query parameters", result.stdout)

    def test_local_navigation_links_are_ignored(self) -> None:
        result = self.run_checker_on_text(
            {
                "README.md": "- [Local page](nested/page.md)\n",
                "nested/page.md": "# Local\n",
            }
        )
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn("checked 0 awesome resources", result.stdout)


if __name__ == "__main__":
    unittest.main()
