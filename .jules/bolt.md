## 2024-05-18 - Lazy-load and Cache ML Models

**Learning:** Deserialization of scikit-learn machine learning models via `joblib.load()` is a heavy, synchronous I/O operation that blocks the request thread. If executed on every request, it introduces significant per-request latency. Scikit-learn machine learning models loaded via joblib are stateless during inference, meaning a single instance can be safely shared across concurrent requests.
**Action:** When implementing Flask endpoints that depend on ML models, models must be lazy-loaded and cached globally rather than loaded sequentially on every request. Use a module-level dictionary (e.g., `model_cache = {}`) to cleanly implement lazy-loading without `global` scope issues.
