## 2024-05-24 - Cached ML Models in Memory
**Learning:** Loading machine learning models from disk inside the request handler adds significant synchronous I/O and deserialization overhead to every request, bottlenecking latency.
**Action:** Always load and cache heavy ML models (e.g. scikit-learn models via joblib) into memory at application startup to ensure optimal request performance.
