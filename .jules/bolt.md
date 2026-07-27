## 2024-04-21 - Lazy loading Machine Learning Models
**Learning:** Loading machine learning models from disk on every Flask request is a severe performance bottleneck.
**Action:** Cache the models in a module-level dictionary (`model_cache`) and lazy-load them on the first request to eliminate disk I/O on subsequent predictions.