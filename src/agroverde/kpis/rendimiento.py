"""Cálculo de KPIs de Rendimiento Agrícola."""
import pandas as pd

def calcular_rendimiento_promedio(df: pd.DataFrame, col_rendimiento: str = "rendimiento_ton_ha") -> float:
    """Calcula el rendimiento promedio por hectárea."""
    if col_rendimiento not in df.columns or df.empty:
        return 0.0
    return float(df[col_rendimiento].mean())

def calcular_rendimiento_por_lote(df: pd.DataFrame, col_lote: str = "id_lote", col_rendimiento: str = "rendimiento_ton_ha") -> pd.Series:
    """Calcula el rendimiento promedio agrupado por lote."""
    return df.groupby(col_lote)[col_rendimiento].mean()
