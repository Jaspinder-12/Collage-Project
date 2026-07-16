## 2024-07-16 - Globals Over Local Loading for ML Models
**Learning:** Loading ML models synchronously from disk via joblib.load() within route handlers creates a massive I/O bottleneck and significantly degrades response latency for each request.
**Action:** Always cache machine learning models in memory by loading them globally at application startup instead of inside individual request handlers.
