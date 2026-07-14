## 2024-05-24 - Unhandled Exceptions and Debug Mode Exposure
**Vulnerability:** The Flask application parses form inputs without a try-except block, leading to 500 errors. Also, `debug=True` exposes the Werkzeug interactive debugger and internal stack traces on these errors.
**Learning:** Exposing stack traces via debug mode or unhandled exceptions provides attackers with detailed internal knowledge of the application's environment and structure, which can be leveraged for further attacks.
**Prevention:** Always wrap user input parsing in try-except blocks, and always run Flask with `debug=False` (or without the debug flag) in production environments to fail securely.
