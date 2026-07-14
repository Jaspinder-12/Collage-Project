## 2024-07-14 - Global Model Caching
**Learning:** In the Collage-Project application (`app.py`), machine learning models (`sc.sav`, `lr.sav`) were being loaded from disk inside the `/predict` route handler, causing synchronous disk I/O and deserialization overhead on every request.
**Action:** Cache machine learning models globally at startup instead of inside request handlers to prevent latency degradation.
