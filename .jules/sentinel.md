## 2024-04-17 - Flask Debug Mode Enabled
**Vulnerability:** Flask's Werkzeug interactive debugger was left exposed by running the application with `debug=True`.
**Learning:** Hardcoding `debug=True` in the main application block leaves production-like deployments vulnerable to arbitrary remote code execution via the debugger console.
**Prevention:** Always set `debug=False` for production, and ideally load debug configurations from secure environment variables rather than hardcoding.
