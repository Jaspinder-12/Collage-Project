## 2024-07-02 - Unhandled Exception Data Leakage and Debug Mode in Flask
**Vulnerability:** Missing form data validation causing unhandled exceptions, and Flask `debug=True` exposed in production.
**Learning:** Default Flask `app.run()` with `debug=True` is dangerous and exposes Werkzeug debugger which leads to RCE. Direct dict lookups on `request.form` without validation lead to 500 errors and information disclosure on bad input.
**Prevention:** Always default to `debug=False` for Flask applications. Wrap all input extraction in a `try/except` to gracefully return 400 Bad Request, avoiding unhandled stack traces.
