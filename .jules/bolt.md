## 2024-06-20 - Global Model Caching in Flask
**Learning:** Loading large machine learning models (like scikit-learn's `sc.sav` and `lr.sav` via `joblib.load`) inside a route handler causes synchronous disk I/O and deserialization on every incoming request, which severely degrades API response latency and throughput.
**Action:** Always load and cache heavy ML models in the global scope during application startup so they reside in memory before the first request is served.
