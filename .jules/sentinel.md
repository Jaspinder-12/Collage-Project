## 2024-06-16 - Flask Debug Mode & Input Validation Vulnerabilities
**Vulnerability:** The Flask application was running with `debug=True` in production and lacked input validation on form data, potentially exposing the Werkzeug interactive debugger and stack traces.
**Learning:** Default configuration for Flask applications leaves them vulnerable to Remote Code Execution (via debug console) and Information Leakage (via unhandled exceptions causing 500 Server Errors).
**Prevention:** Always ensure `debug=False` is set for deployment and defensively wrap user input casting (e.g., `float()`) with `try...except (ValueError, KeyError)` blocks to fail securely with 400 Bad Request.
