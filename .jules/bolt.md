## 2024-07-01 - Global Caching for ML Models
**Learning:** Loading large machine learning models synchronously via disk I/O in route handlers severely degrades response latency.
**Action:** Cache models in memory by loading them globally at application startup.
