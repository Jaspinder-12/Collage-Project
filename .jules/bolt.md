## 2024-05-27 - Global Model Caching in Flask
**Learning:** Scikit-learn models and scalers loaded via joblib must be cached in memory globally to reuse across requests. Loading them inside request handlers causes severe performance degradation due to repetitive disk I/O and deserialization.
**Action:** When working with Flask ML applications, always move `joblib.load()` or similar model loading functions to the global scope so they are only executed once when the application starts.
