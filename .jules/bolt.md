## 2024-05-09 - Lazy Loading ML Models
**Learning:** Loading large ML models (`joblib.load`) synchronously on every prediction request blocks the main thread and causes severe latency.
**Action:** Implement lazy loading and cache models in application context/memory to ensure models are loaded from disk only once.
