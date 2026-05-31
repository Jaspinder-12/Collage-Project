## 2024-05-24 - Global ML Model Caching
**Learning:** Loading heavy ML assets like models and scalers inside Flask route handlers blocks the server on every request, resulting in massive redundant disk I/O and latency.
**Action:** Always cache these assets at the module level (globally) during application startup, replacing hardcoded absolute paths with dynamic relative paths to ensure cross-environment compatibility.
