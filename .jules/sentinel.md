## 2024-06-30 - Prevent Werkzeug Debugger Exposure
**Vulnerability:** Flask application was configured to run with `debug=True` in production code.
**Learning:** Leaving `debug=True` active exposes the Werkzeug interactive debugger, which can lead to Remote Code Execution (RCE) and sensitive data leakage via stack traces on unhandled exceptions.
**Prevention:** Always ensure `debug=False` (or remove the flag entirely) before deploying or committing production Flask applications.
