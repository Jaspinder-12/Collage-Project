## 2024-06-12 - Prevent Per-Request Model Loading
**Learning:** Loading machine learning models from disk using `joblib.load` inside a request handler causes severe performance bottlenecks due to repeated I/O and deserialization on every API call.
**Action:** Always load models into the global scope at application startup so they reside in memory, significantly reducing API latency and overhead.
