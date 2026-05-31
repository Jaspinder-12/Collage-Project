## 2024-05-31 - Disable Werkzeug Debugger in Production
**Vulnerability:** Flask application running with `debug=True` in a production-like environment.
**Learning:** Leaving the Flask debugger enabled exposes a highly interactive console that can execute arbitrary Python code, leading to Remote Code Execution (RCE) and sensitive data leakage.
**Prevention:** Always ensure `app.run(debug=False)` is used when deploying applications, or use environment variables to explicitly control debug mode so it defaults to off.
