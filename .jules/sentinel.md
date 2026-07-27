## 2024-04-23 - Disable Werkzeug Debugger in Production
**Vulnerability:** The Flask application was configured with `debug=True` in `app.run()`, which exposes the Werkzeug interactive debugger. This allows remote code execution if deployed to production.
**Learning:** Development configurations (like `debug=True`) are often accidentally left in production deployment code, posing a critical security risk.
**Prevention:** Always ensure `debug=False` is set or omitted (defaults to False) in production environments, and use environment variables to toggle debug mode rather than hardcoding it.
