## 2024-06-24 - Flask Debug Mode and Unhandled Input
**Vulnerability:** Flask running in debug mode (`debug=True`) which exposes the Werkzeug interactive debugger, and missing input validation causing 500 Internal Server Errors.
**Learning:** Default configurations and lack of input validation can easily expose internal stack traces to users.
**Prevention:** Ensure `debug=False` in production and wrap direct user input type casting in `try...except` blocks.
