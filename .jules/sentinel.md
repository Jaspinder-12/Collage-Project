## 2024-05-23 - Initial Security Assessment
**Vulnerability:** Hardcoded paths and potential path traversal in model loading.
**Learning:** The application uses absolute paths for loading models (e.g., `D:\projects\...`), which is not portable and poses a security risk if user input were somehow involved in path construction (though currently it's hardcoded).  More critically, `app.run(debug=True)` is enabled, which exposes the interactive debugger in production if deployed as-is.
**Prevention:** Use relative paths or environment variables for configuration. Disable debug mode in production.

**Vulnerability:** Input validation missing.
**Learning:** The `/predict` endpoint casts form inputs directly to float without validation. This could lead to server errors (DoS) if non-numeric data is sent.
**Prevention:** Implement input validation using a library like `marshmallow` or manual checks.
