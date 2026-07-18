import joblib
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
import numpy as np

sc = StandardScaler()
sc.fit(np.array([[1, 2, 3, 4, 5, 6, 7, 8, 9]]))
joblib.dump(sc, 'models/sc.sav')

class DummyModel:
    def predict(self, X):
        return np.array(100.0) # To prevent TypeError when casting to float

model = DummyModel()
joblib.dump(model, 'models/lr.sav')
