## 2024-07-17 - Caching machine learning models globally
**Learning:** Loading large machine learning models (like those saved with joblib) inside a route handler causes severe synchronous disk I/O and deserialization latency on every request.
**Action:** Always cache these models in memory by loading them globally at startup.
