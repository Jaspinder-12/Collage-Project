## 2024-07-25 - Prevent Unhandled Exception Leakage in Web Forms
**Vulnerability:** Input data from `request.form` in Flask were being accessed and directly cast to floats without any try-except block, posing a risk of 500 Internal Server Errors that can leak sensitive stack traces.
**Learning:** Raw form values from untrusted sources should never be unconditionally cast or accessed by key in a production app without proper validation and error handling blocks.
**Prevention:** Always wrap dictionary key accesses on untrusted objects (like request.form) and type coercions in `try...except (ValueError, KeyError)` blocks to fail securely.
