## 2026-04-18 - Model I/O Bottleneck Mitigation
**Learning:** Hardcoded model loading inside routing handlers (`joblib.load`) creates a major disk I/O bottleneck resulting in severe performance degradation (~0.025s/req to ~0.0036s/req latency).
**Action:** Always verify machine learning models or heavy artifacts are cached or lazy-loaded at the module level rather than on a per-request basis.
