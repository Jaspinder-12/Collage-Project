## 2024-10-25 - Flask Debug Mode RCE Vulnerability
**Vulnerability:** Flask application was configured to run with `debug=True` in production.
**Learning:** Leaving debug mode enabled exposes the Werkzeug interactive debugger, which allows execution of arbitrary Python code from the browser, leading to a critical Remote Code Execution (RCE) vulnerability and leakage of sensitive stack traces.
**Prevention:** Always ensure `app.run()` is configured with `debug=False` or omit the debug parameter before deploying a Flask application to production.
