## 2024-04-22 - Fix Debug Mode Exposure
**Vulnerability:** The Flask application was running with `debug=True` in production code.
**Learning:** This can expose the Werkzeug interactive debugger to users, potentially allowing remote code execution if the debugger is exposed.
**Prevention:** Always set `debug=False` for production or avoid defining debug behavior directly in code without environment variables.
