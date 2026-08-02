## 2024-07-13 - Cache Models at Startup
**Learning:** Loading and deserializing ML models (like joblib.load) on every request severely degrades response latency and increases disk I/O.
**Action:** Always cache machine learning models globally in memory at application startup rather than synchronously loading them inside route handlers.
