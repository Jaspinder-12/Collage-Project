## 2024-06-14 - Global Caching for ML Models
**Learning:** Loading large machine learning models (deserialization via joblib) synchronously within route handlers blocks the main thread and significantly degrades request latency on every API call.
**Action:** Always load and cache heavy read-only assets (like ML models) in memory globally at application startup instead of inside request handlers.
