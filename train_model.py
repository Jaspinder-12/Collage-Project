import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.linear_model import LinearRegression
import joblib
import os

def train_and_save_model():
    print("Loading data...")
    df_train = pd.read_csv('Train.csv')

    print("Cleaning data...")
    # Handle missing values
    df_train['Item_Weight'] = df_train['Item_Weight'].fillna(df_train['Item_Weight'].mean())
    # Fill mode for Outlet_Size (careful with mode() returning a series)
    outlet_size_mode = df_train['Outlet_Size'].mode()[0]
    df_train['Outlet_Size'] = df_train['Outlet_Size'].fillna(outlet_size_mode)

    # Clean Item_Fat_Content
    df_train['Item_Fat_Content'] = df_train['Item_Fat_Content'].replace({'LF': 'Low Fat', 'low fat': 'Low Fat', 'reg': 'Regular'})

    # Label Encoding
    # We need to ensure the encoding is consistent with alphabetical order so we can replicate it in the UI
    le = LabelEncoder()
    categorical_cols = ['Item_Fat_Content', 'Item_Type', 'Outlet_Size', 'Outlet_Location_Type', 'Outlet_Type']

    mapping_info = {}

    for col in categorical_cols:
        # Fit transform to get the encoded values
        df_train[col] = le.fit_transform(df_train[col])
        # Store mapping for verification
        mapping = dict(zip(le.classes_, le.transform(le.classes_)))
        mapping_info[col] = mapping
        print(f"Encoded {col}: {mapping}")

    # Select features in the correct order matching app.py
    # app.py expects: item_weight, item_fat_content, item_visibility, item_type, item_mrp,
    # outlet_establishment_year, outlet_size, outlet_location_type, outlet_type

    X = df_train[['Item_Weight', 'Item_Fat_Content', 'Item_Visibility', 'Item_Type', 'Item_MRP',
                  'Outlet_Establishment_Year', 'Outlet_Size', 'Outlet_Location_Type', 'Outlet_Type']]
    Y = df_train['Item_Outlet_Sales']

    # Standardization
    print("Scaling features...")
    sc = StandardScaler()
    X_std = sc.fit_transform(X)

    # Train Model
    print("Training model...")
    lr = LinearRegression()
    lr.fit(X_std, Y)

    # Create models directory if not exists
    os.makedirs('models', exist_ok=True)

    # Save models
    print("Saving models...")
    joblib.dump(sc, 'models/sc.sav')
    joblib.dump(lr, 'models/lr.sav')
    print("Models saved successfully to models/sc.sav and models/lr.sav")

if __name__ == "__main__":
    train_and_save_model()
