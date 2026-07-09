## 2024-06-15 - Unhandled Exception and Debug Mode Vulnerability
**Vulnerability:** The application runs with `debug=True` in production and directly casts user input without exception handling, exposing stack traces and the interactive debugger.
**Learning:** Failing to handle user input can trigger 500 errors, which combined with Flask's debug mode, creates a Remote Code Execution risk or leaks sensitive info.
**Prevention:** Always validate and safely cast user input using `try...except` blocks and never run Flask in `debug=True` mode in production.
