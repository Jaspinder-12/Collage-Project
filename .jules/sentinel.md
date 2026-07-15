## 2024-07-15 - Unhandled Form Exceptions and Debug Mode Enabled
**Vulnerability:** Flask application deployed with `debug=True` and unhandled form data extraction.
**Learning:** `debug=True` in a production environment exposes the Werkzeug interactive debugger and internal stack traces, posing a significant RCE and information disclosure risk. Furthermore, failing to handle `KeyError` or `ValueError` during `request.form` extraction can lead to unhandled 500 Internal Server Errors that may also expose stack traces when debug mode is enabled.
**Prevention:** Always deploy Flask applications with `debug=False` and wrap form data extraction in `try...except` blocks, returning secure, generic error messages to the user without exposing internal application logic.
