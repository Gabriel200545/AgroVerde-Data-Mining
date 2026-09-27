"""Análisis de correlaciones entre variables agrícolas."""
import pandas as pd

def compute_correlation_matrix(df: pd.DataFrame, method: str = "pearson") -> pd.DataFrame:
    numeric_df = df.select_dtypes(include=['float64', 'int64'])
    return numeric_df.corr(method=method)
