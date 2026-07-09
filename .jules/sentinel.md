## 2024-05-18 - Flask Debug Mode & Unhandled Exceptions
**Vulnerability:** Flask application exposed the Werkzeug interactive debugger (`debug=True`) and leaked stack traces on 500 Internal Server Errors due to unhandled exceptions during `float()` casting of user input.
**Learning:** Local development configurations (`debug=True`) and optimistic data parsing (`float(request.form[...])`) without error boundaries are common patterns that accidentally leak sensitive internal state into production.
**Prevention:** Always set `debug=False` for production-ready code and wrap user input parsing in `try...except` blocks that return a safe, generic 400 Bad Request message.
