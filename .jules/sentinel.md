## 2024-05-24 - Werkzeug Debugger RCE
**Vulnerability:** Flask application was configured with `debug=True` in production, exposing the interactive Werkzeug debugger.
**Learning:** Leaving the interactive Werkzeug debugger enabled in production environments allows unauthenticated Remote Code Execution (RCE) and leaks sensitive application state/code.
**Prevention:** Always ensure `app.run(debug=False)` or omit the `debug` parameter entirely when running Flask applications outside of local development.
