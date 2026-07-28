## 2024-07-28 - Disable Flask Debug Mode in Production
**Vulnerability:** Flask application configured with `debug=True` in production.
**Learning:** This exposes the interactive Werkzeug debugger, leading to Remote Code Execution (RCE) and data leakage on unhandled exceptions.
**Prevention:** Always ensure `app.run()` is configured with `debug=False` before deployment.
