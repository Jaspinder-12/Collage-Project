## 2024-05-05 - Lazy-Loading Machine Learning Assets

**Learning:** In Flask applications utilizing heavy ML models, loading assets via `joblib.load()` from disk inside route handlers causes massive performance degradation on every single request.
**Action:** Always implement a module-level cache (e.g., a dictionary) to lazy-load these assets into memory upon the first request, ensuring subsequent requests only perform the fast in-memory lookups.
