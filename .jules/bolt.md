## 2024-05-01 - Caching ML Models in Flask Routes
**Learning:** Loading machine learning models (e.g., via `joblib.load`) inside a Flask route handler causes expensive and redundant disk I/O on every single request, severely degrading API response times.
**Action:** Always lazy-load ML models into a module-level dictionary (e.g., `model_cache = {}`) so the application only pays the disk I/O cost once during its lifecycle.
