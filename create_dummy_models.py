import os
import joblib
from dummy_classes import DummyScaler, DummyModel

if __name__ == '__main__':
    os.makedirs('models', exist_ok=True)
    joblib.dump(DummyScaler(), os.path.join('models', 'sc.sav'))
    joblib.dump(DummyModel(), os.path.join('models', 'lr.sav'))
