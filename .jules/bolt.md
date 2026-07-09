## $(date +%Y-%m-%d) - Module-Level Model Caching
**Learning:** Loading machine learning models from disk inside the request handler (e.g., inside the `/predict` route) causes a severe performance bottleneck because the model is read from disk on every single request.
**Action:** Always load heavy assets like ML models at the module level (global scope) so they are only loaded once when the application starts.
