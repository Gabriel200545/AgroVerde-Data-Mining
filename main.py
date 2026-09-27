"""Punto de entrada principal para el proyecto AgroVerde - Data Mining."""
import sys
from pathlib import Path

# Agregar la carpeta src al PYTHONPATH
sys.path.insert(0, str(Path(__file__).resolve().parent / "src"))

import pandas as pd
import numpy as np
from agroverde.config import settings
from agroverde.utils.logger import get_logger
from agroverde.utils.helpers import print_section_header
from agroverde.pipeline.preprocessing_pipeline import run_preprocessing_pipeline
from agroverde.pipeline.training_pipeline import run_training_pipeline
from agroverde.kpis.calculator import KPICalculator

logger = get_logger("AgroVerdeMain")

def main():
    print_section_header("AgroVerde - Data Mining System")
    logger.info(f"Iniciando proyecto: {settings.PROJECT_NAME}")
    logger.info(f"Directorio base: {settings.BASE_DIR}")

    # Simulación de carga de datos sintéticos agrícolas
    np.random.seed(42)
    n_samples = 100
    df_dummy = pd.DataFrame({
        "id_lote": [f"LOTE-{i:03d}" for i in range(1, n_samples + 1)],
        "tipo_cultivo": np.random.choice(["Aguacate", "Maíz", "Café"], n_samples),
        "rendimiento_ton_ha": np.random.normal(15, 3, n_samples),
        "volumen_agua_m3": np.random.normal(1200, 200, n_samples),
        "porcentaje_perdida": np.random.uniform(2, 12, n_samples),
        "produccion_total_ton": np.random.normal(150, 30, n_samples)
    })

    # 1. Pipeline de preprocesamiento
    df_processed = run_preprocessing_pipeline(df_dummy)

    # 2. Cálculo de KPIs
    kpis = KPICalculator.compute_all_kpis(df_processed)
    print_section_header("KPIs Calculados")
    for k, v in kpis.items():
        print(f"  • {k}: {v:.2f}")

    # 3. Pipeline de entrenamiento demo
    X = df_processed[["volumen_agua_m3", "porcentaje_perdida", "ratio_rendimiento_agua"]]
    y = df_processed["rendimiento_ton_ha"]
    
    print_section_header("Entrenamiento de Modelo Predictivo")
    model, metrics = run_training_pipeline(X, y)
    
    logger.info("Ejecución finalizada exitosamente.")

if __name__ == "__main__":
    main()
