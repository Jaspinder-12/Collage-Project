## 2024-05-24 - Fix Information Exposure in Flask App
**Vulnerability:** Flask application was running with `debug=True` in production and missing input validation on form endpoints, which could leak stack traces and sensitive environment details upon bad input.
**Learning:** Default Flask configurations (debug mode) and unhandled type conversions (`float()`) on raw request data present immediate information disclosure risks.
**Prevention:** Always set `debug=False` for deployment and wrap route handlers in `try...except` blocks to catch expected input errors and prevent generic exceptions from bubbling up to the user.
