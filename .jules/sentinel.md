## 2026-04-25 - Prevent Werkzeug Debugger Exposure
**Vulnerability:** The Flask application was configured with `debug=True`, which exposes the Werkzeug interactive debugger.
**Learning:** Exposing the interactive debugger allows arbitrary Python code execution in a production environment.
**Prevention:** Always ensure `debug=False` in `app.run()` for production environments.
