"""Módulo de ingeniería de características."""
import pandas as pd

class FeatureEngineer:
    """Creación de variables sintéticas y combinadas."""

    @staticmethod
    def add_yield_per_water(df: pd.DataFrame) -> pd.DataFrame:
        df_out = df.copy()
        if "rendimiento_ton_ha" in df_out.columns and "volumen_agua_m3" in df_out.columns:
            df_out["ratio_rendimiento_agua"] = df_out["rendimiento_ton_ha"] / (df_out["volumen_agua_m3"] + 1e-5)
        return df_out
