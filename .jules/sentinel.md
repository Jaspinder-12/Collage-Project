## 2024-05-20 - Unhandled Inputs & Debug Mode Expose Application Details

**Vulnerability:** The application originally had `debug=True` enabled in production, and its route handlers did not catch exceptions like `KeyError` or `ValueError` when reading missing or improperly formatted form inputs.

**Learning:** When `debug=True` is enabled alongside unhandled exceptions in route definitions, an attacker can intentionally craft bad requests to crash the endpoint, exposing internal stack traces, configuration, and environment details. This is a DoS vector combined with information disclosure.

**Prevention:** Ensure `debug=False` in production code. Always wrap direct form extractions (and parsing logic) in `try...except` blocks that catch expected types (like `KeyError`, `ValueError`, `TypeError`) and return a generic 400 Bad Request instead of allowing a 500 internal server error.
