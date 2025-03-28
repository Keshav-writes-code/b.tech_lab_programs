import numpy as np
# Sigmoid activation function and its derivative
def sigmoid(x):
    return 1 / (1 + np.exp(-x))
def sigmoid_derivative(x):
    return x * (1 - x)

# Training function for the neural network
def train_neural_network(inputs, outputs, epochs=10000, learning_rate=0.1):
    input_layer_neurons = inputs.shape[0]
    hidden_layer_neurons = 5
    output_layer_neurons = outputs.shape[0]
    # Initialize weights and biases
    hidden_weights = np.random.uniform(size=(hidden_layer_neurons, input_layer_neurons))
    hidden_biases = np.zeros((hidden_layer_neurons, 1))
    output_weights = np.random.uniform(size=(output_layer_neurons, hidden_layer_neurons))
    output_biases = np.zeros((output_layer_neurons, 1))

    for epoch in range(epochs):
        # Forward pass
        hidden_layer_input = np.dot(hidden_weights, inputs) + hidden_biases
        hidden_layer_output = sigmoid(hidden_layer_input)
        output_layer_input = np.dot(output_weights, hidden_layer_output) + output_biases
        predicted_output = sigmoid(output_layer_input)

        # Backpropagation
        error = outputs - predicted_output
        output_delta = error * sigmoid_derivative(predicted_output)
        hidden_layer_error = np.dot(output_weights.T, output_delta)
        hidden_layer_delta = hidden_layer_error * sigmoid_derivative(hidden_layer_output)

        # Update weights and biases
        output_weights += learning_rate * np.dot(output_delta, hidden_layer_output.T)
        output_biases += learning_rate * np.sum(output_delta, axis=1, keepdims=True)
        hidden_weights += learning_rate * np.dot(hidden_layer_delta, inputs.T)
        hidden_biases += learning_rate * np.sum(hidden_layer_delta, axis=1, keepdims=True)
    return hidden_weights, hidden_biases, output_weights, output_biases

# Prediction function
def predict(test_data, hidden_weights, hidden_biases, output_weights, output_biases):
    hidden_layer_input = np.dot(hidden_weights, test_data) + hidden_biases
    hidden_layer_output = sigmoid(hidden_layer_input)
    output_layer_input = np.dot(output_weights, hidden_layer_output) + output_biases
    predicted_output = sigmoid(output_layer_input)
    return predicted_output.round()

# Example inputs and outputs
input_data = np.random.randint(2, size=(5, 10))
output_data = np.random.randint(2, size=(10, 10))

# Train the network
hidden_weights, hidden_biases, output_weights, output_biases = train_neural_network(input_data, output_data)

# Testing the network
test_data = np.random.randint(2, size=(5, 5))
predictions = predict(test_data, hidden_weights, hidden_biases, output_weights, output_biases)
print("Test data:")
print(test_data)
print("\nPredictions:")
print(predictions)
