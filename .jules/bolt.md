## 2026-03-21 - Lazy Load Machine Learning Models
**Learning:** Loading models with `joblib.load` on every request creates an I/O bottleneck and adds significant latency, but loading at module scope breaks tests before `monkeypatch` can mock the models.
**Action:** Use a global cache populated by a lazy-loading function inside the route (or a helper function) to balance testability (mocking) and production performance (load once, reuse).
