## 2024-06-07 - Avoid loading models on every request
**Learning:** Loading machine learning models (like scikit-learn models via joblib) inside a Flask request handler causes expensive disk I/O on every single request, significantly increasing response times and reducing throughput.
**Action:** Globally cache models at the module level. Ensure the application can still initialize by wrapping the load logic in a try/except block with mock fallback classes if the model files are missing.
