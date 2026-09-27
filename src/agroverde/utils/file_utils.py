"""Utilidades para manejo de archivos e I/O."""
import json
import joblib
from pathlib import Path
from typing import Any

def save_json(data: Any, filepath: Path):
    filepath.parent.mkdir(parents=True, exist_ok=True)
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

def load_json(filepath: Path) -> Any:
    with open(filepath, "r", encoding="utf-8") as f:
        return json.load(f)

def save_model(model: Any, filepath: Path):
    filepath.parent.mkdir(parents=True, exist_ok=True)
    joblib.dump(model, filepath)

def load_model(filepath: Path) -> Any:
    return joblib.load(filepath)
