## 2024-06-03 - Flask Debug Mode & Unhandled Exceptions
**Vulnerability:** The application was running with `debug=True` in production and lacked proper error handling on the prediction endpoint.
**Learning:** `debug=True` enables the interactive Werkzeug debugger which can expose sensitive application details or allow remote code execution if an unhandled exception occurs. Missing error handling allows standard exceptions to propagate up, potentially leaking stack traces.
**Prevention:** Ensure `debug=False` for production deployments. Always wrap user-facing inputs and subsequent processing logic in `try...except` blocks and log errors securely server-side while returning generic error messages to the client.
