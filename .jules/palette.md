
## 2026-03-10 - Programmatic Association of Helper Text
**Learning:** Visual proximity of helper text or hints near an input field does not translate to accessibility for screen readers. Simply placing a `<div class="hint">` next to an `<input>` is insufficient.
**Action:** Always assign a unique `id` to helper text elements and explicitly link them to their corresponding input fields using the `aria-describedby` attribute to ensure screen readers announce the supplementary information properly.
