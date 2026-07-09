## 2024-07-07 - Global Model Caching
**Learning:** Loading machine learning models synchronously during a request handler introduces significant latency and disk I/O overhead.
**Action:** Always load machine learning models into memory at the global scope during application startup rather than inside the request handler.
