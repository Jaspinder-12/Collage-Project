## 2024-10-25 - Flask Debug Mode RCE Vulnerability
**Vulnerability:** Flask application was configured to run with `debug=True` in production.
**Learning:** Leaving debug mode enabled exposes the Werkzeug interactive debugger, which allows execution of arbitrary Python code from the browser, leading to a critical Remote Code Execution (RCE) vulnerability and leakage of sensitive stack traces.
**Prevention:** Always ensure `app.run()` is configured with `debug=False` or omit the debug parameter before deploying a Flask application to production.

## 2025-02-13 - Fix unhandled input exceptions in Flask app
**Vulnerability:** Unhandled ValueError and KeyError exceptions when parsing user input from `request.form`.
**Learning:** Without defensive try/except blocks around form data parsing and type casting, malicious or malformed input can cause 500 Internal Server Errors, potentially leaking stack traces or sensitive internal application state.
**Prevention:** Always wrap request form parsing and casting operations in appropriate `try...except (ValueError, KeyError)` blocks, and return generic error views or redirect to a safe page to fail securely.
