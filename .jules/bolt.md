## 2024-04-30 - Lazy Loading ML Models
**Learning:** Loading `scikit-learn` models and scalers from disk using `joblib.load()` on every request creates a massive performance bottleneck and blocks the main thread.
**Action:** Always cache loaded ML artifacts in memory (e.g., using a module-level `model_cache` dictionary) after the first load to reuse them across subsequent route handlers, reducing response latency.
