## 2024-05-24 - Debug Mode and Information Leakage
**Vulnerability:** Flask application deployed with `debug=True` and missing input validation.
**Learning:** Hardcoding `debug=True` in `app.run()` allows arbitrary code execution via Werkzeug console if exposed, and missing exception handling on input parsing leads to unhandled 500 errors that leak stack traces and environment details.
**Prevention:** Always set `debug=False` for production deployments and wrap external input processing/file loading in robust try-except blocks that return safe, generic HTTP error codes (e.g., 400 or 500).
