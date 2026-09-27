"""Cálculo de KPIs de Eficiencia de Riego."""
import pandas as pd

def calcular_eficiencia_riego(df: pd.DataFrame, col_agua: str = "volumen_agua_m3", col_prod: str = "produccion_total_ton") -> float:
    """Calcula m3 de agua utilizados por tonelada producida."""
    if col_agua not in df.columns or col_prod not in df.columns or df[col_prod].sum() == 0:
        return 0.0
    return float(df[col_agua].sum() / df[col_prod].sum())
