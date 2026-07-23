## 2024-07-23 - Caching ML Models in Flask
**Learning:** Loading scikit-learn models (`sc.sav`, `lr.sav`) inside a request handler (like `/predict`) causes massive synchronous disk I/O and deserialization overhead on every request, severely degrading latency.
**Action:** Always load static models in the global scope at application startup. Ensure absolute file paths are converted to relative paths using `__file__` to maintain portability across environments.
