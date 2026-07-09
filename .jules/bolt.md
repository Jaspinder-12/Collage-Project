## 2024-05-20 - Model Loading at Startup
**Learning:** Loading ML models using `joblib.load` inside request handlers causes significant latency degradation due to synchronous disk I/O and deserialization on every request.
**Action:** Always load and cache ML models globally at application startup so they remain in memory across requests.
