## 2024-05-25 - Flask Debug Mode Vulnerability
**Vulnerability:** Flask `app.run(debug=True)` was used in the application.
**Learning:** Leaving debug mode enabled in Flask exposes the interactive Werkzeug debugger, which allows arbitrary Python code execution (RCE) by anyone who can access the endpoint.
**Prevention:** Always ensure `app.run()` is configured with `debug=False` to prevent RCE vulnerabilities and sensitive data leakage.
