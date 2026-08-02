## 2024-07-13 - Cache Models at Startup
**Learning:** Loading and deserializing ML models (like joblib.load) on every request severely degrades response latency and increases disk I/O.
**Action:** Always cache machine learning models globally in memory at application startup rather than synchronously loading them inside route handlers.

## 2024-07-18 - Caching Models in Memory
**Learning:** Loading and deserializing machine learning models from disk synchronously on every request severely degrades application response latency.
**Action:** Always load and cache machine learning models globally at startup to process inference in-memory efficiently.
