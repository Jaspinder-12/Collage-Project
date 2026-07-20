## 2024-07-20 - Missing Input Validation in Flask Forms
**Vulnerability:** Unhandled exceptions (`ValueError`, `KeyError`) during web form data parsing in `request.form`.
**Learning:** Raw parsing and casting of user inputs without `try...except` blocks in Flask causes 500 Internal Server Errors and leaks sensitive stack traces when `debug=True`.
**Prevention:** Always wrap form data extraction and casting in `try...except (ValueError, KeyError)` blocks to fail securely and return a safe error page.
