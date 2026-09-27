import unittest
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "src"))

import pandas as pd
from agroverde.kpis.rendimiento import calcular_rendimiento_promedio
from agroverde.kpis.calculator import KPICalculator

class TestKPIs(unittest.TestCase):
    def test_calcular_rendimiento_promedio(self):
        df = pd.DataFrame({"rendimiento_ton_ha": [10.0, 20.0, 30.0]})
        val = calcular_rendimiento_promedio(df)
        self.assertEqual(val, 20.0)

    def test_kpi_calculator(self):
        df = pd.DataFrame({
            "rendimiento_ton_ha": [10.0, 20.0],
            "porcentaje_perdida": [5.0, 10.0],
            "produccion_total_ton": [100.0, 200.0],
            "volumen_agua_m3": [1000.0, 2000.0]
        })
        res = KPICalculator.compute_all_kpis(df)
        self.assertEqual(res["rendimiento_promedio_ton_ha"], 15.0)
        self.assertEqual(res["produccion_total_ton"], 300.0)

if __name__ == "__main__":
    unittest.main()
