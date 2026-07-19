## 2024-07-19 - Unhandled Form Data Casting
**Vulnerability:** Missing exception handling when extracting and casting web form inputs in Flask.
**Learning:** Hard-casting `request.form` variables to floats directly without try-except blocks can cause 500 Internal Server Errors on invalid/missing input, leaking sensitive stack traces and risking DoS.
**Prevention:** Always wrap web form data extraction and casting in `try...except (ValueError, KeyError)` blocks to handle malformed input securely.
