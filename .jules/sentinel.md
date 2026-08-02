## 2024-10-25 - Flask Debug Mode RCE Vulnerability
**Vulnerability:** Flask application was configured to run with `debug=True` in production.
**Learning:** Leaving debug mode enabled exposes the Werkzeug interactive debugger, which allows execution of arbitrary Python code from the browser, leading to a critical Remote Code Execution (RCE) vulnerability and leakage of sensitive stack traces.
**Prevention:** Always ensure `app.run()` is configured with `debug=False` or omit the debug parameter before deploying a Flask application to production.

## 2024-07-26 - Prevent Stack Trace Exposure on Invalid Inputs
**Vulnerability:** User inputs from web forms were cast to floats without error handling, which would cause a `ValueError` or `KeyError`, leading to a 500 Internal Server Error that exposes sensitive stack traces.
**Learning:** Web applications must defensively handle all user inputs and fail securely to prevent leaking internal implementation details via stack traces.
**Prevention:** Always wrap user input extraction and casting in `try...except` blocks and return generic error pages or safe fallbacks.
