## 2024-05-24 - Global ML Model Loading
**Learning:** Loading machine learning models (like scikit-learn models) from disk inside a request handler causes severe performance bottlenecks due to repeated disk I/O and deserialization overhead on every single request.
**Action:** Always cache heavily loaded ML models or assets globally at application startup rather than per request, but ensure absolute paths are converted to relative paths so they work in all environments.
