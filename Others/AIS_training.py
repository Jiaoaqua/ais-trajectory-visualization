import pandas as pd
import numpy as np
from keras.models import Sequential
from keras.layers import Dense, LSTM, Dropout
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
from sqlalchemy import create_engine

# PostgreSQL Connection Configuration
DB_HOST = "localhost"
DB_NAME = "ais_data"
DB_USER = "group_3"
DB_PASSWORD = "12345678"

# Create database connection URL
db_url = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:5432/{DB_NAME}"
engine = create_engine(db_url)

# Define Turku region bounding box
LAT_MIN = 59.0
LAT_MAX = 62.0
LON_MIN = 19.5
LON_MAX = 25.0

print("Connecting to database.")

# Fetch latest 1000000 rows from data table
query = """
SELECT * FROM data
ORDER BY timestamp DESC
LIMIT 1000
"""
data = pd.read_sql(query, engine)

print(f"Fetched {len(data)} rows from the database.")

# Filter data for Turku region
data = data[(data['lat'] >= LAT_MIN) & (data['lat'] <= LAT_MAX) &
            (data['lon'] >= LON_MIN) & (data['lon'] <= LON_MAX)]

print(f"Data after filtering for Turku region: {len(data)} rows.")

# Select relevant columns
columns = ['lon', 'lat']
data = data[columns]

print(f"Data after selecting columns: {data.head()}")

# Normalize data
scaler = MinMaxScaler(feature_range=(0, 1))
scaled_data = scaler.fit_transform(data.values)

print(f"Scaled data sample: {scaled_data[:5]}")

# Convert series to supervised learning format
def series_to_supervised(data, n_in=1, n_out=1, dropnan=True):
    n_vars = 1 if type(data) is list else data.shape[1]
    df = pd.DataFrame(data)
    cols, names = list(), list()
    for i in range(n_in, 0, -1):
        cols.append(df.shift(i))
        names += [(f'var{j+1}(t-{i})') for j in range(n_vars)]
    for i in range(0, n_out):
        cols.append(df.shift(-i))
        if i == 0:
            names += [(f'var{j+1}(t)') for j in range(n_vars)]
        else:
            names += [(f'var{j+1}(t+{i})') for j in range(n_vars)]
    agg = pd.concat(cols, axis=1)
    agg.columns = names
    if dropnan:
        agg.dropna(inplace=True)
    return agg

reframed = series_to_supervised(scaled_data, 20, 1)

print(f"Reframed data sample: {reframed.head()}")

# Split data into training, validation, and test sets
train_days = 300
valid_days = 60
values = reframed.values
train = values[:train_days, :]
valid = values[train_days:train_days + valid_days, :]
test = values[train_days + valid_days:, :]
train_X, train_y = train[:, :-2], train[:, -2:]
valid_X, valid_y = valid[:, :-2], valid[:, -2:]
test_X, test_y = test[:, :-2], test[:, -2:]

print(f"Training data shape: {train_X.shape}, {train_y.shape}")
print(f"Validation data shape: {valid_X.shape}, {valid_y.shape}")
print(f"Test data shape: {test_X.shape}, {test_y.shape}")

train_X = train_X.reshape((train_X.shape[0], 1, train_X.shape[1]))
valid_X = valid_X.reshape((valid_X.shape[0], 1, valid_X.shape[1]))
test_X = test_X.reshape((test_X.shape[0], 1, test_X.shape[1]))

print(f"Reshaped training data shape: {train_X.shape}")
print(f"Reshaped validation data shape: {valid_X.shape}")
print(f"Reshaped test data shape: {test_X.shape}")

# Build LSTM model
model = Sequential()
model.add(LSTM(50, activation='relu', input_shape=(train_X.shape[1], train_X.shape[2]), return_sequences=True))
model.add(LSTM(2, activation='relu'))
model.compile(loss='mean_squared_error', optimizer='adam')

print("Model built successfully.")

# Train model
history = model.fit(train_X, train_y, epochs=100, batch_size=32, validation_data=(valid_X, valid_y), verbose=2, shuffle=False)

print("Model training complete.")

# Predict and visualize results
plt.figure(figsize=(24, 8))
plt.xlabel('Longitude')
plt.ylabel('Latitude')
train_predict = model.predict(train_X)
valid_predict = model.predict(valid_X)
test_predict = model.predict(test_X)

print("Predictions complete.")

plt.plot(values[:, 0], values[:, 1], label='raw_trajectory', c='b')
plt.plot(train_predict[:, 0], train_predict[:, 1], label='train_predict', c='g')
plt.plot(valid_predict[:, 0], valid_predict[:, 1], label='valid_predict', c='y')
plt.plot(test_predict[:, 0], test_predict[:, 1], label='test_predict', c='r')
plt.legend()
plt.show()
