## 2024-06-01 - Global Caching for Machine Learning Models
**Learning:** Loading heavy ML models (e.g., using `joblib.load`) inside a request handler causes severe performance degradation, as the model is deserialized from disk on every single request.
**Action:** Always load and cache heavy assets like models at the module (global) level during application startup so they are retained in memory and reused across all requests.
