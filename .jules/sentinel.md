## 2024-07-17 - Unhandled Form Input Exceptions
**Vulnerability:** Flask route lacked input validation for `request.form` keys and type casting, exposing sensitive internal stack traces via 500 Internal Server Errors on malformed requests.
**Learning:** Developers often assume all form submissions will perfectly match expected HTML structure, ignoring malicious or malformed raw POST requests.
**Prevention:** Always wrap form input extraction and casting in `try...except (ValueError, KeyError)` blocks and return safe, generic error responses (e.g., 400 Bad Request) instead of failing ungracefully.
