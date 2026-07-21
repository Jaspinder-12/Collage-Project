## 2024-07-21 - Caching Model at Startup
**Learning:** Found that loading models inside request handlers degrades latency due to synchronous disk I/O and deserialization.
**Action:** Always load machine learning models to memory globally at startup in Flask apps.
