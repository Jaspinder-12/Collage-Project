## 2026-03-01 - Disable submit button on form submission
**Learning:** In simple Flask apps without front-end frameworks, double form submissions can be an issue. Users might click multiple times before the model finishes predicting.
**Action:** Adding a simple vanilla JS snippet to disable the submit button and change its text to 'Predicting...' provides immediate visual feedback and prevents duplicate requests.
