## 2024-05-24 - Model Loading Bottleneck in Flask Routes
**Learning:** Loading large machine learning models (e.g., via `joblib.load`) inside a route handler causes synchronous disk I/O and deserialization overhead on every single request, severely degrading application latency and throughput.
**Action:** Always load and cache machine learning models in memory at the global scope during application startup, ensuring they are ready before the server begins accepting requests. Use relative paths that fail loudly if the models are missing in production.
