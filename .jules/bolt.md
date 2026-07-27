## 2024-05-20 - Lazy Loading ML Models in Flask
**Learning:** `joblib.load()` is a heavy, synchronous I/O operation that blocks the request thread. Loading scikit-learn models sequentially on every request causes significant per-request latency.
**Action:** Always lazy-load and cache these models globally instead of loading them within the route logic, since they are stateless during inference and can be safely shared across concurrent requests.
