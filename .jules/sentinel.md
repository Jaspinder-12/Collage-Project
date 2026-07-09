## 2024-05-23 - Missing Input Validation in Flask Routes
**Vulnerability:** Direct type casting (e.g., `float()`) on `request.form` values without error handling.
**Learning:** This leads to unhandled exceptions (like `ValueError` or `KeyError`), causing 500 internal server errors and potentially leaking stack traces.
**Prevention:** Encapsulate input parsing logic within `try...except` blocks and return a safe HTTP 400 response.

## 2024-05-23 - Flask Debug Mode Enabled in Production
**Vulnerability:** `app.run(debug=True)` was used in the application.
**Learning:** Running Flask in debug mode can lead to remote code execution (RCE) vulnerabilities and sensitive data leakage via the interactive Werkzeug debugger.
**Prevention:** Always ensure `app.run()` is configured with `debug=False` for any production-ready or internet-facing application.
