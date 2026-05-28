## 2024-05-28 - Global Caching of ML Models in Flask
**Learning:** Loading scikit-learn models via joblib inside request handlers causes severe performance degradation due to repetitive disk I/O and deserialization for every request.
**Action:** Always cache heavy assets like machine learning models in memory at the global module scope to reuse across all incoming requests.
