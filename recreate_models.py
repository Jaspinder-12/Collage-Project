import pandas as pd
import numpy as np
import joblib
import os
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.linear_model import LinearRegression

def main():
    print("Loading data...")
    df_train = pd.read_csv('Train.csv')

    # Imputation
    print("Imputing missing values...")
    df_train['Item_Weight'] = df_train['Item_Weight'].fillna(df_train['Item_Weight'].mean())
    df_train['Outlet_Size'] = df_train['Outlet_Size'].fillna(df_train['Outlet_Size'].mode()[0])

    # Drop unnecessary columns
    print("Dropping columns...")
    df_train.drop(['Item_Identifier', 'Outlet_Identifier'], axis=1, inplace=True)

    # Rename columns to snake_case
    print("Renaming columns...")
    df_train.columns = [col.lower() for col in df_train.columns]

    # Categorical columns to encode
    categorical_cols = ['item_fat_content', 'item_type', 'outlet_size', 'outlet_location_type', 'outlet_type']

    print("Encoding categorical variables...")
    le = LabelEncoder()
    mappings = {}

    for col in categorical_cols:
        df_train[col] = le.fit_transform(df_train[col])
        # Get mapping
        mapping = dict(zip(le.classes_, le.transform(le.classes_)))
        mappings[col] = mapping
        print(f"Mapping for {col}: {mapping}")

    # Split X and Y
    X = df_train.drop('item_outlet_sales', axis=1)
    Y = df_train['item_outlet_sales']

    # Standardization
    print("Standardizing...")
    sc = StandardScaler()
    X_std = sc.fit_transform(X)

    # Save Scaler
    print("Saving Scaler...")
    joblib.dump(sc, 'models/sc.sav')

    # Train Model
    print("Training Linear Regression...")
    lr = LinearRegression()
    lr.fit(X_std, Y)

    # Save Model
    print("Saving Model...")
    joblib.dump(lr, 'models/lr.sav')

    print("Done!")

if __name__ == "__main__":
    main()
