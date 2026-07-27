import joblib
import numpy as np
import os
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler

os.makedirs('models', exist_ok=True)

sc = StandardScaler()
sc.fit(np.random.rand(10, 9))
joblib.dump(sc, 'models/sc.sav')

lr = LinearRegression()
lr.fit(np.random.rand(10, 9), np.random.rand(10))
joblib.dump(lr, 'models/lr.sav')
