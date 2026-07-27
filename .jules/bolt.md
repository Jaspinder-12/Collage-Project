## 2026-03-23 - Lazy Loading Models
**Learning:** Currently, models are loaded synchronously inside the route on every request. This is highly inefficient because reading from disk and deserializing takes time.
**Action:** Move model loading outside of the request handler or lazily load them and cache the result. I will use lazy loading with globals so it works smoothly with mock patching during testing.
