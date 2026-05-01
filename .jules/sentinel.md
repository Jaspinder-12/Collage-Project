## 2024-05-01 - Disable Werkzeug Debug Mode
**Vulnerability:** Werkzeug interactive debugger enabled in production (debug=True).
**Learning:** Exposing the Werkzeug debugger allows arbitrary code execution (RCE) on the server.
**Prevention:** Always ensure debug=False in app.run() for production environments.
