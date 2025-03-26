import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, mean_squared_error
import joblib

# Load and clean data (only use first 50,000 rows to reduce model size)
df = pd.read_csv("coding/Processed_AIS_Training_Data.csv")
df = df.dropna().head(50000)

# Define input and target variables
X = df[["latitude", "longitude", "velocity", "heading", "cog"]]
y = df[["target_latitude", "target_longitude"]]

# Check for missing values
if X.isnull().values.any() or y.isnull().values.any():
    print("Still have missing values!")
    print("X missing:\n", X.isnull().sum())
    print("y missing:\n", y.isnull().sum())
    exit()

# Split into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a smaller Random Forest model
print("Training model...")
model = RandomForestRegressor(
    n_estimators=20,      # Fewer trees
    max_depth=10,         # Limit tree depth
    random_state=42
)
model.fit(X_train, y_train)

# Evaluate performance
y_pred = model.predict(X_test)
print("MAE:", mean_absolute_error(y_test, y_pred))
print("MSE:", mean_squared_error(y_test, y_pred))

# Save the model
joblib.dump(model, "coding/trajectory_rf_model.pkl")
print("Model saved to: coding/trajectory_rf_model.pkl")




