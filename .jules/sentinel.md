## 2024-06-17 - Unhandled Input Casting and Debug Mode Exposure
**Vulnerability:** The application was vulnerable to 500 Internal Server Errors due to unhandled ValueError/KeyError exceptions when casting `request.form` inputs to floats, which coupled with `app.run(debug=True)` could expose the Werkzeug interactive debugger and stack traces.
**Learning:** Hardcoded type casting on user input without validation and leaving debug mode enabled in production code creates a severe information leakage and potential RCE vector.
**Prevention:** Always wrap direct user input parsing in a `try...except` block returning a 400 Bad Request, and explicitly set `debug=False` for production deployments.
