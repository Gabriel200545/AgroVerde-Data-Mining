"""Módulo para carga e ingesta de datos agrícolas."""
import pandas as pd
from pathlib import Path
from typing import Union
from agroverde.utils.logger import get_logger

logger = get_logger(__name__)

class DataLoader:
    """Clase encargada de la lectura de archivos de datos."""

    @staticmethod
    def load_csv(file_path: Union[str, Path], **kwargs) -> pd.DataFrame:
        path = Path(file_path)
        logger.info(f"Cargando archivo CSV desde: {path}")
        if not path.exists():
            raise FileNotFoundError(f"El archivo {path} no existe.")
        return pd.read_csv(path, **kwargs)

    @staticmethod
    def load_parquet(file_path: Union[str, Path]) -> pd.DataFrame:
        path = Path(file_path)
        logger.info(f"Cargando archivo Parquet desde: {path}")
        return pd.read_parquet(path)
