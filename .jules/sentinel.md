## 2024-05-24 - DoS and Info Leakage in Flask App
**Vulnerability:** The Flask app was running with `debug=True`, exposing stack traces and potentially allowing RCE. Additionally, the `/predict` endpoint parsed inputs without error handling.
**Learning:** The lack of a `try...except (KeyError, ValueError, TypeError)` block meant invalid or missing form data would cause a 500 Internal Server Error instead of failing gracefully. Attackers could exploit this to perform a Denial of Service attack or to leak the internal state.
**Prevention:** Always set `debug=False` for production and ensure all user-supplied inputs are robustly validated with appropriate error handling that avoids revealing internal logic.
