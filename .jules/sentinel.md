## 2024-05-24 - Unhandled Input Exceptions and Debug Mode Exposure
**Vulnerability:** The Flask application lacked input validation on the `/predict` route, allowing unhandled exceptions (ValueError, KeyError) to trigger 500 errors. Furthermore, the application had `debug=True` enabled in `app.run()`.
**Learning:** Combining unhandled exceptions with `debug=True` in production can expose the Werkzeug interactive debugger and internal stack traces, leading to critical remote code execution (RCE) or information disclosure risks.
**Prevention:** Always validate and handle expected input errors explicitly (e.g., returning a 400 Bad Request) and ensure `debug=False` is set before deploying Flask applications to prevent exposing the interactive debugger.
