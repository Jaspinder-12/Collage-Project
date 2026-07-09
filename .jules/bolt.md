## 2024-06-10 - Global Model Caching in Flask
**Learning:** Initializing machine learning models (`joblib.load()`) inside Flask request handlers causes severe performance bottlenecks due to repetitive disk I/O and deserialization per request.
**Action:** Load machine learning models once globally at the module level to ensure they are cached in memory for all subsequent requests, falling back to mock models safely when files are absent.
