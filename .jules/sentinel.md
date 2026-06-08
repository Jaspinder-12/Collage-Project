## 2024-06-08 - Prevent Information Leakage in Debug Mode
**Vulnerability:** The Flask application was running with `debug=True` and lacked input validation, meaning any invalid request would expose a full stack trace and potentially the interactive debugger to users.
**Learning:** Hardcoded `debug=True` in the main application file and missing `try-except` blocks around `request.form` parsing create a high risk of information disclosure.
**Prevention:** Always set `debug=False` (or use environment variables) in production-ready files and add generic exception handlers that return standardized error messages instead of leaking internal state.
