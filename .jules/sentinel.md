## 2024-05-24 - Unhandled Input Exceptions in Flask
**Vulnerability:** User input from `request.form` was directly cast to `float` without error handling, leading to 500 Internal Server Errors and potential stack trace exposure.
**Learning:** Flask's `request.form` throws `KeyError` for missing fields, and type casting throws `ValueError` for invalid types. Without `try...except`, this crashes the route handler.
**Prevention:** Always wrap direct user input access and type casting in a `try...except` block and return a 400 Bad Request for client errors.
