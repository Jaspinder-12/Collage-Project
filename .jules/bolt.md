## 2024-05-24 - [Optimize Model Loading]
**Learning:** Loading machine learning models globally instead of inside a request handler in a Flask app prevents major I/O bottlenecks and speeds up every single request.
**Action:** Always load models into memory during application initialization and wrap them in a `try...except FileNotFoundError` block for robust CI/CD and testing environments.
