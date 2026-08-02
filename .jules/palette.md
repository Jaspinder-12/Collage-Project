## 2024-04-12 - Using HTML5 Native Validation and Native Attributes for Number Values

**Learning:** Changing input `type="text"` to `type="number"` with native properties (`min`, `max`, `step`) is a simple, effective micro-UX improvement that enforces numeric input via browser without adding complex custom JS validation. It specifically improves accessibility on mobile devices by triggering the numerical keyboard. Also, using `aria-live="polite"` on the submit button ensures screen readers are aware of the temporary "Predicting..." loading state, providing feedback that a slow request is happening.

**Action:** Whenever a backend expects float/integer values (which cast using `float()` or `int()` and might error on strings), ensure forms utilize native HTML5 validation and constraints to reduce 500 errors gracefully from invalid user entry, avoiding custom styling/validation bloat where native handles it.
