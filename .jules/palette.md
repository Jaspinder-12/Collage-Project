## 2024-03-22 - Add Form Submission Loading State
**Learning:** Adding a visible loading state (e.g., text change to "Predicting..." and disabling the button with `cursor: not-allowed; opacity: 0.7;`) using vanilla JS significantly improves UX during blocking backend requests (like loading ML models) by providing immediate feedback.
**Action:** Always provide explicit disabled/loading states for form submissions that trigger time-consuming async/blocking backend operations.
