## 2024-07-07 - Flask Debug Mode & Unhandled Exceptions
**Vulnerability:** Debug mode was enabled in production and missing input validation allowed for 500 Internal Server Errors.
**Learning:** This exposes the Werkzeug interactive debugger and internal stack traces to users when errors occur.
**Prevention:** Always set debug=False in production and wrap request input parsing in try...except blocks.
