## 2026-03-01 - Add Form Loading State
**Learning:** Added basic UX loading state to the submit button while the prediction is running on the backend. This improves perceived performance.
**Action:** Always add loading states to async operations or complex form submissions to prevent multiple clicks and reassure the user.

## 2026-04-27 - Format Raw ML Predictions
**Learning:** Displaying raw machine learning numerical outputs can confuse users with excessive decimal places. Formatting the output on the client-side improves readability.
**Action:** Always use client-side vanilla JavaScript (e.g., `toLocaleString()`) to format raw numerical predictions for visual clarity without altering backend logic.
