## 2024-06-15 - Global Model Caching in Flask
**Learning:** Machine learning models loaded inside a route handler cause synchronous disk I/O and deserialization on every request, severely degrading latency.
**Action:** Cache models in memory by loading them globally at application startup instead.
