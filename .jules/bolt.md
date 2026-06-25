## 2025-06-25 - Caching Machine Learning Models in Memory
**Learning:** Loading machine learning models (like scikit-learn's `joblib.load`) involves synchronous disk I/O and deserialization. Placing these calls inside a Flask route handler causes them to run on every single request, which severely degrades response latency and creates a major performance bottleneck for concurrent requests.
**Action:** Always cache machine learning models globally at application startup so they are loaded into memory exactly once, ensuring rapid and efficient inference during request handling.
