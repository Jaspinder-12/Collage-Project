## 2024-06-23 - Global Model Caching
**Learning:** In the BigMart Sales Prediction application (`app.py`), machine learning models must be cached in memory by loading them globally at startup rather than inside the `/predict` route handler to prevent synchronous disk I/O and deserialization from degrading response latency.
**Action:** Always load large machine learning models at the module level rather than per-request level in Flask applications to ensure fast request handling.
