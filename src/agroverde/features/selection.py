"""Selección de variables relevantes."""
import pandas as pd
from typing import List

def select_top_numeric_features(df: pd.DataFrame, target_col: str, k: int = 5) -> List[str]:
    if target_col not in df.columns:
        return []
    corrs = df.select_dtypes(include=['float64', 'int64']).corr()[target_col].abs()
    top_features = corrs.drop(labels=[target_col]).nlargest(k).index.tolist()
    return top_features
