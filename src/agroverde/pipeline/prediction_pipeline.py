"""Pipeline de Predicción en Inferencia."""
import pandas as pd
from agroverde.utils.logger import get_logger

logger = get_logger(__name__)

def run_prediction_pipeline(model, X_new: pd.DataFrame) -> pd.Series:
    logger.info(f"Generando predicciones para {len(X_new)} registros...")
    predictions = model.predict(X_new)
    return pd.Series(predictions, index=X_new.index, name="prediccion_rendimiento")
