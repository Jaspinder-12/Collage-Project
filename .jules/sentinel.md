## 2024-06-18 - Exposed Werkzeug Debugger
**Vulnerability:** Flask application deployed with `debug=True` exposing the Werkzeug interactive debugger and internal stack traces.
**Learning:** Deploying an application with debug mode enabled poses a critical security risk as it allows arbitrary code execution and leaks sensitive application state.
**Prevention:** Always ensure `debug=False` or completely omit the `debug` parameter in production environments. Use environment variables to control configuration in different deployments.
