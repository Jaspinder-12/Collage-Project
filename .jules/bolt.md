## 2025-02-18 - Caching ML Models
**Learning:** Loading scikit-learn machine learning models synchronously from disk inside route handlers causes significant, repetitive serialization/deserialization overhead.
**Action:** Always hoist file loading for models to the global scope at startup to cache them in memory. Convert hardcoded absolute paths to relative paths (`os.path.join(os.path.dirname(os.path.abspath(__file__)), ...)`) to avoid cross-platform crashes during import.
