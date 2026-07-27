## 2024-05-24 - Unhandled Exceptions Resulting in DoS
**Vulnerability:** The Flask `/predict` endpoint accepted user input via `request.form` and cast it directly to `float()`. If missing fields or non-numeric strings were provided, it caused unhandled `KeyError` or `ValueError` exceptions, leading to a 500 Internal Server Error.
**Learning:** This exposes the application to Denial of Service (DoS) attacks and potential stack trace exposure if an attacker intentionally submits invalid data.
**Prevention:** Wrap user input processing and type conversions in a `try...except` block, returning a specific client error (e.g., 400 Bad Request) instead of failing gracefully. Additionally, ensure `debug=False` in production `app.run()`.
