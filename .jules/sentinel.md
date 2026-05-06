## 2025-05-06 - Flask Debug Mode Enabled in Main Block
**Vulnerability:** The Flask application was hardcoded to run with `debug=True` in the `if __name__ == "__main__":` block.
**Learning:** Leaving `debug=True` enabled exposes the Werkzeug interactive debugger, which allows arbitrary Python code execution (RCE) if an unhandled exception occurs (e.g. from missing request form parameters). It also leaks server filesystem paths and configuration.
**Prevention:** Always set `debug=False` for production deployments or use environment variables to explicitly control debug configurations.
