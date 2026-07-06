## 2024-05-30 - Global Model Caching in Flask
**Learning:** Loading scikit-learn machine learning models via joblib within a Flask route handler causes synchronous disk I/O and deserialization latency on every request, creating a severe performance bottleneck.
**Action:** Always load and cache heavy machine learning models globally at application startup to ensure they reside in memory, significantly improving route response latency.
