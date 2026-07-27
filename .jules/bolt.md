## 2024-05-14 - Fix Request Bottleneck
**Learning:** The application had a severe I/O bottleneck in the `/predict` route because the machine learning models (`sc` and `model`) were deserialized using `joblib.load()` synchronously on every single request. In performance testing, this increased request latency dramatically and limited throughput.
**Action:** Always load large machine learning model artifacts into memory at application startup (global scope) rather than inside request handlers, enabling high-throughput request processing by reusing in-memory objects across connections.
