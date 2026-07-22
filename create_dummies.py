import joblib
import os
import numpy as np

os.makedirs('models', exist_ok=True)

class DummyScaler:
    def transform(self, X):
        return X

class DummyModel:
    def predict(self, X):
        return np.array(100.0)

joblib.dump(DummyScaler(), 'models/sc.sav')
joblib.dump(DummyModel(), 'models/lr.sav')
