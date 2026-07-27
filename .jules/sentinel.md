## 2024-07-27 - Flask Debug Mode RCE Vulnerability
**Vulnerability:** The Flask application was running with `debug=True` in `app.py`.
**Learning:** This exposes the interactive Werkzeug debugger in production environments, creating a critical Remote Code Execution (RCE) vulnerability and leaking sensitive stack traces on 500 errors.
**Prevention:** Always ensure `app.run()` is configured with `debug=False` before deployment and use environment variables for configuring debug modes locally.
