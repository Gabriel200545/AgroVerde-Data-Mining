"""Pipeline de Preprocesamiento de Datos."""
import pandas as pd
from agroverde.data.cleaner import DataCleaner
from agroverde.data.transformer import DataTransformer
from agroverde.features.engineering import FeatureEngineer
from agroverde.utils.logger import get_logger

logger = get_logger(__name__)

def run_preprocessing_pipeline(df: pd.DataFrame) -> pd.DataFrame:
    logger.info("Iniciando Pipeline de Preprocesamiento...")
    df_clean = DataCleaner.remove_duplicates(df)
    df_clean = DataCleaner.handle_missing_values(df_clean, strategy="median")
    df_feat = FeatureEngineer.add_yield_per_water(df_clean)
    logger.info("Pipeline de Preprocesamiento finalizado con éxito.")
    return df_feat
