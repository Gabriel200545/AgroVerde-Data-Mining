"""Cálculo de KPIs de Pérdidas de Cosecha."""
import pandas as pd

def calcular_tasa_perdida_total(df: pd.DataFrame, col_perdida: str = "porcentaje_perdida") -> float:
    """Calcula la tasa promedio de pérdida de cultivo."""
    if col_perdida not in df.columns or df.empty:
        return 0.0
    return float(df[col_perdida].mean())
