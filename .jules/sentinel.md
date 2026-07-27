## 2024-05-01 - Fix Information Leakage and DoS Vectors via Unhandled Exceptions and Absolute Paths
**Vulnerability:**
1. The Flask app had `debug=True` in production code.
2. The endpoint `/predict` relied on unhandled input validations to implicitly fail (with Python exceptions), likely generating 500 error HTTP responses that exposed stack traces.
3. Model paths were hardcoded as absolute local windows paths (`D:\projects\...`).
**Learning:** Hardcoded absolute paths and `debug=True` lead to disclosing the server directory structure and internal logic stack traces on failure. Implicit typecasting without exception handling in endpoints further exacerbates this because it provides a reliable vector to force application exceptions simply by omitting inputs or submitting strings instead of expected floats.
**Prevention:**
1. Always set `debug=False` for Flask apps in production unless actively developing locally in an ephemeral environment.
2. All request parsing (e.g. `request.form[...]` or float conversions) MUST be wrapped in a `try...except` block catching exceptions like `KeyError` or `ValueError` to return graceful, sanitized errors (e.g. 400 Bad Request) instead of exposing unhandled exceptions.
3. Only use relative or cross-platform safe paths relying on `os.path.join(os.path.dirname(__file__), ...)` for loading local assets like models to hide the execution environment directory structure.
