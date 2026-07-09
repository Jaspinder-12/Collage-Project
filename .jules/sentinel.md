## 2024-05-30 - Disable Flask Debug Mode
**Vulnerability:** Flask development server was running with `debug=True` in the main entry point, which exposes the Werkzeug interactive debugger.
**Learning:** Hardcoded `debug=True` can easily leak into production environments, allowing Remote Code Execution (RCE) and sensitive data exposure.
**Prevention:** Always set `debug=False` or omit the parameter in production code, relying on environment variables (like `FLASK_DEBUG`) during local development instead.
