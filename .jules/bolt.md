## 2024-05-24 - Lazy load machine learning models to eliminate I/O bottleneck
**Learning:** Loading scikit-learn models from disk (`joblib.load`) on every request blocks the main thread with heavy I/O operations and model deserialization, significantly degrading per-request performance and causing a severe latency bottleneck in the Flask app.
**Action:** When working with ML models in web endpoints, always introduce a module-level `model_cache` dictionary to lazily load models on the first request and cache them in memory for all subsequent concurrent requests.
