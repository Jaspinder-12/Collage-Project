## 2024-05-14 - Debug Mode Enabled in Production
**Vulnerability:** The Flask application was running with `debug=True` in production code.
**Learning:** Hardcoded configuration settings often leave critical features enabled, like the Flask Werkzeug debugger which can expose source code and stack traces to users.
**Prevention:** Avoid hardcoding `debug=True` in the production file. Always ensure settings like this are environment variables, and default them to `False`.