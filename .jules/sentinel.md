## 2024-05-14 - Fix Flask Debug Mode and Input Validation
**Vulnerability:** Flask application was running in debug mode (RCE risk) and lacked input validation for form data, which could lead to 500 errors and stack trace leakage.
**Learning:** Always disable debug mode in production and wrap type conversions from user input in try-except blocks to fail gracefully.
**Prevention:** Enforce `debug=False` for Flask app.run() and implement robust error handling for `request.form` extraction.