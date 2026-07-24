## 2024-07-24 - Unhandled Web Form Inputs
**Vulnerability:** Unhandled ValueError and KeyError exceptions in form parsing can lead to 500 Internal Server Errors and expose sensitive stack traces.
**Learning:** User input was directly cast to float without validation or error handling, assuming perfect input.
**Prevention:** Always wrap web form data access and casting in try...except blocks and return safe, generic error messages.
