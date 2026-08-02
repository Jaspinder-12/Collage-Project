## 2024-10-25 - Flask Debug Mode RCE Vulnerability
**Vulnerability:** Flask application was configured to run with `debug=True` in production.
**Learning:** Leaving debug mode enabled exposes the Werkzeug interactive debugger, which allows execution of arbitrary Python code from the browser, leading to a critical Remote Code Execution (RCE) vulnerability and leakage of sensitive stack traces.
**Prevention:** Always ensure `app.run()` is configured with `debug=False` or omit the debug parameter before deploying a Flask application to production.

## 2024-07-18 - Unhandled exceptions in form parsing
**Vulnerability:** User form input was directly cast to float without error handling, which would cause a 500 Internal Server Error and leak stack traces upon missing or malformed data.
**Learning:** Raw input extraction must always be wrapped in defensive try-except blocks (e.g. ValueError, KeyError) before further processing.
**Prevention:** Always use try-except blocks when handling user input and return a generic error message (400 Bad Request) instead of exposing application internals.
