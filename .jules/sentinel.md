## 2024-05-18 - [Security Assessment]
**Vulnerability:** Initial look indicates the `app.py` has debug mode enabled (`app.run(debug=True, port=9457)`).
**Learning:** Running Flask with `debug=True` exposes the Werkzeug interactive debugger, a critical security risk allowing RCE.
**Prevention:** Always set `debug=False` for production deployments.
