## 2024-05-26 - ML Model Loading Bottleneck
**Learning:** Loading machine learning models (like scikit-learn models via joblib) inside a Flask request handler causes severe performance degradation due to repetitive disk I/O and deserialization on every single request.
**Action:** Always load and cache such heavy assets at the module (global) level when the application starts, so they remain in memory and are reused across all incoming requests.
