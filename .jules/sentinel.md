## 2024-06-23 - Disable Flask Debug Mode and Handle Input Errors
**Vulnerability:** Flask debug mode was enabled in production (`app.run(debug=True)`) and user input from `request.form` was cast to float without error handling, exposing internal stack traces on 500 errors.
**Learning:** Development settings like `debug=True` can inadvertently leak into production, and unhandled exceptions during input parsing lead to 500 Internal Server Errors which leak stack traces when debug is on.
**Prevention:** Always ensure `debug=False` for production deployments and wrap direct user input type casting in `try...except` blocks to fail securely with a 400 Bad Request.
