import numpy as np

class DummyScaler:
    def transform(self, X):
        return X

class DummyModel:
    def predict(self, X):
        return np.array([1234.56789])
