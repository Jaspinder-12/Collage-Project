## 2024-07-09 - Global Model Caching in Flask
**Learning:** Loading scikit-learn models from disk on every `/predict` request introduces massive synchronous disk I/O and deserialization overhead.
**Action:** Always load machine learning models globally at application startup to cache them in memory.
