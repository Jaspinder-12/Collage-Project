## 2024-04-29 - Werkzeug Debugger Exposure
**Vulnerability:** Flask development server was running with `debug=True`.
**Learning:** Leaving debug mode on in a public-facing app exposes the Werkzeug interactive debugger, leading to remote code execution risks.
**Prevention:** Always ensure `debug=False` for production deployments or use environment variables to control the debug flag.
