## 2024-03-30 - [Lazy Load ML Models in Flask]
**Learning:** Deserialization of scikit-learn machine learning models via joblib.load() is a heavy, synchronous I/O operation that blocks the request thread. If placed inside a route, it executes sequentially on every request causing massive latency in this specific Flask architecture.
**Action:** Always lazy-load and cache heavy ML models globally in web applications to prevent per-request I/O blocking.
