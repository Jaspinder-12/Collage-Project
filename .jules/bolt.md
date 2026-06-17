## 2024-06-17 - Caching Machine Learning Models Globally
**Learning:** Loading machine learning models (like scikit-learn's `joblib.load`) synchronously inside a route handler severely degrades response latency and blocks the main thread on every request due to repeated disk I/O and deserialization.
**Action:** Always load and cache heavy machine learning models in memory at the global scope during application startup, ensuring they fail loudly early rather than dynamically at request time.
