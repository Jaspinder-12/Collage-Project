## 2026-02-24 - Model-UI Consistency
**Learning:** When building UI for ML models, the categorical encoding (LabelEncoder) determines the strict values (integers) the UI must send. Guessing these values leads to errors.
**Action:** Always verify the training data encoding or regenerate the model to ensure the UI dropdowns map 1:1 to what the model expects.

## 2026-02-24 - Accessibility in Data Forms
**Learning:** Data science apps often lack basic semantic HTML (labels, fieldsets). Adding them massively improves usability without complex CSS.
**Action:** Always wrap inputs in labels or use `for`/`id` pairs, and use `<select>` for categorical data instead of asking users to type "Low Fat".
