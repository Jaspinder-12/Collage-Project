## 2026-02-25 - [Insecure Flask Configuration]
**Vulnerability:** Found `debug=True` enabled in production entry point and hardcoded absolute file paths for models.
**Learning:** The application was likely developed on a local Windows machine and deployed without cleaning up development settings.
**Prevention:** Use environment variables for configuration and relative paths using `os.path`.
