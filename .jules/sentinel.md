## 2024-06-27 - Disable Werkzeug Debugger and Secure Inputs
**Vulnerability:** Werkzeug interactive debugger exposed and unhandled input casting causing 500 Internal Server Errors.
**Learning:** Default Flask applications may start with `debug=True`, exposing stack traces and remote code execution vulnerabilities in production. Missing try-catch around form inputs causes uncontrolled errors.
**Prevention:** Always set `debug=False` in production and wrap form data parsing in `try...except` to return 400 Bad Request.
