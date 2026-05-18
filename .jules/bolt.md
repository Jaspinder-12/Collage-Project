## 2024-05-18 - Model Loading Bottleneck
**Learning:** Loading scikit-learn models (joblib.load) inside a request handler causes severe performance degradation as disk I/O and deserialization happen on every request.
**Action:** Always cache machine learning assets (models, scalers) in memory globally to reuse them across requests, ensuring the cache condition checks for all interdependent assets together.
