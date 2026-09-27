import unittest
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "src"))

import numpy as np
from agroverde.models.regression import train_yield_regressor

class TestModels(unittest.TestCase):
    def test_train_yield_regressor(self):
        X = np.array([[1, 2], [3, 4], [5, 6]])
        y = np.array([10, 20, 30])
        model = train_yield_regressor(X, y)
        preds = model.predict(X)
        self.assertEqual(len(preds), 3)

if __name__ == "__main__":
    unittest.main()
