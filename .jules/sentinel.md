## 2024-05-02 - Information Disclosure in Production
**Vulnerability:** Debug mode (`debug=True`) was enabled in `app.run()`, exposing the Werkzeug interactive debugger and potential unhandled exceptions to users.
**Learning:** Production applications should never expose internal stack traces or interactive debuggers.
**Prevention:** Always set `debug=False` for production or omit it entirely in deployment configurations.
