## 2024-07-29 - Fixed RCE and Stack Trace Leak
**Vulnerability:** The Werkzeug debugger was enabled in production via `debug=True`, and unhandled user input exceptions leaked sensitive stack traces.
**Learning:** Using `debug=True` in production exposes a critical Remote Code Execution (RCE) vulnerability and leaks sensitive information on 500 errors.
**Prevention:** Always deploy Flask applications with `debug=False` and validate/sanitize user inputs within a `try-except` block to prevent unhandled exceptions.
