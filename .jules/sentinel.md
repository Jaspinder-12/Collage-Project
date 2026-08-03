## 2024-10-25 - Flask Debug Mode RCE Vulnerability
**Vulnerability:** Flask application was configured to run with `debug=True` in production.
**Learning:** Leaving debug mode enabled exposes the Werkzeug interactive debugger, which allows execution of arbitrary Python code from the browser, leading to a critical Remote Code Execution (RCE) vulnerability and leakage of sensitive stack traces.
**Prevention:** Always ensure `app.run()` is configured with `debug=False` or omit the debug parameter before deploying a Flask application to production.
## 2025-02-09 - Missing Input Validation in Flask Route
**Vulnerability:** Unhandled KeyError and ValueError when extracting and casting form data in `request.form`.
**Learning:** Web forms can submit incomplete or maliciously formatted payloads. Relying on strict dict access (e.g., `request.form['key']`) and immediate float casting without error handling causes unhandled exceptions, resulting in 500 Internal Server Errors and potentially leaking sensitive stack traces.
**Prevention:** Always wrap form data extraction and type casting in a `try...except (ValueError, KeyError)` block to handle invalid inputs safely, returning a 400 Bad Request or re-rendering the input form with an error message.
