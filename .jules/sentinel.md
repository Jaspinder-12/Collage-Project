## 2024-06-13 - Add Input Validation for Flask Route
**Vulnerability:** Unvalidated user inputs (`request.form` keys directly cast to `float`) can cause `ValueError` or `KeyError`, leading to an unhandled exception and potentially exposing stack traces.
**Learning:** External user inputs must always be validated and parsed within `try...except` blocks to fail gracefully and return standard HTTP error codes (e.g., 400 Bad Request) instead of throwing 500 Internal Server Errors.
**Prevention:** Always wrap type casting of user input in `try...except (ValueError, KeyError):` blocks and return appropriate 400-level HTTP responses.
