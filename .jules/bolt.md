## 2024-03-27 - ML Model Deserialization Overhead
**Learning:** scikit-learn models loaded via joblib block the request thread during deserialization. Loading models per-request adds significant I/O and deserialization latency (especially since the data paths are hardcoded to disk locations).
**Action:** Implement lazy-loading of ML models using global variables. Global model objects in Flask are thread-safe for inference. This ensures the expensive `joblib.load` operation only happens on the first request (or at startup), significantly improving subsequent request latency.
