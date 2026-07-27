## 2024-05-18 - Flask Debug Mode Exposed
**Vulnerability:** Flask application was configured to run with `debug=True` in production (app.run).
**Learning:** Developers often leave debug mode enabled for easier local testing, but this exposes the Werkzeug debugger console and stack traces in production, leading to potential Remote Code Execution (RCE) and sensitive data leakage.
**Prevention:** Always default to `debug=False` in code and use environment variables exclusively for local development environments.
