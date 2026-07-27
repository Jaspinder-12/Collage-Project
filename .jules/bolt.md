## 2025-03-01 - Cache ML assets in memory for Flask apps
**Learning:** Loading scikit-learn models or scalers from disk (`joblib.load`) on every request causes huge disk I/O latency.
**Action:** Always load and cache ML assets at the application level (or lazily in a cached dictionary) so it only happens once per worker/server startup.
