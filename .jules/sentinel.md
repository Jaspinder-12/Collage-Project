## 2024-10-25 - Flask Debug Mode RCE Vulnerability
**Vulnerability:** Flask application was configured to run with `debug=True` in production.
**Learning:** Leaving debug mode enabled exposes the Werkzeug interactive debugger, which allows execution of arbitrary Python code from the browser, leading to a critical Remote Code Execution (RCE) vulnerability and leakage of sensitive stack traces.
**Prevention:** Always ensure `app.run()` is configured with `debug=False` or omit the debug parameter before deploying a Flask application to production.

## 2024-07-25 - Prevent Unhandled Exception Leakage in Web Forms
**Vulnerability:** Input data from `request.form` in Flask were being accessed and directly cast to floats without any try-except block, posing a risk of 500 Internal Server Errors that can leak sensitive stack traces.
**Learning:** Raw form values from untrusted sources should never be unconditionally cast or accessed by key in a production app without proper validation and error handling blocks.
**Prevention:** Always wrap dictionary key accesses on untrusted objects (like request.form) and type coercions in `try...except (ValueError, KeyError)` blocks to fail securely.
