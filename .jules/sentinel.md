## 2024-05-24 - Unhandled Input Exceptions and Exposed Stack Traces

**Vulnerability:** The Flask application extracted form inputs via `request.form` and immediately casted them to `float()` without error handling. When deployed with `debug=True`, submitting invalid inputs (or omitting fields) caused a `ValueError` or `KeyError`, crashing the endpoint with a 500 error and exposing sensitive backend stack traces to the user.

**Learning:** Missing input validation paired with development debugging tools enabled in production directly leads to Information Exposure (CWE-200). An attacker could leverage the stack trace details to learn about the underlying file paths, library versions, and system architecture.

**Prevention:** Always validate and safely parse user inputs by catching specific expected exceptions (`KeyError`, `ValueError`, `TypeError`). Return generic, non-informative client-error responses (e.g., 400 Bad Request) instead of failing ungracefully. Never deploy Flask applications with `app.run(debug=True)`.
