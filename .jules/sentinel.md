
## 2024-05-24 - Input Validation and Production Server Settings
**Vulnerability:** Unhandled inputs causing DoS/stack trace leaks and enabled debug mode in production.
**Learning:** The application lacked input validation and a try-except block, allowing missing or non-numerical values to throw 500 errors and leak stack traces when debug mode was enabled.
**Prevention:** Always validate, catch missing inputs safely by returning 400 Bad Request instead of allowing 500 server errors, and ensure `debug=False` for Flask apps in production environments.
