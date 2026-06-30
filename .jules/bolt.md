## 2024-06-30 - Cache Machine Learning Models at Startup
**Learning:** Loading ML models from disk synchronously inside request handlers causes severe latency degradation.
**Action:** Always load and cache heavy resources like ML models globally at application startup.
