import numpy as np 
import tensorflow as tf 
from sklearn.preprocessing import MinMaxScaler 
# For simplicity, we have a function load_data() that returns your data. 
# input_data = load_data() 
# Generate random data for demonstration 
input_data = np.random.rand(1000, 50)

# Normalize the data 
scaler = MinMaxScaler() 
input_data_normalized = scaler.fit_transform(input_data)

# Set the compression dimension (output dimension of the neural network ) 
compression_dim = 10

# Build the neural network model 
model = tf.keras.models.Sequential([ 
    tf.keras.layers.Dense(128, activation='relu', input_shape=(input_data.shape[1],)), 
    tf.keras.layers.Dense(compression_dim, activation='relu'),
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dense(input_data.shape[1], activation='sigmoid')
])                                   
    
#Compile the model 
model.compile(optimizer='adam', loss='mean_squared_error') 
#Train the model 
model.fit(input_data_normalized, input_data_normalized, epochs=50, batch_size=32) 
#Compress the data 
compressed_data = model.predict(input_data_normalized)
              
# Print the results 
print("Original Data:") 
print(input_data[0]) 
print("\nCompressed Data:") 
print(compressed_data[0])
