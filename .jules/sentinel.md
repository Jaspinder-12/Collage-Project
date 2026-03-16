## 2024-05-24 - [HIGH] Fix DoS risk and information disclosure in app
**Vulnerability:** Missing input validation in `/predict` route allowed unhandled exceptions (e.g. ValueError when parsing floats) causing 500 server errors, which could be abused for Denial of Service. Also, `debug=True` was enabled, which leaks internal stack traces to users on errors.
**Learning:** Always validate user inputs and fail securely with a 400 Bad Request instead of throwing unhandled 500 errors. Also, never run `app.run(debug=True)` in production environments to avoid information disclosure.
**Prevention:** Implement `try...except` blocks around type-casting input from `request.form` and return a safe error message. Ensure production server configurations do not run with `debug=True`.
