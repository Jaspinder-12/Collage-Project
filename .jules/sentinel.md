## 2024-06-01 - Flask Debugger RCE Risk
**Vulnerability:** Flask application configured with `debug=True` at the module level.
**Learning:** Enabling `debug=True` activates the interactive Werkzeug debugger, which allows arbitrary code execution from the browser if exposed publicly.
**Prevention:** Always ensure `debug=False` in production or default configurations to prevent RCE and data leakage.
