## 2024-05-24 - Model Loading Performance in Request Handlers
**Learning:** Loading scikit-learn models and scalers via joblib inside request handlers causes severe performance degradation due to repetitive disk I/O and deserialization on every incoming request.
**Action:** Always cache machine learning models globally at the module level in Flask applications so they are reused across requests, and use robust relative paths instead of hardcoded absolute paths to prevent environment-specific failures.
