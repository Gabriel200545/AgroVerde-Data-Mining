"""Modelos de Regresión (ej. Predicción de Rendimiento)."""
import numpy as np

try:
    from sklearn.ensemble import GradientBoostingRegressor
    HAS_SKLEARN = True
except ImportError:
    HAS_SKLEARN = False

class SimpleRegressor:
    """Regresor lineal simple como fallback sin dependencias externas."""
    def __init__(self):
        self.weights = None
        self.intercept = None

    def fit(self, X, y):
        X_arr = np.asarray(X, dtype=float)
        y_arr = np.asarray(y, dtype=float)
        if X_arr.ndim == 1:
            X_arr = X_arr.reshape(-1, 1)
        X_design = np.c_[np.ones(X_arr.shape[0]), X_arr]
        res, _, _, _ = np.linalg.lstsq(X_design, y_arr, rcond=None)
        self.intercept = res[0]
        self.weights = res[1:]
        return self

    def predict(self, X):
        X_arr = np.asarray(X, dtype=float)
        if X_arr.ndim == 1:
            X_arr = X_arr.reshape(-1, 1)
        return X_arr @ self.weights + self.intercept

def train_yield_regressor(X, y):
    if HAS_SKLEARN:
        model = GradientBoostingRegressor(n_estimators=100, random_state=42)
        model.fit(X, y)
        return model
    else:
        model = SimpleRegressor()
        model.fit(X, y)
        return model
