## 2024-06-29 - Loading ML models on every request
**Learning:** Loading large ML model files (e.g., joblib.load) inside a route handler causes synchronous disk I/O and deserialization bottlenecks on every request, severely degrading latency.
**Action:** Always load and cache ML models globally at application startup to ensure immediate availability and faster request processing.
