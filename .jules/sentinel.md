## 2024-05-24 - Input Validation and Information Leakage Prevention
**Vulnerability:** Unhandled exceptions in the `/predict` route when parsing form inputs could lead to 500 Internal Server Errors (potential DoS risk). Additionally, `debug=True` in `app.run()` risks exposing sensitive stack traces in production.
**Learning:** Robust input validation using `try...except` and returning explicit `400 Bad Request` prevents silent server errors. Disabling debug mode is a fundamental security practice.
**Prevention:** Always validate and safely cast incoming form data. Ensure production environments use `debug=False` or dedicated WSGI servers.
