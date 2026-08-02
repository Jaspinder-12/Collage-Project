## 2024-10-25 - Flask Debug Mode RCE Vulnerability
**Vulnerability:** Flask application was configured to run with `debug=True` in production.
**Learning:** Leaving debug mode enabled exposes the Werkzeug interactive debugger, which allows execution of arbitrary Python code from the browser, leading to a critical Remote Code Execution (RCE) vulnerability and leakage of sensitive stack traces.
**Prevention:** Always ensure `app.run()` is configured with `debug=False` or omit the debug parameter before deploying a Flask application to production.

## 2024-07-17 - Unhandled Form Input Exceptions
**Vulnerability:** Flask route lacked input validation for `request.form` keys and type casting, exposing sensitive internal stack traces via 500 Internal Server Errors on malformed requests.
**Learning:** Developers often assume all form submissions will perfectly match expected HTML structure, ignoring malicious or malformed raw POST requests.
**Prevention:** Always wrap form input extraction and casting in `try...except (ValueError, KeyError)` blocks and return safe, generic error responses (e.g., 400 Bad Request) instead of failing ungracefully.
