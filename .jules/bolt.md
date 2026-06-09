## 2024-06-09 - Global Model Caching in Flask
**Learning:** Loading machine learning models from disk on every request is a severe performance bottleneck. However, moving them to global scope requires careful fallback mechanisms (like Mock classes) so the app doesn't crash during initialization in environments like CI where the model files might be absent.
**Action:** Always cache expensive static resources globally in web frameworks, but use robust `try...except` fallbacks with mock objects to handle environments where files are missing.
