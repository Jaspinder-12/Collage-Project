## 2024-05-25 - Caching ML Models Globally
**Learning:** Loading scikit-learn models via joblib inside request handlers causes severe performance degradation due to repetitive disk I/O and deserialization on every request.
**Action:** Always load and cache heavy assets like ML models globally at the module level when the application starts, and mock the loading library (e.g., joblib) during test collection if the files are missing.
