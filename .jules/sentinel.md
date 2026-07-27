## 2024-04-11 - [Input Validation and Error Handling]
**Vulnerability:** The application was not validating input data and would crash with a `ValueError` stack trace when processing non-numeric inputs in `app.py`. Furthermore, `debug=True` was enabled in production which leaks stack traces and sensitive internal configuration upon error.
**Learning:** Proper input handling ensures error responses do not leak implementation details and limits risk. Disabling debug mode in production is critical to prevent information disclosure.
**Prevention:** Implement `try-except` blocks for all user inputs from requests and handle specific expected exception types (`KeyError`, `ValueError`, `TypeError`). Always disable `debug` mode in `app.run()`.
