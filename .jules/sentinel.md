## 2024-06-04 - Production Debug Mode and Missing Error Handling
**Vulnerability:** The Flask application was running with `debug=True`, enabling the Werkzeug debugger which can lead to RCE. Furthermore, missing error handlers for data processing and model loading exposed raw stack traces on errors.
**Learning:** Hardcoded model paths (that fail in non-local environments) combined with `debug=True` create a dangerous path disclosure / stack trace leakage vector.
**Prevention:** Always deploy with `debug=False` and implement generic top-level exception handling for external routes to fail securely without leaking internal state.
