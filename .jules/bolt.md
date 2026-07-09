## 2024-06-28 - Cache Machine Learning Models at Startup
**Learning:** Loading large machine learning models (via `joblib.load`) from disk synchronously inside a route handler introduces massive disk I/O and deserialization overhead on every single HTTP request, severely degrading application throughput and latency.
**Action:** Always load and cache static assets like machine learning models into memory globally at application startup so that request handlers only perform fast, in-memory inference.
