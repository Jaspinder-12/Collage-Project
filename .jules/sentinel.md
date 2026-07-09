## 2024-07-06 - Unhandled Exceptions Exposing Stack Traces
**Vulnerability:** Flask application lacked input validation (ValueError/KeyError from casting request.form directly to float) while running with `debug=True`, which exposes Werkzeug's interactive debugger and internal stack traces to users.
**Learning:** In Flask apps, unhandled exceptions combined with debug mode can lead to severe information disclosure. The codebase assumes all POST data is perfectly formed.
**Prevention:** Always wrap direct request.form access and type casting in `try...except` blocks to handle errors gracefully and ensure `debug=False` in production environments.
