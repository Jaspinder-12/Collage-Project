## 2024-05-17 - Model Caching for Flask APIs
**Learning:** Loading large Machine Learning models (e.g. via joblib) synchronously inside a request handler causes severe performance bottlenecks due to expensive disk I/O on every request.
**Action:** Always implement a global or module-level cache for ML assets and lazy-load them on the first request (or at startup) to keep subsequent inference times fast. Ensure the cache checks for all interdependent assets simultaneously to avoid partial cache states.
