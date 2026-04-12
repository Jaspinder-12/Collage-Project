## 2024-11-20 - Lazy Loading Machine Learning Models
**Learning:** Loading scikit-learn machine learning models via `joblib.load()` is a heavy, synchronous I/O operation. Loading these models on every request blocks the main thread, introducing significant per-request latency.
**Action:** Implement lazy-loading via a global `model_cache` dictionary (e.g., `model_cache = {}`) inside the Flask route. The models are loaded once on the first request and subsequently accessed from memory, dramatically reducing inference time.
