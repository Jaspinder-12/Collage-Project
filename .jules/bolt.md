## 2024-05-15 - Synchronous Model Loading in Route Handlers
**Learning:** Loading machine learning models (e.g., `joblib.load`) synchronously inside request handlers severely degrades latency due to blocking disk I/O and deserialization.
**Action:** Always hoist resource-intensive file loading into the global scope to cache them in memory at application startup.
