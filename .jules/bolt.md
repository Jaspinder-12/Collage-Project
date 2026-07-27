## 2025-02-18 - Model Loading Performance
**Learning:** Loading heavy ML models (using joblib/pickle) inside the request handler causes significant latency as the file is read and deserialized on every request.
**Action:** Always load models at the module level (global scope) or using a lazy-loading singleton pattern so they are loaded once at startup.
