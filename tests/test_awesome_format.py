import subprocess
import sys
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


if __name__ == "__main__":
    unittest.main()
