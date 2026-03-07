
## 2024-05-24 - [Optimize Model Loading]
**Learning:** Loading large objects like machine learning models per request in Flask introduces significant file I/O and deserialization latency.
**Action:** Move ML model loading via `joblib.load()` to the global scope to only load once at application startup, reducing prediction latency. Implement a graceful fallback to prevent unhandled exceptions if the models are missing during CI/CD checks.
