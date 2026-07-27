## 2024-04-05 - Use HTML5 validation attributes for micro-UX
**Learning:** For physical quantities (like weight, price, visibility) adding `min="0"` directly to HTML5 numerical inputs prevents impossible negative values from being entered via browser UI controls or directly, offering an immediate native micro-UX validation improvement without requiring custom Javascript validation logic.
**Action:** Always apply basic physical limits via `min` and `max` constraints to numerical inputs to provide immediate guardrails and guide accurate data entry.
