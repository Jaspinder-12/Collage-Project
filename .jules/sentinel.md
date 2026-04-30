## 2024-05-24 - Disabled Flask Debug Mode
**Vulnerability:** Flask application deployed with debug=True.
**Learning:** Leaving debug=True enables the Werkzeug interactive debugger, allowing potential arbitrary Python code execution if exposed.
**Prevention:** Ensure debug=False is explicitly set for production deployments.