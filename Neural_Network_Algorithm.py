import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import tensorflow as tf 
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout
from tensorflow.keras.optimizers import Adam

file_path = rf'D:\Datasets\Illegal Fishing\Processed Data\filtered_ship_data.csv'
df = pd.read_csv(file_path)

df['shiptype']=df['shiptype'].map({
'drifting_longlines':1,
'fixed_gear':2,
'pole_and_line':3,
'purse_seines':4,
'trawlers':5,
'trollers':6,
'unknown':7 })
X_numeric = df[['speed', 'course', 'distance_from_shore', 'distance_from_port', 'lat', 'lon','shiptype']].values

y = df['illegal'].map({'yes':2, 'maybe':1,'no':0})


# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X_numeric, y, test_size=0.2, random_state=42)

# Standard scaling
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Neural network model
model = Sequential([
    Dense(32, activation='relu', input_shape=(X_train.shape[1],)),
    Dense(16, activation='relu'),
    Dense(1, activation='sigmoid')
])

# Compile the model
model.compile(optimizer=Adam(learning_rate=0.001), loss='binary_crossentropy', metrics=['accuracy'])

# Train the model
history = model.fit(X_train_scaled, y_train, epochs=10, batch_size=32, validation_data=(X_test_scaled, y_test))

loss, accuracy = model.evaluate(X_test_scaled, y_test)
model.save('Neural_Network_Model.keras')

print(f'Test Accuracy: {accuracy}')