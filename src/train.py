import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
import joblib

# Load data
df = pd.read_csv("Fraud.csv")   # keep file in same folder or adjust path

# Sampling
df = df.sample(n=200000, random_state=42)

# Preprocessing
df = pd.get_dummies(df, columns=['type'], drop_first=True)
df = df.drop(['nameOrig', 'nameDest'], axis=1)

# Features & target
X = df.drop('isFraud', axis=1)
y = df['isFraud']

# Model
model = RandomForestClassifier(random_state=42)
model.fit(X, y)

# Save model + columns (IMPORTANT)
joblib.dump(model, "model.pkl")
joblib.dump(X.columns, "columns.pkl")

print("Model trained and saved successfully!")
