## 2024-04-01 - Lazy-load ML models to eliminate per-request I/O bottleneck
**Learning:** Deserialization of scikit-learn machine learning models via `joblib.load()` is a heavy, synchronous I/O operation that blocks the request thread. If loaded sequentially on every request, it introduces massive latency overhead.
**Action:** Always ensure that machine learning models in Flask are lazy-loaded and cached globally (e.g., using a module-level dictionary) so they are only loaded into memory once and shared across subsequent concurrent requests.
