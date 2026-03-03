## 2024-03-03 - Global Model Loading vs Request Scope
**Learning:** Initializing machine learning models (`joblib.load`) inside the request route execution (`/predict`) creates a massive I/O bottleneck and performance penalty on every request.
**Action:** Always load heavy ML models into global scope at app startup. Wrap the loading in a `try/except` to allow tests and the app to load gracefully even when actual model artifact files (`sc.sav`, `lr.sav`) are missing.
