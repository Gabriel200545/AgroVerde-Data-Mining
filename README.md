# AgroVerde - Data Mining

Sistema integral de minería de datos, ingeniería de características, análisis de KPIs y modelado predictivo para la optimización de procesos agrícolas en **AgroVerde**.

---

## Estructura del Proyecto

```text
agroverde-data-mining/
├── .github/workflows/       # Integración continua (GitHub Actions)
├── .vscode/                 # Configuraciones de VSCode
├── data/                    # Datasets (raw, interim, processed, external)
├── notebooks/               # Cuadernos Jupyter para investigación y EDA
├── src/agroverde/           # Código fuente modular en Python
│   ├── config/              # Configuraciones globales y constantes
│   ├── data/                # Ingesta, limpieza, transformación y validación
│   ├── kpis/                # Lógica agronómica e indicadores clave
│   ├── analysis/            # Estadística descriptiva y gráficos
│   ├── features/            # Ingeniería y selección de variables
│   ├── models/              # Modelos ML (Clasificación, Regresión, Clustering)
│   ├── pipeline/            # Pipelines automatizados de entrenamiento e inferencia
│   └── utils/               # Loggers, helpers y utilidades I/O
├── models/                  # Artefactos de modelos entrenados (.joblib, .pkl)
├── reports/                 # Informes, tablas y figuras generadas
├── tests/                   # Pruebas unitarias con Pytest
├── docs/                    # Documentación del proyecto y metodologías
├── .env.example             # Ejemplo de variables de entorno
├── .gitignore               # Archivos ignorados por Git
├── pyproject.toml           # Configuración de paquete Python
├── requirements.txt         # Dependencias del proyecto
└── main.py                  # Punto de entrada principal
```

---

## Instalación y Configuración

1. **Clonar el repositorio:**
   ```bash
   git clone https://github.com/agroverde/agroverde-data-mining.git
   cd agroverde-data-mining
   ```

2. **Crear y activar entorno virtual:**
   ```bash
   python -m venv .venv
   # Windows:
   .venv\Scripts\activate
   # Linux/macOS:
   source .venv/bin/activate
   ```

3. **Instalar dependencias:**
   ```bash
   pip install -r requirements.txt
   pip install -e .
   ```

4. **Configurar variables de entorno:**
   ```bash
   cp .env.example .env
   ```

---

## Ejecución

- **Ejecutar Pipeline Principal:**
  ```bash
  python main.py
  ```

- **Ejecutar Pruebas Unitarias:**
  ```bash
  pytest
  ```

- **Lanzar Jupyter Notebooks:**
  ```bash
  jupyter lab
  ```
