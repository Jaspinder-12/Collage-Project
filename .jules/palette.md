
## 2026-03-03 - Fix invalid CSS 'ring' and add required field indicators
**Learning:** The codebase attempted to use a Tailwind CSS utility class ('ring') as a standard CSS property in a plain HTML/CSS template (`templates/home.html`), causing focus states to fail silently. Relying on visual cues like a red asterisk `*` for all required fields improves form accessibility.
**Action:** Replaced invalid 'ring' property with standard CSS `box-shadow` for focus visibility, and added `label::after { content: " *"; color: #ef4444; }` for required field indicators. Always verify CSS properties are valid in vanilla environments.
