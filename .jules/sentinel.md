## 2024-05-04 - Fix debug mode RCE vulnerability and stack trace leakage
**Vulnerability:** Application ran in debug mode and lacked error handling, exposing interactive Werkzeug debugger (RCE risk) and stack traces.
**Learning:** Hardcoding `debug=True` in production code is extremely dangerous. Any unhandled exception can leak stack details.
**Prevention:** Always set `debug=False` for production deployments and implement general exception catchers on user input endpoints to fail securely.
