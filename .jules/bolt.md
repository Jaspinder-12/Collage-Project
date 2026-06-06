## 2024-06-06 - Machine Learning Model Loading in Web Requests
**Learning:** Loading ML models from disk (e.g., via `joblib.load`) inside request handlers creates a massive I/O bottleneck and significantly increases latency for every prediction.
**Action:** Always cache models and scalers globally at the module level so they are loaded once at startup and reused across all incoming requests.
