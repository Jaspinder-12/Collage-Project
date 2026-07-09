## 2024-06-21 - Global Model Caching
**Learning:** Loading large machine learning models using `joblib.load()` inside route handlers causes massive synchronous disk I/O and deserialization latency on every single request.
**Action:** Always load machine learning models globally at application startup so they are cached in memory.
