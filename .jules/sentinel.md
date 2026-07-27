## 2025-01-29 - Missing Input Validation
**Vulnerability:** Unhandled ValueError and KeyError exceptions on user input parsing could crash the application and leak stack traces.
**Learning:** Raw form data must always be validated and caught within a try-except block before processing to prevent information disclosure.
**Prevention:** Implement input validation wrappers or use robust form validation libraries for all external inputs.
