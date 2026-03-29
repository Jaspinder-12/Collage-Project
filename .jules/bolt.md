## 2024-03-29 - Lazy-loading ML Models in Flask
**Learning:** scikit-learn machine learning models loaded via joblib are stateless during inference, meaning a single lazily-loaded global model instance can be safely shared across concurrent requests without thread-safety issues.
**Action:** When working on ML web APIs, ensure that heavy, synchronous I/O operations like model deserialization are lazy-loaded and cached globally to prevent blocking the request thread and causing significant per-request latency.
