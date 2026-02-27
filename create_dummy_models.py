import joblib
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
import os

# Create models directory if it doesn't exist
if not os.path.exists('models'):
    os.makedirs('models')

# Create dummy data (100 samples, 9 features)
X = np.random.rand(100, 9)
y = np.random.rand(100)

# Train scaler
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
joblib.dump(scaler, 'models/sc.sav')

# Train model
model = LinearRegression()
model.fit(X_scaled, y)
joblib.dump(model, 'models/lr.sav')

print("Dummy models created in models/")
