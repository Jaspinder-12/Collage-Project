## 2024-04-29 - Cache ML Models In Memory
**Learning:** In Flask machine learning applications, calling `joblib.load()` on every prediction request leads to an expensive disk I/O bottleneck.
**Action:** Implement a module-level cache dictionary (e.g., `model_cache = {}`) to lazily load and store ML models in memory upon the first request, drastically improving response times for subsequent requests.
