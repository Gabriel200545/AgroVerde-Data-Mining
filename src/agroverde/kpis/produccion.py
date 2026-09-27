"""Cálculo de KPIs de Producción Total."""
import pandas as pd

def calcular_produccion_total(df: pd.DataFrame, col_produccion: str = "produccion_total_ton") -> float:
    """Suma la producción total cosechada en toneladas."""
    if col_produccion not in df.columns or df.empty:
        return 0.0
    return float(df[col_produccion].sum())
