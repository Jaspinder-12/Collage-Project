## 2025-05-03 - Disabled Flask Debug Mode in Production
**Vulnerability:** Flask debug mode was left enabled (`debug=True`) in the production startup script (`app.py`).
**Learning:** Leaving Flask debug mode enabled in production exposes the Werkzeug interactive debugger, which can lead to Remote Code Execution (RCE) and information leakage.
**Prevention:** Always ensure `debug=False` for production deployments, or preferably, use a production WSGI server like Gunicorn.
