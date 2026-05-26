## 2024-05-24 - Flask Debug Mode Enabled in Production
**Vulnerability:** The Flask application had `debug=True` enabled in `app.run()`.
**Learning:** Running Flask with debug mode enabled allows remote code execution (RCE) via the interactive Werkzeug debugger and exposes sensitive internal data if accessed remotely.
**Prevention:** Always ensure `debug=False` is set before deploying, and manage environment-specific configurations properly.