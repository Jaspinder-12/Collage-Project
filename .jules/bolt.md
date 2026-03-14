## 2024-03-14 - Global ML Model Loading in Flask

**Learning:** Loading large Machine Learning models (like `.sav` files via `joblib.load`) on every request within a Flask view function (e.g., `/predict`) creates a massive I/O and processing bottleneck, dramatically increasing latency. My benchmark showed 100 requests dropped from 0.59s to 0.11s by moving this out of the request context.

**Action:** Always load heavy dependencies (like ML models or static reference data) globally at application startup instead of inside route handlers. To handle testing or missing files safely, wrap the global load in a `try...except` block and implement fallback logic inside the route handler to ensure the application still boots and returns a graceful error or mock response when models are absent.
