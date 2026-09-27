"""Modelos de Clasificación (ej. Grado de Calidad de Cultivo)."""
import numpy as np

try:
    from sklearn.ensemble import RandomForestClassifier
    HAS_SKLEARN = True
except ImportError:
    HAS_SKLEARN = False

class SimpleClassifier:
    """Clasificador simple como fallback sin dependencias externas."""
    def __init__(self):
        self.classes_ = None
        self.majority_class = None

    def fit(self, X, y):
        self.classes_, counts = np.unique(y, return_counts=True)
        self.majority_class = self.classes_[np.argmax(counts)]
        return self

    def predict(self, X):
        return np.full(shape=(len(X),), fill_value=self.majority_class)

def train_crop_classifier(X, y):
    if HAS_SKLEARN:
        clf = RandomForestClassifier(n_estimators=100, random_state=42)
        clf.fit(X, y)
        return clf
    else:
        clf = SimpleClassifier()
        clf.fit(X, y)
        return clf
