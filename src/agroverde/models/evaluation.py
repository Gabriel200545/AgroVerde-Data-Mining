"""Evaluación de métricas de desempeño."""
import numpy as np
from typing import Dict, Any

try:
    from sklearn.metrics import mean_squared_error, r2_score, accuracy_score, classification_report
    HAS_SKLEARN = True
except ImportError:
    HAS_SKLEARN = False

class ModelEvaluator:
    """Evaluador de modelos predictivos."""

    @staticmethod
    def evaluate_regression(y_true, y_pred) -> Dict[str, float]:
        if HAS_SKLEARN:
            return {
                "rmse": float(mean_squared_error(y_true, y_pred, squared=False)),
                "r2": float(r2_score(y_true, y_pred))
            }
        else:
            y_t = np.asarray(y_true, dtype=float)
            y_p = np.asarray(y_pred, dtype=float)
            mse = float(np.mean((y_t - y_p) ** 2))
            rmse = float(np.sqrt(mse))
            ss_tot = float(np.sum((y_t - np.mean(y_t)) ** 2))
            ss_res = float(np.sum((y_t - y_p) ** 2))
            r2 = float(1.0 - (ss_res / (ss_tot + 1e-10)))
            return {"rmse": rmse, "r2": r2}

    @staticmethod
    def evaluate_classification(y_true, y_pred) -> Dict[str, Any]:
        if HAS_SKLEARN:
            return {
                "accuracy": float(accuracy_score(y_true, y_pred)),
                "report": classification_report(y_true, y_pred, output_dict=True)
            }
        else:
            y_t = np.asarray(y_true)
            y_p = np.asarray(y_pred)
            acc = float(np.mean(y_t == y_p))
            return {"accuracy": acc, "report": {}}
