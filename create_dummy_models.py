import os
import joblib
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
import numpy as np

os.makedirs('models', exist_ok=True)

# Dummy scaler
sc = StandardScaler()
sc.fit(np.random.rand(10, 9))
joblib.dump(sc, 'models/sc.sav')

# Dummy model
lr = LinearRegression()
lr.fit(np.random.rand(10, 9), np.random.rand(10))
joblib.dump(lr, 'models/lr.sav')

print("Dummy models created.")
