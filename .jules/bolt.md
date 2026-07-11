## 2024-07-11 - Caching Machine Learning Models in Flask
**Learning:** Loading machine learning models (via joblib) synchronously inside request handlers degrades response latency due to repeated disk I/O and deserialization overhead, acting as a major performance bottleneck.
**Action:** Always load and cache ML models globally at application startup so they reside in memory, ensuring fast and non-blocking predictions during requests.
