## 2024-06-12 - Missing Input Validation
**Vulnerability:** User input from request.form was directly cast to float without validation, leading to unhandled ValueError or KeyError exceptions.
**Learning:** Direct type casting of user input without exception handling can cause 500 Internal Server Errors and potentially expose stack traces.
**Prevention:** Always wrap direct user input type casting in try-except blocks to handle invalid or missing data and return a secure 400 Bad Request response.
