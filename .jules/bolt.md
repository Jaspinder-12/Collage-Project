## 2024-04-16 - Prevent Global Scope Errors When Lazy Loading Machine Learning Models
**Learning:** Loading expensive ML models inside a Flask route using `global` causes `flake8` F824 errors and pollutes the global namespace.
**Action:** Use a module-level dictionary (e.g. `model_cache = {}`) and initialize the model objects within the route using `if key not in dict`. This cleanly achieves lazy loading (preventing expensive disk I/O per request) and ensures compatibility with linters and tests.
