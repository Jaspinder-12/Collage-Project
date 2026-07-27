## 2024-05-27 - Caching Machine Learning Models in Flask
**Learning:** Loading machine learning models from disk on every single request in a Flask route is a significant performance bottleneck. Disk I/O is slow, and repeatedly instantiating models (like `joblib.load`) adds unnecessary overhead.
**Action:** Always load machine learning models and scalers once at application startup (or lazily on the first request) and cache them in memory. In Flask, avoid using the `global` keyword directly to prevent `flake8 F824` errors; instead, use a module-level dictionary to store the cached models.
