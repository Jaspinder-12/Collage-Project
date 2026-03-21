## 2025-02-28 - Information Exposure through Unhandled Exceptions in Development Mode
**Vulnerability:** Missing input validation in `app.py` caused unhandled `ValueError` or `KeyError` when form fields were missing or invalid. Compounding this, `app.run(debug=True)` caused the application to return detailed stack traces (500 Internal Server Error) on crashes, which risks leaking internal infrastructure, directory structure, and environment variables.
**Learning:** Never enable `debug=True` in production code. Always validate form input to fail securely (return a 400 Bad Request instead of allowing 500 crashes).
**Prevention:** Wrap user input processing in a `try...except` block, sanitize or validate data, and ensure debug mode is disabled (`debug=False`).
