## 2024-04-28 - Disable Flask Debug Mode in Production
**Vulnerability:** Flask application running with `debug=True` exposes the Werkzeug interactive debugger, which can lead to Remote Code Execution (RCE) if publicly accessible.
**Learning:** Hardcoded `debug=True` in production code is a critical risk.
**Prevention:** Always ensure `debug=False` in production or control it strictly via environment variables.
