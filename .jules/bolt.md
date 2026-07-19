## 2025-02-14 - Global Model Caching in Flask
**Learning:** Loading `joblib` machine learning models inside the Flask request handler causes synchronous disk I/O and deserialization on every single request, which severely degrades API response latency and throughput.
**Action:** Always hoist file loading operations (e.g., `joblib.load`) to the global scope to cache resources at startup. Use relative paths with `os.path.dirname(os.path.abspath(__file__))` instead of hardcoded absolute paths to prevent application crashes during cross-environment deployments.
