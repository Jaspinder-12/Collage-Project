## 2024-07-26 - Prevent Stack Trace Exposure on Invalid Inputs
**Vulnerability:** User inputs from web forms were cast to floats without error handling, which would cause a `ValueError` or `KeyError`, leading to a 500 Internal Server Error that exposes sensitive stack traces.
**Learning:** Web applications must defensively handle all user inputs and fail securely to prevent leaking internal implementation details via stack traces.
**Prevention:** Always wrap user input extraction and casting in `try...except` blocks and return generic error pages or safe fallbacks.

## 2024-07-26 - Critical Werkzeug Debugger Vulnerability
**Vulnerability:** Flask was running with `debug=True` in production, which enabled the interactive Werkzeug debugger. This creates a critical Remote Code Execution (RCE) vulnerability and exposes sensitive stack traces on any unhandled exception.
**Learning:** Development configurations (like debug modes) are often accidentally deployed and expose massive security risks.
**Prevention:** Never use `debug=True` in production. Always set `debug=False` for Flask apps in deployed environments.
