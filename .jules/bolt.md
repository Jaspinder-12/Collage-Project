## 2024-05-24 - Model Lazy Loading
**Learning:** scikit-learn machine learning models loaded via joblib are stateless during inference, meaning a single lazily-loaded global model instance can be safely shared across concurrent requests without thread-safety issues.
**Action:** Always load models once globally (lazy loaded in the route) to save massive I/O and memory overhead per request, rather than reloading the model every single time the route is hit. Use `global` keyword appropriately to modify the reference but avoid it if just reading to prevent flake8 errors.
