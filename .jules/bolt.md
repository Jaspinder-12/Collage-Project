## 2024-06-24 - Caching Machine Learning Models Globally
**Learning:** Loading large machine learning models (via joblib or pickle) synchronously inside a route handler severely bottlenecks request latency due to repeated disk I/O and deserialization.
**Action:** Always load and cache ML models globally at application startup so they reside in memory, allowing fast inference on incoming requests without redundant loading overhead.
