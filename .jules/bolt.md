## 2024-05-18 - Lazy Loading ML Models in Flask
**Learning:** Loading scikit-learn ML models synchronously from disk on every `/predict` request causes significant thread blocking due to heavy I/O, increasing latency.
**Action:** Use a module-level dictionary (`model_cache`) to lazily load and cache models on the first request to drastically improve per-request latency.
