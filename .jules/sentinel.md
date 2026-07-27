## 2024-04-27 - Disable Flask Debug Mode
**Vulnerability:** Flask development server was configured with `debug=True` in production code.
**Learning:** Leaving `debug=True` in `app.run()` exposes the Werkzeug interactive debugger, which can allow arbitrary Python code execution if accessed by malicious users.
**Prevention:** Always ensure `debug=False` when deploying Flask applications or disable the interactive debugger completely for production environments.
