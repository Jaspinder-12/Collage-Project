## 2024-10-25 - Flask Debug Mode RCE Vulnerability
**Vulnerability:** Flask application was configured to run with `debug=True` in production.
**Learning:** Leaving debug mode enabled exposes the Werkzeug interactive debugger, which allows execution of arbitrary Python code from the browser, leading to a critical Remote Code Execution (RCE) vulnerability and leakage of sensitive stack traces.
**Prevention:** Always ensure `app.run()` is configured with `debug=False` or omit the debug parameter before deploying a Flask application to production.

## 2024-07-20 - Missing Input Validation in Flask Forms
**Vulnerability:** Unhandled exceptions (`ValueError`, `KeyError`) during web form data parsing in `request.form`.
**Learning:** Raw parsing and casting of user inputs without `try...except` blocks in Flask causes 500 Internal Server Errors and leaks sensitive stack traces when `debug=True`.
**Prevention:** Always wrap form data extraction and casting in `try...except (ValueError, KeyError)` blocks to fail securely and return a safe error page.
