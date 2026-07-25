## 2025-07-24 - Model Loading Latency
**Learning:** Loading machine learning models (deserializing via joblib) inside a Flask request handler introduces significant synchronous disk I/O and parsing overhead, degrading response latency for every request.
**Action:** Always load and cache ML models globally at application startup instead of inside route handlers.
