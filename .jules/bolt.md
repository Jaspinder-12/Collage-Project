## 2024-04-09 - Lazy loading and caching ML models in Flask
**Learning:** Deserializing scikit-learn models via `joblib.load()` synchronously on every request creates a significant performance bottleneck.
**Action:** Lazy-load these models into a global module-level dictionary (`model_cache = {}`) during the first request to eliminate repetitive disk I/O and deserialization latency for all subsequent requests.
