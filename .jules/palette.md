## 2025-05-01 - Add immediate loading feedback to inference form
**Learning:** Adding a basic JavaScript loading state (button disabled, text changed to "Predicting...") drastically improves perceived performance and prevents duplicate submissions during slow ML inferences, avoiding the need for a complex full page spinner.
**Action:** Always intercept form submissions to provide visual feedback (`disabled`, `aria-live="polite"`, `cursor: not-allowed`) before long-running backend routes take over.
