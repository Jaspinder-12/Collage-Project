## 2024-06-25 - Prevent Exposure of Internal Stack Traces and Unhandled Exceptions
**Vulnerability:** Werkzeug interactive debugger was exposed via `debug=True`, and missing input validation on form submissions allowed unhandled exceptions to cause 500 Internal Server Errors.
**Learning:** Default configuration and missing `try...except` blocks for direct input casting can lead to critical information leakage and denial of service.
**Prevention:** Always set `debug=False` in production code and use proper `try...except` blocks with appropriate HTTP error codes (e.g., 400) when validating user inputs.
