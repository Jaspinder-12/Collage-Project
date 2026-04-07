## 2024-05-24 - Model Loading Bottleneck in Flask
**Learning:** Deserialization of scikit-learn machine learning models via `joblib.load()` is a heavy, synchronous I/O operation that blocks the request thread. If executed inside a route handler on every request, it creates a severe per-request latency bottleneck.
**Action:** Always implement lazy-loading with a module-level global cache (e.g. `model_cache = {}`) for machine learning models in Flask apps, ensuring they are loaded only once and safely shared across concurrent requests.
