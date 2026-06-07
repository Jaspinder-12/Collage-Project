## 2024-06-07 - Information Leakage via Debug Mode and Unhandled Exceptions
**Vulnerability:** The Flask application was running with `debug=True` in production and lacked input validation, which could leak stack traces and internal details on invalid inputs.
**Learning:** Leaving debug mode enabled and missing `try...except` blocks on direct type casting of request data creates unhandled exceptions that expose server internals.
**Prevention:** Always set `debug=False` for deployment and wrap external input processing in explicit `try...except` blocks to fail securely without exposing stack traces.
