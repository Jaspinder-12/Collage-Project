## 2024-06-26 - Global Model Caching in Flask
**Learning:** Loading large scikit-learn models (joblib.load) inside route handlers causes significant synchronous disk I/O and deserialization latency on every request, severely degrading backend performance in Python applications.
**Action:** Always load machine learning models and large static assets into memory at the global scope during application startup.
