## 2024-07-05 - Model Caching in Flask
**Learning:** Loading scikit-learn models from disk (via `joblib.load()`) synchronously inside route handlers introduces massive response latency and blocks the main thread, causing severe performance bottlenecks.
**Action:** Always load machine learning models globally at application startup so they are cached in memory.
