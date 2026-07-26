## 2024-07-26 - Hoisting ML Models
**Learning:** Loading `joblib` models synchronously inside a Flask route handler causes significant latency due to repeated disk I/O and deserialization for every request. Hardcoded absolute paths also break deployment.
**Action:** Always load large resources like machine learning models at module scope using relative paths (`os.path.join(__file__)`) to cache them in memory when the application starts, dramatically improving response times while remaining cross-environment compatible.
