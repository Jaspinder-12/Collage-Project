## 2024-05-23 - Global Model Caching in Flask
**Learning:** Loading scikit-learn models and scalers via `joblib.load` inside request handlers causes severe performance degradation due to repetitive disk I/O and deserialization.
**Action:** Always cache heavy assets like ML models in memory at the global module scope to reuse them across requests.
