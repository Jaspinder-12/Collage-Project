## 2024-05-29 - Global Model Caching in Flask
**Learning:** Loading machine learning models inside request handlers causes severe performance degradation due to repetitive disk I/O and deserialization on every API call.
**Action:** Cache ML models and scalers in memory at the module level (global scope) during application startup, reusing them across all requests.
