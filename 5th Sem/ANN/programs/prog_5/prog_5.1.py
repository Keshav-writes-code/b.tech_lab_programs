import numpy as np

# Neural Network with 2 layers for XOR
def NN_XOR(input):
    weights_hidden = np.array([[1, -1], [-1, 1]])  # Detects (1,0) and (0,1)
    bias_hidden = np.array([-0.5, -0.5])  # Set bias to adjust the threshold for the hidden neurons

    weights_output = np.array([1, 1])  # Combine the results from the two hidden neurons
    bias_output = -0.5  # Adjust threshold for the output neuron

    hidden_sum = np.dot(weights_hidden, input) + bias_hidden
    hidden_output = np.array([1 if s >= 0 else 0 for s in hidden_sum])  # Step activation function

    output_sum = np.dot(weights_output, hidden_output) + bias_output
    output = 1 if output_sum >= 0 else 0  # Step activation function

    return output

# Define inputs (truth table for XOR)
inputs = np.array([
    [0, 0],
    [1, 0],
    [0, 1],
    [1, 1]
])

# Testing the XOR logic
print("\nXOR Logic\n")
print("Input : Output")
for i in inputs:
    print(i, " : ", NN_XOR(i))
print("")
