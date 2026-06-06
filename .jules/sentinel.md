## 2024-05-24 - Unhandled Exceptions and Debug Mode in Flask
**Vulnerability:** The Flask app ran with `debug=True` and lacked exception handling in the `/predict` route, potentially exposing internal stack traces and environment details to attackers via the Werkzeug debugger or unhandled 500 errors.
**Learning:** Default Flask configurations often prioritize developer convenience over security. Failing to catch input parsing errors directly leads to stack trace disclosure when inputs are malformed.
**Prevention:** Always set `debug=False` in production and wrap route handlers in `try...except` blocks that return generic error messages (e.g., 400 Bad Request) instead of raw exceptions.
