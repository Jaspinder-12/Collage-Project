## 2024-05-24 - Flask Debug Mode RCE Vulnerability
**Vulnerability:** Flask `app.run(debug=True)` was enabled in a context where it could be exposed, which allows attackers to access the Werkzeug interactive debugger and execute arbitrary Python code.
**Learning:** Production or externally facing Flask applications must never run with `debug=True`.
**Prevention:** Explicitly set `debug=False` (or remove `debug=True` as it defaults to False) and ensure environment variables strictly manage debug flags across environments.
