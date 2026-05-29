## 2025-02-23 - Flask Werkzeug Debugger RCE Risk
**Vulnerability:** The Flask application was hardcoded to start with `debug=True` in production (`app.run(debug=True)`), which exposes the interactive Werkzeug debugger.
**Learning:** This exposes the application to Remote Code Execution (RCE) because the debugger allows anyone to execute arbitrary Python code.
**Prevention:** Ensure `debug=False` for any production deployments, or configure it via environment variables (e.g., `FLASK_DEBUG=0`) instead of hardcoding `True`.
