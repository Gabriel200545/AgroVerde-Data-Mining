"""Utilidades para generación de gráficos descriptivos."""
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from pathlib import Path

def plot_correlation_heatmap(df: pd.DataFrame, output_path: Path = None):
    plt.figure(figsize=(10, 8))
    numeric_df = df.select_dtypes(include=['float64', 'int64'])
    sns.heatmap(numeric_df.corr(), annot=True, cmap="YlGnBu", fmt=".2f")
    plt.title("Matriz de Correlación Agrícola")
    plt.tight_layout()
    if output_path:
        output_path.parent.mkdir(parents=True, exist_ok=True)
        plt.savefig(output_path)
    plt.close()
