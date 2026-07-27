## 2024-05-24 - Model Caching Bottleneck
**Learning:** Loading scikit-learn models from disk on every Flask request causes massive I/O bottlenecks and latency. This pattern is common in prototype codebases.
**Action:** Always implement a module-level dictionary cache (e.g., `model_cache = {}`) for ML models to ensure they are loaded into memory exactly once per worker process.
