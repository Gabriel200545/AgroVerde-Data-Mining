"""Preprocesamiento para modelos de ML."""
import pandas as pd
import numpy as np

try:
    from sklearn.preprocessing import StandardScaler, RobustScaler
    HAS_SKLEARN = True
except ImportError:
    HAS_SKLEARN = False

class SimpleScaler:
    """StandardScaler fallback."""
    def fit_transform(self, X):
        X_arr = np.asarray(X, dtype=float)
        mean = np.mean(X_arr, axis=0)
        std = np.std(X_arr, axis=0) + 1e-8
        return (X_arr - mean) / std

def scale_features(df: pd.DataFrame, cols: list, scaler_type: str = "standard"):
    if HAS_SKLEARN:
        scaler = StandardScaler() if scaler_type == "standard" else RobustScaler()
        scaled_array = scaler.fit_transform(df[cols])
    else:
        scaler = SimpleScaler()
        scaled_array = scaler.fit_transform(df[cols])
        
    scaled_df = pd.DataFrame(scaled_array, columns=[f"{c}_scaled" for c in cols], index=df.index)
    return pd.concat([df, scaled_df], axis=1), scaler
