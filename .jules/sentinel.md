## 2024-05-21 - Flask Debug Mode RCE Vulnerability
**Vulnerability:** Flask application was configured with `debug=True` in `app.run()` and lacked input validation on `request.form`.
**Learning:** Running Flask with debug mode enabled can allow attackers to execute arbitrary code (RCE) via the interactive Werkzeug debugger if it's exposed. Lack of input validation leads to unhandled exceptions which can leak sensitive stack traces.
**Prevention:** Always ensure `debug=False` in production environments, and encapsulate input parsing in `try...except` blocks to return safe HTTP responses.
