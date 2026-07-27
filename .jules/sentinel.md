## 2024-05-20 - Fix Critical RCE and Unhandled Exceptions in Flask App
**Vulnerability:** Flask application running in debug mode (RCE risk) and missing input validation causing 500 errors.
**Learning:** Hardcoded `debug=True` exposes the Werkzeug interactive debugger, and direct type casting without `try...except` exposes stack traces.
**Prevention:** Always run Flask with `debug=False` in production-like environments and wrap external input processing in `try...except (ValueError, KeyError)` returning a 400 response.