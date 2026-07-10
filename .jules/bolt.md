## 2024-05-17 - Global Model Caching in Flask
**Learning:** Loading machine learning models inside route handlers causes significant synchronous disk I/O and deserialization latency on every request, degrading performance.
**Action:** Always load and cache ML models in memory at the global scope during application startup for predictive endpoints.
