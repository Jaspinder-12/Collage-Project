## 2024-05-04 - Caching multiple ML models in Flask
**Learning:** When loading multiple interdependent machine learning assets (like a scaler and a prediction model) for a Flask route, they must be cached together using a combined condition (e.g., `if 'sc' not in cache or 'model' not in cache:`) to prevent partial cache state bugs. Also using `Y_pred[0]` avoids NumPy deprecation warnings when rendering scalar predictions.
**Action:** Always group related ML assets into a single cache check, and extract scalar predictions using array indexing instead of passing the entire array to `float()`.
