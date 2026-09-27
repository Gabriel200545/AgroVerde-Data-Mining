"""Módulo para transformación y estructuración de datos."""
import pandas as pd
from agroverde.utils.logger import get_logger

logger = get_logger(__name__)

class DataTransformer:
    """Transformación y normalización de esquemas."""

    @staticmethod
    def parse_dates(df: pd.DataFrame, date_cols: list) -> pd.DataFrame:
        df_out = df.copy()
        for col in date_cols:
            if col in df_out.columns:
                df_out[col] = pd.to_datetime(df_out[col], errors='coerce')
                logger.info(f"Columna '{col}' convertida a datetime.")
        return df_out
