## 2024-06-20 - Exposed Werkzeug Debugger and Unhandled Exceptions
**Vulnerability:** The Flask application was configured with `debug=True`, exposing the Werkzeug interactive debugger. Additionally, missing input validation on `request.form` allowed unhandled exceptions to crash the server with 500 Internal Server Errors.
**Learning:** Developers often leave debug mode enabled and assume happy-path user input, which inadvertently exposes internal stack traces and server state to attackers.
**Prevention:** Ensure `debug=False` in production and always wrap user input parsing in `try...except` blocks to handle invalid data gracefully with 400 Bad Request responses.
