## 2024-04-28 - Caching machine learning models in Flask
**Learning:** Loading machine learning models from disk on every single request using `joblib.load()` introduces significant performance bottlenecks due to disk I/O and deserialization latency.
**Action:** Implement lazy-loading with a module-level cache dictionary (`model_cache = {}`) to store the loaded models in memory, reusing them across subsequent requests.
