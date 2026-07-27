import joblib
import numpy as np
import os
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression

# Ensure models directory exists
os.makedirs('models', exist_ok=True)

# Generate dummy training data matching the expected input shape
# 9 features: item_weight, item_fat_content, item_visibility, item_type, item_mrp,
# outlet_establishment_year, outlet_size, outlet_location_type, outlet_type
X_train = np.random.rand(100, 9)
y_train = np.random.rand(100)

# Train and save StandardScaler
sc = StandardScaler()
X_train_std = sc.fit_transform(X_train)
joblib.dump(sc, os.path.join('models', 'sc.sav'))
print("Dummy StandardScaler saved to models/sc.sav")

# Train and save LinearRegression model
lr = LinearRegression()
lr.fit(X_train_std, y_train)
joblib.dump(lr, os.path.join('models', 'lr.sav'))
print("Dummy LinearRegression model saved to models/lr.sav")
