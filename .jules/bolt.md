
## 2024-03-19 - Test Mocking vs Module-Level Model Loading
**Learning:** Loading large Machine Learning models globally at the *module level* in Flask (i.e. outside any function) breaks test suites that rely on mocking (`pytest monkeypatch`), because the `joblib.load` execution happens during import, before the mock is applied.
**Action:** Always wrap global model loading in a lazy-init function (e.g. `load_models()`) and call it inside the route handler. This provides the performance benefit of loading models exactly once, while still allowing the test suite to safely mock the file system operations on module import.
