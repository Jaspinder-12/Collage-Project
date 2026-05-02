## 2024-05-02 - Lazy Loading ML Models in Request Handlers
**Learning:** Loading machine learning models from disk (e.g., using `joblib.load`) inside a request handler creates a massive performance bottleneck, causing slow responses and blocking the server thread on every single request.
**Action:** Always load large assets like ML models globally or use a module-level lazy-loading cache (`model_cache = {}`) so they are only loaded into memory once during the application's lifecycle.
