## 2024-06-22 - Debug Mode and Missing Input Validation
**Vulnerability:** Flask application running with `debug=True` and unhandled form inputs exposing 500 internal server errors.
**Learning:** Debug mode exposes the Werkzeug interactive debugger and internal stack traces, and lack of input validation can cause application crashes or expose internals via exceptions.
**Prevention:** Always ensure `debug=False` in production and validate/handle form inputs using try-except blocks or validation libraries.
