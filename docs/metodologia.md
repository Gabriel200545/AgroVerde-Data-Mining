# Metodología CRISP-DM Aplicada

El proyecto utiliza el marco **CRISP-DM** (Cross-Industry Standard Process for Data Mining):

1. **Comprensión del Negocio (Business Understanding)**:
   - Optimización de rendimiento agrícola por hectárea.
   - Reducción de porcentaje de pérdidas post-cosecha.
   - Eficiencia en la utilización de agua de riego.

2. **Comprensión de los Datos (Data Understanding)**:
   - Exploración de series temporales de cosecha y sensores en lotes (`notebooks/01_exploracion_inicial.ipynb`).

3. **Preparación de los Datos (Data Preparation)**:
   - Limpieza, imputación de nulos y feature engineering (`src/agroverde/data/` y `src/agroverde/features/`).

4. **Modelado (Modeling)**:
   - Regresión de rendimiento, clasificación de riesgos y clustering de zonas (`src/agroverde/models/`).

5. **Evaluación (Evaluation)**:
   - Validación cruzada y métricas agronómicas (`src/agroverde/models/evaluation.py`).

6. **Despliegue (Deployment)**:
   - Pipelines automatizados ejecutables mediante `main.py`.
