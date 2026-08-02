## 2024-10-25 - Flask Debug Mode RCE Vulnerability
**Vulnerability:** Flask application was configured to run with `debug=True` in production.
**Learning:** Leaving debug mode enabled exposes the Werkzeug interactive debugger, which allows execution of arbitrary Python code from the browser, leading to a critical Remote Code Execution (RCE) vulnerability and leakage of sensitive stack traces.
**Prevention:** Always ensure `app.run()` is configured with `debug=False` or omit the debug parameter before deploying a Flask application to production.

## 2024-05-20 - Unhandled Form Input Exceptions
**Vulnerability:** Missing error handling on form inputs leading to 500 Internal Server Error.
**Learning:** In Flask apps, failing to catch KeyErrors and ValueErrors when parsing request.form exposes the app to unhandled exceptions which can leak stack traces in debug mode or crash the process.
**Prevention:** Always wrap form input extraction and type casting in try...except (ValueError, KeyError) blocks to fail securely.
