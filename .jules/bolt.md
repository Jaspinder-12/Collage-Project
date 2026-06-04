## 2024-06-04 - Caching ML Models at Module Level
**Learning:** Loading scikit-learn/joblib models inside the route handler means reading from disk on every single request, which is a major performance bottleneck for a Flask API.
**Action:** Cache the models at the module level (outside the request cycle) and handle missing files gracefully with mock classes to avoid CI crashes while still enabling fast predictions in production.
