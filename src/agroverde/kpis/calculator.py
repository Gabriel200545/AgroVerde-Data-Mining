"""Calculador centralizado de KPIs."""
import pandas as pd
from typing import Dict, Any
from .rendimiento import calcular_rendimiento_promedio
from .perdidas import calcular_tasa_perdida_total
from .produccion import calcular_produccion_total
from .riego import calcular_eficiencia_riego

class KPICalculator:
    """Orquestador de cálculo de Indicadores Clave de Desempeño."""

    @staticmethod
    def compute_all_kpis(df: pd.DataFrame) -> Dict[str, Any]:
        return {
            "rendimiento_promedio_ton_ha": calcular_rendimiento_promedio(df),
            "tasa_perdida_promedio_pct": calcular_tasa_perdida_total(df),
            "produccion_total_ton": calcular_produccion_total(df),
            "eficiencia_riego_m3_ton": calcular_eficiencia_riego(df),
        }
