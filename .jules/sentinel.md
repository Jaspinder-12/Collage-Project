## 2024-05-24 - Unhandled Input and Debug Mode in Flask
**Vulnerability:** The Flask app exposed internal stack traces due to `debug=True` and unhandled exceptions (ValueError, KeyError) when casting user input to floats.
**Learning:** Raw input from `request.form` should always be validated and cast inside a try-except block to gracefully handle unexpected types or missing keys. Leaving debug mode on in Flask applications can lead to RCE via the interactive debugger.
**Prevention:** Always set `debug=False` in production and wrap direct user input type-casting in `try-except` blocks, returning a safe error message instead of crashing.
