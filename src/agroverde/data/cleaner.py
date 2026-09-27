"""Módulo de limpieza y depuración de datos."""
import pandas as pd
from agroverde.utils.logger import get_logger

logger = get_logger(__name__)

class DataCleaner:
    """Operaciones de depuración de datasets agrícolas."""

    @staticmethod
    def remove_duplicates(df: pd.DataFrame, subset=None) -> pd.DataFrame:
        initial = len(df)
        df_clean = df.drop_duplicates(subset=subset).copy()
        removed = initial - len(df_clean)
        logger.info(f"Registros duplicados eliminados: {removed}")
        return df_clean

    @staticmethod
    def handle_missing_values(df: pd.DataFrame, strategy: str = "mean", cols: list = None) -> pd.DataFrame:
        df_out = df.copy()
        target_cols = cols if cols else df_out.select_dtypes(include=['float64', 'int64']).columns
        
        for col in target_cols:
            if df_out[col].isnull().sum() > 0:
                if strategy == "mean":
                    df_out[col] = df_out[col].fillna(df_out[col].mean())
                elif strategy == "median":
                    df_out[col] = df_out[col].fillna(df_out[col].median())
                elif strategy == "drop":
                    df_out = df_out.dropna(subset=[col])
        logger.info(f"Imputación de nulos aplicada con estrategia '{strategy}'.")
        return df_out
