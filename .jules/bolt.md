## 2024-05-18 - Model Caching for Inference
**Learning:** Loading machine learning models from disk on every API request causes massive I/O overhead and latency. In environments without the models (like CI), absolute hardcoded paths cause fatal `FileNotFoundError` crashes.
**Action:** Cache models globally outside the request handler using relative paths, and provide mock fallback classes during initialization to ensure robust, high-performance API endpoints.
