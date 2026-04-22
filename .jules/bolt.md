## 2025-04-21 - Optimize ML model loading
**Learning:** Loading ML models synchronously on every `/predict` request causes a significant performance bottleneck (latency per request) and memory overhead.
**Action:** Load models globally at module level, so they are initialized once at server startup and reused across requests.
