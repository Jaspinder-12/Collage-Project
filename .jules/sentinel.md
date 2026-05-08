## 2024-05-08 - Fixed Production Debug Mode
**Vulnerability:** Flask application was running with debug=True in production, which exposes interactive stack traces and potential Remote Code Execution (RCE) via the Werkzeug debugger.
**Learning:** Default project templates or local testing configurations are often checked into version control without being disabled for production.
**Prevention:** Always ensure debug=False for Flask apps, and use environment variables (FLASK_ENV=production) instead of hardcoded booleans.
