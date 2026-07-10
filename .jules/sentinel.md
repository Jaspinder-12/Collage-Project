## 2024-07-10 - Unhandled Exceptions and Exposed Debugger
**Vulnerability:** The application was running with `debug=True` which exposes the Werkzeug interactive debugger and internal stack traces, and lacked input validation allowing unhandled exceptions (500 errors).
**Learning:** Leaving `debug=True` in production and trusting user input implicitly exposes critical application internals and allows for denial of service or remote code execution.
**Prevention:** Always run Flask with `debug=False` in production and validate/handle all inputs from `request.form` using a `try...except` block returning a 400 Bad Request.
