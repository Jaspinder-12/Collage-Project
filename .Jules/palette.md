## 2024-03-27 - Initializing Palette Journal\n**Learning:** Initializing journal for future learnings.\n**Action:** Create journal if missing.

## 2024-03-27 - Add native form validation for numerical inputs
**Learning:** Native HTML validation (`min="0"`) on `<input type="number">` prevents users from accidentally submitting logically invalid data (like negative prices or weights), improving form robustness and providing instant visual feedback without the need for custom JavaScript validation logic.
**Action:** Always check numeric inputs that correspond to physical quantities (like weight, price, dimensions) and add appropriate `min` and `max` boundaries.
