## 2024-05-15 - Disable Flask debug mode and secure error handling
**Vulnerability:** The Flask app was running with `debug=True` in production and had no try/except block for form data parsing. This could leak sensitive application state, stack traces, and local filesystem structures.
**Learning:** Default templates or unhandled exceptions in a web framework configured for debugging will expose internal configurations to attackers when they provide unexpected input formats.
**Prevention:** Always deploy with `debug=False`, implement explicit error handling that returns plain generic error responses, and remove hardcoded paths.
