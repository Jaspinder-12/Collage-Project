## 2026-03-31 - Lazy Loading ML Models
**Learning:** Deserialization of scikit-learn machine learning models via `joblib.load()` is a heavy, synchronous I/O operation that blocks the request thread.
**Action:** These models must be lazy-loaded and cached globally (using a module-level dictionary) rather than loaded sequentially on every request.
