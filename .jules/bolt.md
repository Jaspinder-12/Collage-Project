## 2024-07-24 - Model Loading Bottleneck
**Learning:** Hardcoded absolute paths and synchronous disk I/O deserialization of machine learning models within route handlers drastically block the main thread and degrade response latency on every request.
**Action:** Hoist file loading operations like joblib.load to the global scope at startup using dynamic relative paths constructed with os.path.join and __file__.
