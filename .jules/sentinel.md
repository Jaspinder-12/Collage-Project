## 2026-04-13 - Fix debug mode in production
**Vulnerability:** Flask was running with `debug=True` in production.
**Learning:** This could expose sensitive information via stack traces.
**Prevention:** Always ensure `debug=False` when running web frameworks in production environments.
