## 2024-07-15 - Global Model Caching in Flask
**Learning:** Loading machine learning models dynamically within a request handler causes severe performance degradation due to synchronous disk I/O and deserialization overhead blocking the main thread on every request.
**Action:** Always cache models globally in memory at application startup to ensure low-latency predictions.
