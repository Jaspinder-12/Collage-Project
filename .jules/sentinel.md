## 2024-05-24 - DoS and Information Leakage via Unhandled Exceptions and Debug Mode

**Vulnerability:**
The Flask application lacked proper input validation for the `/predict` POST route, leading to potential Denial of Service (DoS) and application crashes when unexpected input formats were submitted (e.g., non-numeric data or missing keys). Additionally, the Flask app was explicitly set to run with `debug=True` in production, which leaks sensitive internal stack traces and environment details to attackers if an error occurs.

**Learning:**
Relying on implicit type conversion without explicit `try...except` handling for form data submitted by users is a common vector for application instability. Furthermore, debug mode in Flask must always be disabled (`debug=False`) when deploying outside of a local development environment.

**Prevention:**
Always encapsulate input parsing and type casting in strict exception handling blocks. Catch specific exceptions like `KeyError`, `ValueError`, and `TypeError`, and return safe, generalized 400 Bad Request responses. Ensure production deployments use production-ready web servers (like Gunicorn) instead of the built-in Flask development server, and never hardcode `debug=True`.
