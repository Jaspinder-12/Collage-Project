
## 2026-04-03 - Form Accessibility Hint
**Learning:** Helper text for form inputs (like physical descriptions or format rules) must be explicitly associated with the input field using the `aria-describedby` attribute, pointing to the ID of the hint element. Without this, screen readers will not announce the extra context when the field receives focus.
**Action:** Always verify that informational helper text adjacent to form fields is linked via `aria-describedby` to ensure all users receive necessary context for completing the form.
