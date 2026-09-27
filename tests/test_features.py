import unittest
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "src"))

import pandas as pd
from agroverde.features.engineering import FeatureEngineer

class TestFeatures(unittest.TestCase):
    def test_add_yield_per_water(self):
        df = pd.DataFrame({"rendimiento_ton_ha": [10.0], "volumen_agua_m3": [100.0]})
        df_res = FeatureEngineer.add_yield_per_water(df)
        self.assertIn("ratio_rendimiento_agua", df_res.columns)

if __name__ == "__main__":
    unittest.main()
