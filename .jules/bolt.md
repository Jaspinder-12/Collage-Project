## 2024-04-10 - Lazy Loading ML Models in Flask
**Learning:** Loading scikit-learn machine learning models via `joblib.load()` is a heavy, synchronous I/O operation that blocks the request thread. Loading these models on every request inside a Flask route causes significant latency and poor performance.
**Action:** Lazily load and cache models using a global module-level dictionary (`model_cache = {}`) so they are only loaded once on the first request and shared across all subsequent concurrent requests.
