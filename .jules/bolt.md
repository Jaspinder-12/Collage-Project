## 2024-05-24 - Model Deserialization Bottleneck
**Learning:** Machine learning models loaded synchronously inside request handlers cause severe response latency degradation due to repeated disk I/O and deserialization.
**Action:** Always load and cache heavy assets (like ML models or scalers) in memory at application startup in global scope.
