import pandas as pd
import numpy as np
import joblib
import klib
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import os

# Create models directory
if not os.path.exists('models'):
    os.makedirs('models')

print("Loading data...")
# Load data
df_train = pd.read_csv('Train.csv')

print("Cleaning data...")
# Clean Item_Fat_Content
df_train['Item_Fat_Content'] = df_train['Item_Fat_Content'].replace({'LF': 'Low Fat', 'low fat': 'Low Fat', 'reg': 'Regular'})

# Fill missing values
df_train['Item_Weight'] = df_train['Item_Weight'].fillna(df_train['Item_Weight'].mean())
outlet_size_mode = df_train['Outlet_Size'].mode()[0]
df_train['Outlet_Size'] = df_train['Outlet_Size'].fillna(outlet_size_mode)

# Drop ID columns (based on notebook)
df_train.drop(['Item_Identifier', 'Outlet_Identifier'], axis=1, inplace=True)

# Clean column names (to match app.py expectations of snake_case)
df_train = klib.clean_column_names(df_train)

# Label Encoding
le = LabelEncoder()
text_cols = ['item_fat_content', 'item_type', 'outlet_size', 'outlet_location_type', 'outlet_type']
mappings = {}

print("Encoding categoricals...")
for col in text_cols:
    df_train[col] = le.fit_transform(df_train[col])
    # Store mappings to help build the UI
    mappings[col] = dict(zip(le.classes_, le.transform(le.classes_)))

print("Mappings:")
for col, mapping in mappings.items():
    print(f"{col}: {mapping}")

# Split X, Y
X = df_train.drop('item_outlet_sales', axis=1)
Y = df_train['item_outlet_sales']

# Split train/test (optional but good for consistency)
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, random_state=101, test_size=0.2)

print("Scaling features...")
# StandardScaler
sc = StandardScaler()
X_train_std = sc.fit_transform(X_train)
X_test_std = sc.transform(X_test)

# Save Scaler
joblib.dump(sc, 'models/sc.sav')

print("Training model...")
# Train Model
lr = LinearRegression()
lr.fit(X_train_std, Y_train)

# Save Model
joblib.dump(lr, 'models/lr.sav')

print("Models saved successfully to models/sc.sav and models/lr.sav")
