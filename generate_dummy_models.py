import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler
import joblib
import os

os.makedirs('models', exist_ok=True)
sc = StandardScaler()
sc.fit(np.zeros((2, 9)))
joblib.dump(sc, 'models/sc.sav')

lr = LinearRegression()
lr.fit(np.zeros((2, 9)), np.zeros(2))
joblib.dump(lr, 'models/lr.sav')
