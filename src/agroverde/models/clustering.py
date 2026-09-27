"""Modelos de Clustering (ej. Segmentación de Lotes / Suelos)."""
import numpy as np

try:
    from sklearn.cluster import KMeans
    HAS_SKLEARN = True
except ImportError:
    HAS_SKLEARN = False

class SimpleKMeans:
    """Implementación básica de KMeans como fallback."""
    def __init__(self, n_clusters=3, max_iter=100):
        self.n_clusters = n_clusters
        self.max_iter = max_iter
        self.cluster_centers_ = None

    def fit_predict(self, X):
        X_arr = np.asarray(X, dtype=float)
        indices = np.random.choice(len(X_arr), self.n_clusters, replace=False)
        self.cluster_centers_ = X_arr[indices]
        
        labels = np.zeros(len(X_arr))
        for _ in range(self.max_iter):
            dists = np.linalg.norm(X_arr[:, np.newaxis] - self.cluster_centers_, axis=2)
            labels = np.argmin(dists, axis=1)
            new_centers = np.array([X_arr[labels == k].mean(axis=0) if np.sum(labels == k) > 0 else self.cluster_centers_[k] for k in range(self.n_clusters)])
            if np.allclose(self.cluster_centers_, new_centers):
                break
            self.cluster_centers_ = new_centers
        return labels

def cluster_zones(X, n_clusters: int = 3):
    if HAS_SKLEARN:
        kmeans = KMeans(n_clusters=n_clusters, random_state=42)
        labels = kmeans.fit_predict(X)
        return kmeans, labels
    else:
        kmeans = SimpleKMeans(n_clusters=n_clusters)
        labels = kmeans.fit_predict(X)
        return kmeans, labels
