import numpy as np

# Activation functions
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def sigmoid_derivative(x):
    return x * (1 - x)

# XOR Input and Output
X = np.array([
    [0, 0],
    [0, 1],
    [1, 0],
    [1, 1]
])

y = np.array([[0], [1], [1], [0]])

# Seed for reproducibility
np.random.seed(1)

# Define number of neurons
input_neurons = 2
hidden_neurons = 2
output_neurons = 1

# Initialize weights and biases
wh = np.random.uniform(size=(input_neurons, hidden_neurons))  # Weights between input and hidden
bh = np.random.uniform(size=(1, hidden_neurons))              # Bias for hidden layer
wo = np.random.uniform(size=(hidden_neurons, output_neurons)) # Weights between hidden and output
bo = np.random.uniform(size=(1, output_neurons))              # Bias for output layer

# Training parameters
epochs = 10000
learning_rate = 0.1

# Training loop
for epoch in range(epochs):
    # Feedforward
    hidden_input = np.dot(X, wh) + bh
    hidden_output = sigmoid(hidden_input)

    final_input = np.dot(hidden_output, wo) + bo
    final_output = sigmoid(final_input)

    # Calculate error
    error = y - final_output

    # Backpropagation
    d_output = error * sigmoid_derivative(final_output)
    error_hidden = d_output.dot(wo.T)
    d_hidden = error_hidden * sigmoid_derivative(hidden_output)

    # Update weights and biases
    wo += hidden_output.T.dot(d_output) * learning_rate
    bo += np.sum(d_output, axis=0, keepdims=True) * learning_rate
    wh += X.T.dot(d_hidden) * learning_rate
    bh += np.sum(d_hidden, axis=0, keepdims=True) * learning_rate

    # Print error occasionally
    if epoch % 1000 == 0:
        print(f"Epoch {epoch}, Error: {np.mean(np.abs(error))}")

# Final prediction
print("\nFinal Output after Training:\n")
print("Input      Predicted   Target")
for i in range(len(X)):
    print(f"{X[i]}   ->   {final_output[i][0]:.3f}     (Expected: {y[i][0]})")
