<<<<<<< HEAD
## 2024-07-13 - Cache Models at Startup
**Learning:** Loading and deserializing ML models (like joblib.load) on every request severely degrades response latency and increases disk I/O.
**Action:** Always cache machine learning models globally in memory at application startup rather than synchronously loading them inside route handlers.
=======
## 2024-07-16 - Globals Over Local Loading for ML Models
**Learning:** Loading ML models synchronously from disk via joblib.load() within route handlers creates a massive I/O bottleneck and significantly degrades response latency for each request.
**Action:** Always cache machine learning models in memory by loading them globally at application startup instead of inside individual request handlers.
>>>>>>> a573b4d (Commit changes before rebase)
