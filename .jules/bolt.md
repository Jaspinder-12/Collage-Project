## 2024-05-19 - Global Model Caching in Flask
**Learning:** Loading scikit-learn models (via joblib) inside request handlers causes severe performance degradation due to repetitive disk I/O and deserialization.
**Action:** Always load machine learning models globally at application startup to cache them in memory and reuse across requests.
