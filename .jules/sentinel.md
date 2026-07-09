## 2024-06-10 - Unvalidated Input Leading to 500 Errors
**Vulnerability:** The `/predict` endpoint directly casts user input from `request.form` to `float` without any prior validation.
**Learning:** Supplying missing or non-numeric input values triggers a `ValueError` or `KeyError`, which results in an unhandled 500 Internal Server Error, potentially exposing internal stack traces or causing application instability.
**Prevention:** Always encapsulate input parsing in a `try...except` block or use dedicated validation libraries to safely catch and handle invalid input, returning a sanitized HTTP 400 Bad Request to the user.
