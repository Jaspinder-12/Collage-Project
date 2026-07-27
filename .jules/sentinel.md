## 2024-04-19 - 🛡️ Sentinel: Fix Werkzeug Debugger Exposure
**Vulnerability:** Flask application running with `debug=True` in production-like entry points.
**Learning:** Hardcoding `debug=True` in `app.run()` exposes the Werkzeug interactive debugger, leading to potential Remote Code Execution (RCE) if exceptions are triggered (e.g., via malformed form inputs).
**Prevention:** Always set `debug=False` or rely on environment variables (like `FLASK_DEBUG`) to control debug mode, keeping it disabled by default in code.
