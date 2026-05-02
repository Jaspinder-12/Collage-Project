## 2024-05-02 - Client-side formatting for raw predictions
**Learning:** Raw numerical machine learning predictions displayed to users can be confusing and lack professional polish. Formatting these numbers client-side with commas and limited decimal places using `Number.prototype.toLocaleString()` significantly improves readability without requiring backend logic changes.
**Action:** Always format raw numerical output explicitly into a localized format (e.g., currency or standard decimal presentation) when displaying it directly in the UI.
