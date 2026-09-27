"""Módulo para validación de la integridad y estructura de datos."""
import pandas as pd
from typing import List
from agroverde.utils.logger import get_logger

logger = get_logger(__name__)

class DataValidator:
    """Validaciones de esquemas y rangos de datos."""

    @staticmethod
    def check_missing_columns(df: pd.DataFrame, required_cols: List[str]) -> List[str]:
        missing = [col for col in required_cols if col not in df.columns]
        if missing:
            logger.warning(f"Columnas faltantes detectadas: {missing}")
        return missing

    @staticmethod
    def validate_range(df: pd.DataFrame, col: str, min_val: float, max_val: float) -> bool:
        if col not in df.columns:
            return False
        out_of_bounds = df[(df[col] < min_val) | (df[col] > max_val)]
        valid = len(out_of_bounds) == 0
        if not valid:
            logger.warning(f"Se encontraron {len(out_of_bounds)} registros fuera de rango [{min_val}, {max_val}] en '{col}'.")
        return valid
