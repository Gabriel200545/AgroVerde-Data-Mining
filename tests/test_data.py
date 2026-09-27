import unittest
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "src"))

import pandas as pd
from agroverde.data.cleaner import DataCleaner
from agroverde.data.validator import DataValidator

class TestData(unittest.TestCase):
    def test_remove_duplicates(self):
        df = pd.DataFrame({"a": [1, 1, 2], "b": [3, 3, 4]})
        cleaned = DataCleaner.remove_duplicates(df)
        self.assertEqual(len(cleaned), 2)

    def test_missing_columns(self):
        df = pd.DataFrame({"a": [1], "b": [2]})
        missing = DataValidator.check_missing_columns(df, ["a", "c"])
        self.assertEqual(missing, ["c"])

if __name__ == "__main__":
    unittest.main()
