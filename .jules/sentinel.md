## 2024-06-14 - Unhandled Exceptions and Stack Trace Leaks
**Vulnerability:** Unhandled type casting exceptions and active debug mode exposed stack traces and internal application logic.
**Learning:** Flask routes directly casting `request.form` values without a try-catch will cause a 500 Internal Server Error when missing or malformed data is provided. Active debug mode leaked this information to users.
**Prevention:** Always wrap direct user input type casting in `try-except` blocks and return a 400 Bad Request. Ensure `debug=False` in production.
