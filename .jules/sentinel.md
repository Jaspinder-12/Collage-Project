## 2024-04-18 - Flask Debug Mode Enabled in Production

**Vulnerability:** The Flask application was configured with `app.run(debug=True)`. This enables the Werkzeug interactive debugger, which allows executing arbitrary code in the context of the application if an error occurs.
**Learning:** Development settings can easily leak into production if not properly managed or separated. Leaving debug mode on is a critical security risk as it exposes stack traces and a Python shell to potentially malicious users.
**Prevention:** Ensure `debug=False` is set in production. Use environment variables (e.g., `FLASK_DEBUG=1` for dev) instead of hardcoding `debug=True` in the `app.run()` configuration to prevent accidental deployment of debug mode.
