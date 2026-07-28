## 2024-07-28 - Model Loading in Route Handler
**Learning:** Loading and deserializing machine learning models directly inside route handlers causes severe performance degradation, as synchronous disk I/O and deserialization occur on every single request.
**Action:** Always hoist file loading operations (e.g., joblib.load) to the global scope to cache resources in memory at startup, converting absolute paths to relative paths for portability.
