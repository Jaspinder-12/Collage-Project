## 2024-06-13 - Expensive Operations in Request Handlers
**Learning:** Loading machine learning models from disk (`joblib.load`) inside a route handler causes severe performance degradation, as the file I/O and deserialization happen synchronously on every single request, blocking the main thread and destroying throughput.
**Action:** Always load static resources like machine learning models into memory at application startup (global scope) and reuse them across requests to minimize latency and maximize throughput.
