## 2024-05-24 - Interactive Debugger and Stack Trace Exposure
**Vulnerability:** Running Flask with `debug=True` in production code and lacking input validation exception handling exposes the Werkzeug interactive debugger and internal stack traces.
**Learning:** These exposures can be leveraged by attackers for Remote Code Execution (RCE) via the debugger or to map out internal application logic and paths via stack traces. Unhandled form parsing causes 500 errors.
**Prevention:** Ensure `debug=False` is set for deployment and wrap input parsing with `try...except (ValueError, KeyError)` returning a 400 Bad Request to gracefully handle malformed data without leaking state.
