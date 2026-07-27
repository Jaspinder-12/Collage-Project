## 2024-04-21 - [CRITICAL] Prevent Werkzeug Debugger Exposure
**Vulnerability:** Flask application started with debug=True which exposes the Werkzeug interactive debugger to users, potentially allowing remote code execution. Also lacks error handling in the prediction route, leading to potential sensitive internal stack traces leakage on invalid input.
**Learning:** Default Flask configurations (debug=True) and missing generic error handling can easily leave the app vulnerable to remote code execution and information disclosure.
**Prevention:** Always set debug=False for production and ensure robust error handling using try-except blocks that fail gracefully without exposing underlying error strings.
