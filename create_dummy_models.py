import joblib
import numpy as np
import os
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression

def create_models():
    # Create a dummy dataset with 9 features
    # 100 samples, 9 features
    X = np.random.rand(100, 9)
    y = np.random.rand(100)

    # Train StandardScaler
    sc = StandardScaler()
    X_std = sc.fit_transform(X)

    # Train LinearRegression
    lr = LinearRegression()
    lr.fit(X_std, y)

    # Save models
    models_dir = 'models'
    if not os.path.exists(models_dir):
        os.makedirs(models_dir)

    joblib.dump(sc, os.path.join(models_dir, 'sc.sav'))
    joblib.dump(lr, os.path.join(models_dir, 'lr.sav'))

    print("Models created successfully in 'models/' directory.")

if __name__ == "__main__":
    create_models()
