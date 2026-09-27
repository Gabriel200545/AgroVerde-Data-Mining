"""Constantes globales del proyecto AgroVerde."""

RANDOM_SEED = 42

# Nombres estándar de columnas
COL_FECHA = "fecha"
COL_LOTE = "id_lote"
COL_CULTIVO = "tipo_cultivo"
COL_RENDIMIENTO = "rendimiento_ton_ha"
COL_AGUA_RIEGO = "volumen_agua_m3"
COL_PERDIDA = "porcentaje_perdida"

# Umbrales
MAX_PERDIDA_ACEPTABLE = 15.0  # Porcentaje
UMBRAL_RIEGO_EFICIENTE = 0.85
