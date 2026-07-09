## 2024-05-24 - RCE via Werkzeug Debugger
**Vulnerability:** Flask application configured to run with `debug=True` in production.
**Learning:** Leaving debug mode enabled exposes the interactive Werkzeug debugger, which allows remote execution of arbitrary Python code (RCE).
**Prevention:** Always ensure `debug=False` when calling `app.run()` or setting environment variables in production.
