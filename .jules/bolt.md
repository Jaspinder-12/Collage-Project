## 2024-07-13 - Cache Models at Startup
**Learning:** Loading and deserializing ML models (like joblib.load) on every request severely degrades response latency and increases disk I/O.
**Action:** Always cache machine learning models globally in memory at application startup rather than synchronously loading them inside route handlers.

## 2025-02-18 - Latency from Synchronous Model Loading in Flask
**Learning:** In Flask/Python applications loading heavy resources (like scikit-learn machine learning models via joblib or pickle), dynamically loading them from disk within the request handler (e.g., inside the `/predict` route) introduces significant synchronous disk I/O and CPU-intensive deserialization overhead on *every single incoming request*, which creates a massive performance bottleneck. Additionally, hardcoded absolute paths (like Windows `D:\projects\...` paths) will cause severe import crashes on deployment or CI.
**Action:** Always hoist resource-intensive deserialization/loading operations to the global scope so they are executed exactly once during startup, caching the objects in memory for near-instantaneous inference during requests. Always use relative path construction (e.g., `os.path.join(os.path.dirname(os.path.abspath(__file__)), ...)`) instead of hardcoded absolute paths to guarantee environment portability.
