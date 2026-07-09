## 2024-06-08 - Caching Models in Flask
**Learning:** Loading machine learning models from disk on every request is a severe performance bottleneck.
**Action:** Cache models at the module level using relative paths so they are only loaded once on startup, improving latency.
