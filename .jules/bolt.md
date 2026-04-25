## 2024-04-25 - Caching ML Models in Flask
**Learning:** Loading scikit-learn models from disk on every request is a massive performance bottleneck and causes unnecessary I/O blocking.
**Action:** Always load models globally into a cache dictionary on the first request to ensure they stay in memory for subsequent requests, drastically improving prediction latency.
