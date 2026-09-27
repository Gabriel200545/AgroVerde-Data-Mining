"""Análisis estadístico descriptivo."""
import pandas as pd
from typing import Dict, Any

class DescriptiveAnalysis:
    """Generador de resúmenes estadísticos."""

    @staticmethod
    def get_summary_statistics(df: pd.DataFrame) -> pd.DataFrame:
        return df.describe(include='all').transpose()
