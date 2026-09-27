"""Pipeline de Entrenamiento de Modelos."""
import pandas as pd
from agroverde.models.regression import train_yield_regressor
from agroverde.models.evaluation import ModelEvaluator
from agroverde.utils.logger import get_logger

logger = get_logger(__name__)

def run_training_pipeline(X, y):
    logger.info("Iniciando Pipeline de Entrenamiento...")
    model = train_yield_regressor(X, y)
    preds = model.predict(X)
    metrics = ModelEvaluator.evaluate_regression(y, preds)
    logger.info(f"Entrenamiento completado. Métricas: {metrics}")
    return model, metrics
