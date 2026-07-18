## 2024-07-18 - Caching Models in Memory
**Learning:** Loading and deserializing machine learning models from disk synchronously on every request severely degrades application response latency.
**Action:** Always load and cache machine learning models globally at startup to process inference in-memory efficiently.
