## 2024-05-24 - Model I/O Bottleneck
**Learning:** Loading machine learning models (like scikit-learn or joblib dumps) inside a request handler causes severe latency because of expensive disk I/O and deserialization on every request.
**Action:** Always load static models globally at application startup to keep them in memory for fast inference.
