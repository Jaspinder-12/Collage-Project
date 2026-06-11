## 2024-06-11 - Global Model Loading in Flask
**Learning:** Loading machine learning models (via joblib) inside a Flask route handler causes severe performance bottlenecks due to expensive disk I/O on every request.
**Action:** Always load models globally during application initialization so they remain in memory across requests.
