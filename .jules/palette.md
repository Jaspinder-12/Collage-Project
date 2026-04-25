## 2024-04-25 - Informing Screen Readers During ML Predictions
**Learning:** During long-running async operations like ML predictions, visually disabling the submit button is insufficient for screen reader users, who might not perceive the visual change and remain unaware of the system state.
**Action:** Always implement an ARIA live region (e.g., `aria-live="polite"`) that gets updated with status text like "Predicting..." to provide confidence to assistive technologies without blocking the main UI.

## 2024-04-25 - Formatting Raw ML Output
**Learning:** Rendering raw floating-point numbers directly from ML models creates an unpolished and hard-to-read UI, especially for monetary or large unit predictions.
**Action:** Apply client-side vanilla JavaScript formatting (e.g., `Number.prototype.toLocaleString()`) to natively handle thousands separators and decimal limits, ensuring the UI remains readable without needing to alter the backend data flow.
