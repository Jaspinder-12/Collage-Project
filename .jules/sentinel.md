## 2024-05-18 - Fix DoS risk and Information Leakage in `app.py`
**Vulnerability:** The Flask application had two critical security vulnerabilities:
1.  **Information Leakage:** `app.run(debug=True)` was active in production, potentially exposing sensitive stack traces and source code to users on error.
2.  **Denial of Service (DoS):** The `/predict` endpoint directly casted `request.form` inputs to `float` without error handling. Sending missing keys, non-numeric strings, or incorrect data types caused a `ValueError`, `KeyError`, or `TypeError`, resulting in an unhandled 500 Internal Server Error.

**Learning:** When inputs are read from an HTTP form, they should never be blindly cast without wrapping them in an exception handler, as this creates a trivial DoS vector and leads to poorly handled server errors. The default configuration of Flask apps often leaves `debug=True`, which must be explicitly removed before deploying.

**Prevention:**
- Always ensure `debug=False` (or remove the `debug=True` parameter entirely) in the main entry point for Flask apps.
- Validate and wrap all external input parsing in a `try...except` block, specifically catching `ValueError`, `KeyError`, and `TypeError` when dealing with numeric conversions.
- Return a safe `400 Bad Request` response instead of allowing the application to crash with a `500 Internal Server Error`.
