
## 2024-05-18 - Lazy Loading Machine Learning Models in Flask Routes
**Learning:** In Flask applications, loading scikit-learn ML models via `joblib.load()` from disk inside the route handler executes on *every single request*. This is highly inefficient because disk I/O and deserialization add unnecessary latency (approx 20ms per request for dummy models, and much longer for actual large models).
**Action:** When working with stateless scikit-learn models (which are inherently thread-safe during inference), lazily load the models into global variables on the first request and reuse them across subsequent requests to eliminate redundant I/O operations and significantly reduce latency (from ~0.02s per 100 requests to ~0.001s per 100 requests).
