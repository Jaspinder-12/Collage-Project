## 2024-05-24 - Flask Debug Mode and Input Validation
**Vulnerability:** The application was running with `debug=True` in production, exposing the Werkzeug interactive debugger, and lacked input validation causing 500 Internal Server Errors.
**Learning:** Hardcoded debug modes and unhandled input exceptions can leak sensitive internal state and stack traces to attackers.
**Prevention:** Always ensure `debug=False` in production environments and implement robust input validation/error handling for user data.
