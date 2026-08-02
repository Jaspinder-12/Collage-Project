## 2024-10-25 - Flask Debug Mode RCE Vulnerability
**Vulnerability:** Flask application was configured to run with `debug=True` in production.
**Learning:** Leaving debug mode enabled exposes the Werkzeug interactive debugger, which allows execution of arbitrary Python code from the browser, leading to a critical Remote Code Execution (RCE) vulnerability and leakage of sensitive stack traces.
**Prevention:** Always ensure `app.run()` is configured with `debug=False` or omit the debug parameter before deploying a Flask application to production.

## 2024-05-18 - Prevent Unhandled Form Exceptions
**Vulnerability:** The Flask app had unhandled form inputs in the `/predict` route (leading to 500 errors and leaking internal stack traces when values were missing or invalid).
**Learning:** Developers often assume users will only submit valid form data via perfectly functioning frontends, ignoring direct POST requests or manipulation.
**Prevention:** Wrap all `request.form` extractions and type-castings in `try...except (ValueError, KeyError)` blocks to gracefully render HTML error messages.
