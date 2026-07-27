
## 2024-05-28 - [Performance Bottleneck] Cache machine learning models
**Learning:** Machine learning models loaded via joblib.load() are extremely slow and blocking operations. Loading them per-request in Flask causes severe performance latency and limits request throughput.
**Action:** Always lazy-load models into global variables within Flask routes. Initialize variables as None outside the route, and load them inside the route only if they are None to ensure models are loaded once and reused across subsequent requests.
