## 2026-02-24 - [Unsanitized Dev Environment Leak]
**Vulnerability:** Production app configured with `debug=True` and hardcoded local Windows paths.
**Learning:** The repository reflects a raw developer environment dump, leaking internal path structures and enabling debug mode by default, which exposes stack traces and potential RCE.
**Prevention:** Strip debug flags and use relative paths or environment variables before committing.
