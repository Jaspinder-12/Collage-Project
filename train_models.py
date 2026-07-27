import pandas as pd
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import joblib
import os


def clean_column_names(df):
    df.columns = df.columns.str.lower().str.replace('.', '_')
    return df


def train_and_save_models():
    # Load data
    try:
        df_train = pd.read_csv('Train.csv')
    except FileNotFoundError:
        print("Error: Train.csv not found.")
        return

    # Impute missing values
    df_train['Item_Weight'] = df_train['Item_Weight'].fillna(df_train['Item_Weight'].mean())
    mode_outlet_size = df_train['Outlet_Size'].mode()[0]
    df_train['Outlet_Size'] = df_train['Outlet_Size'].fillna(mode_outlet_size)

    # Drop identifiers
    df_train.drop(['Item_Identifier', 'Outlet_Identifier'], axis=1, inplace=True)

    # Clean column names
    df_train = clean_column_names(df_train)

    # Label Encoding
    le = LabelEncoder()
    categorical_cols = ['item_fat_content', 'item_type', 'outlet_size', 'outlet_location_type', 'outlet_type']

    # We need to ensure consistent encoding.
    # In a real scenario, we would fit the encoders and save them too,
    # but here we just replicate the notebook which fits on the fly.
    for col in categorical_cols:
        df_train[col] = le.fit_transform(df_train[col])

    # Prepare X and Y
    X = df_train.drop('item_outlet_sales', axis=1)
    Y = df_train['item_outlet_sales']

    # Split data (using random_state=101 as in notebook)
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, random_state=101, test_size=0.2)

    # Standardization
    sc = StandardScaler()
    X_train_std = sc.fit_transform(X_train)
    # X_test_std = sc.transform(X_test) # Not needed for saving model

    # Save Scaler
    if not os.path.exists('models'):
        os.makedirs('models')

    joblib.dump(sc, os.path.join('models', 'sc.sav'))
    print("Scaler saved to models/sc.sav")

    # Train Linear Regression
    lr = LinearRegression()
    lr.fit(X_train_std, Y_train)

    # Save Model
    joblib.dump(lr, os.path.join('models', 'lr.sav'))
    print("Model saved to models/lr.sav")


if __name__ == "__main__":
    train_and_save_models()
