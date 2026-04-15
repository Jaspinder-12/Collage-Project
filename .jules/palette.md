## 2024-05-15 - Micro-UX feedback with native constraints and ARIA live
**Learning:** For long-running ML predictions, disabling the submit button and providing feedback via an ARIA live region gives confidence without blocking UI.
**Action:** Always wrap prediction forms with this snippet and add constraints natively.

## 2024-05-15 - Enhancing accessibility with required fields and helper text
**Learning:** ML forms often require specific categorical integers which users might not know. Additionally, missing inputs on the backend will cause 400 Bad Request or TypeErrors. Adding `required` attributes and `aria-describedby` helper text natively guides users and prevents errors before submission.
**Action:** Always map confusing categorical inputs to human-readable hints and enforce required fields via HTML5 validation.
