## 2024-05-20 - Unhandled Form Input Exceptions
**Vulnerability:** Missing error handling on form inputs leading to 500 Internal Server Error.
**Learning:** In Flask apps, failing to catch KeyErrors and ValueErrors when parsing request.form exposes the app to unhandled exceptions which can leak stack traces in debug mode or crash the process.
**Prevention:** Always wrap form input extraction and type casting in try...except (ValueError, KeyError) blocks to fail securely.
