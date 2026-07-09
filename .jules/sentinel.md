## 2024-05-24 - Unhandled input and Debug Mode
**Vulnerability:** 500 errors exposing stack traces and debug mode enabled in production.
**Learning:** Flask apps should not run with debug=True in production. Form input casting should be handled to avoid unhandled exceptions.
**Prevention:** Disable debug mode for production deployments. Always wrap user input parsing in try-except blocks.
