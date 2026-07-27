## 2024-05-22 - Global Model Caching
**Learning:** Loading scikit-learn models inside request handlers causes severe performance degradation due to repetitive disk I/O and deserialization.
**Action:** Always load large machine learning models into memory globally at application startup to reuse them across all requests.
