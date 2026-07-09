## 2024-05-24 - Global Model Caching for ML APIs
**Learning:** In Flask machine learning applications, loading models (like `joblib.load()`) inside route handlers introduces severe latency bottlenecks due to repeated synchronous disk I/O and deserialization on every request.
**Action:** Always cache ML models globally in memory at application startup to ensure fast request handling. Let missing models fail loudly in production instead of using dummy fallbacks.
