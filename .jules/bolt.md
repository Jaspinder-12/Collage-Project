## 2024-06-16 - Global Model Caching in Flask
**Learning:** Loading machine learning models from disk inside route handlers causes significant synchronous I/O blocks, heavily degrading response latency under load.
**Action:** Always load and cache machine learning models globally at application startup rather than per-request.
