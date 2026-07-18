## 2024-07-18 - Unhandled exceptions in form parsing
**Vulnerability:** User form input was directly cast to float without error handling, which would cause a 500 Internal Server Error and leak stack traces upon missing or malformed data.
**Learning:** Raw input extraction must always be wrapped in defensive try-except blocks (e.g. ValueError, KeyError) before further processing.
**Prevention:** Always use try-except blocks when handling user input and return a generic error message (400 Bad Request) instead of exposing application internals.
