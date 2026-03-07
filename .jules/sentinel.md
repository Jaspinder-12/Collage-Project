## 2024-05-24 - [CRITICAL] Fix debug mode and unhandled input validation
**Vulnerability:**
1. The Flask app was configured with `app.run(debug=True)`, which poses a critical security risk in production environments as it exposes stack traces and can potentially allow Remote Code Execution via the Werkzeug debugger.
2. The `/predict` endpoint did not handle missing or invalid user input. It directly converted values from `request.form` into `float`, leaving it vulnerable to `KeyError` or `ValueError`, resulting in a 500 Internal Server Error, which can leak server internals and cause a Denial of Service (DoS).

**Learning:**
1. Development settings like `debug=True` frequently get committed accidentally or overlooked during deployment.
2. Input validation and graceful error handling are critical on any endpoint that accepts user input, especially from forms, to prevent unexpected exceptions.

**Prevention:**
1. Never hardcode `debug=True` in production code. Use environment variables (e.g., `FLASK_DEBUG`) to control debug mode, and default to `False`.
2. Wrap user input parsing in a `try...except` block, specifically catching `KeyError`, `ValueError`, and `TypeError`, to securely return a generic 400 Bad Request instead of throwing an unhandled exception.