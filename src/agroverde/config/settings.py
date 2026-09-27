"""Configuración general del proyecto."""
from pathlib import Path
from os import getenv

try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass

class Settings:
    PROJECT_NAME: str = "AgroVerde - Data Mining"
    BASE_DIR: Path = Path(__file__).resolve().parent.parent.parent.parent
    DATA_DIR: Path = BASE_DIR / "data"
    RAW_DATA_DIR: Path = DATA_DIR / "raw"
    INTERIM_DATA_DIR: Path = DATA_DIR / "interim"
    PROCESSED_DATA_DIR: Path = DATA_DIR / "processed"
    MODELS_DIR: Path = BASE_DIR / "models"
    REPORTS_DIR: Path = BASE_DIR / "reports"
    LOG_LEVEL: str = getenv("LOG_LEVEL", "INFO")

settings = Settings()
