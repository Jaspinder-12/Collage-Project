## 2024-07-08 - Model Caching for Flask Latency
**Learning:** In the BigMart Sales Prediction app, placing `joblib.load` inside route handlers causes severe latency spikes by triggering synchronous disk I/O and deserialization for every request.
**Action:** Always load machine learning models globally at application startup to cache them in memory and ensure sub-millisecond route execution.
