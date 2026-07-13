## 2024-07-13 - Disable Flask Debug Mode and Handle Input Errors
**Vulnerability:** Flask debug mode was enabled in production and missing input validation on form parsing could lead to unhandled exceptions.
**Learning:** Hardcoded `debug=True` exposes the Werkzeug interactive debugger which is a severe security risk. Additionally, directly casting `request.form` user input without `try...except` can cause 500 errors and stack traces.
**Prevention:** Always ensure `debug=False` for production Flask deployments and wrap input parsing in try-except blocks that return proper 400 error codes.
