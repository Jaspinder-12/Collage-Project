## 2024-05-10 - Global Caching for Machine Learning Models
**Learning:** Loading large Machine Learning models and scalers from disk using `joblib.load` inside an endpoint's request lifecycle adds massive latency to every request.
**Action:** Always load static models into global memory (or cache them locally on the first request) before inference to minimize I/O overhead.
