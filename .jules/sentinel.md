## 2024-04-10 - Prevent Sensitive Information Leakage

**Vulnerability:** Flask's `app.run(debug=True)` was enabled in production code, and the `/predict` POST endpoint did not handle `KeyError`, `ValueError`, and `TypeError` when form values were missing or had incorrect types. This caused raw unhandled exceptions and full stack traces to be returned to the client, exposing internal server state and file paths.

**Learning:** Leaving debug mode on and not gracefully handling expected conversion errors creates a critical information disclosure vector, especially in web endpoints parsing unstructured user input.

**Prevention:** Ensure `app.run()` explicitly sets `debug=False` for production deployments. Always wrap user input parsing and casting (like `float(request.form['x'])`) in `try...except` blocks and return generic, plain text HTTP 400 Bad Request errors to avoid leaking stack traces.
