## 2025-01-01 - Fix Flask Werkzeug Debug Exposure and Input Validation
**Vulnerability:** Flask application was configured with `debug=True` in production code alongside unhandled type casting exceptions (`ValueError`, `KeyError`) on form inputs.
**Learning:** Exposing the Werkzeug interactive debugger allows potential remote code execution (RCE) and leaks sensitive stack traces when combined with unhandled exceptions.
**Prevention:** Always set `debug=False` in production setups and wrap all direct `request.form` type casts in `try...except` blocks returning 400 Bad Request to gracefully handle malformed inputs.
