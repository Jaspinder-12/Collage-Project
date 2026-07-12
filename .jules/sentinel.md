## 2024-05-24 - Unhandled Form Data Leading to 500 Errors
**Vulnerability:** Flask application lacked input validation and error handling for `request.form` parsing, leading to unhandled `ValueError` or `KeyError` exceptions and 500 Internal Server Errors when invalid or missing data was submitted.
**Learning:** Raw input parsing must always be protected. Flask's default behavior exposes unhandled exceptions, which can leak internal application state and provide a poor user experience.
**Prevention:** Always wrap form data extraction and type casting in `try...except` blocks and return appropriate 400 Bad Request responses (rendering a template with an error message) instead of failing catastrophically.
