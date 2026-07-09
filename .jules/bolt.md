## 2024-05-24 - Model Loading Bottleneck
**Learning:** Loading scikit-learn models (joblib.load) inside a route handler causes severe synchronous I/O and deserialization latency on every request.
**Action:** Always load and cache machine learning models globally at application startup.
