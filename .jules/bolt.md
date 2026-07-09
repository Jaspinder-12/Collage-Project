## 2024-06-02 - Move Model Loading to Global Scope
**Learning:** Loading heavy ML models per request creates severe performance bottlenecks and increases response latency significantly.
**Action:** Always cache and load static assets like ML models at the module (global) scope rather than within route handlers to ensure they are loaded only once during application startup.
