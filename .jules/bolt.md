## 2024-07-12 - Flask ML Model Loading Optimization
**Learning:** Instantiating `joblib.load()` inside a Flask request handler (`@app.route`) for machine learning models causes massive synchronous disk I/O and deserialization overhead on every single request, acting as a severe performance bottleneck.
**Action:** Always load machine learning models globally at application startup so they are cached in memory and can be reused concurrently across multiple requests.
