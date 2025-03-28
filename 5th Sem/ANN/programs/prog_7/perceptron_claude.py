import numpy as np


class Perceptron:
  def __init__(self, input_layer_size, hidden_layer_sizes, output_layer_size, learning_rate):
      # Input layer initialization
      self.input_layer_values = np.zeros(input_layer_size)

      # Hidden layers initialization
      self.hidden_layers_values = []
      for size in hidden_layer_sizes:
          self.hidden_layers_values.append(np.zeros(size))

      # Initialize weights for hidden layers
      self.hidden_layers_weights = []
      prev_layer_size = input_layer_size

      for hidden_size in hidden_layer_sizes:
          # Create weight matrix for each layer
          weight_matrix = np.random.randn(
              hidden_size, prev_layer_size) * 0.01
          self.hidden_layers_weights.append(weight_matrix)
          prev_layer_size = hidden_size

      # Output layer initialization
      self.output_layer_values = np.zeros(output_layer_size)
      self.output_layer_weights = np.random.randn(
          output_layer_size, hidden_layer_sizes[-1]) * 0.01

      # Learning rate
      self.learning_rate = learning_rate

  def forward(self, inputs):
      """
      Forward propagation through the network
      """
      # Set input values
      self.input_layer_values = inputs

      # Propagate through hidden layers
      current_input = inputs
      for i in range(len(self.hidden_layers_weights)):
          # Calculate layer output
          layer_output = np.dot(self.hidden_layers_weights[i], current_input)
          # Apply activation function (ReLU)
          self.hidden_layers_values[i] = np.maximum(0, layer_output)
          current_input = self.hidden_layers_values[i]

      # Calculate final output
      self.output_layer_values = np.dot(
          self.output_layer_weights, current_input)
      return self.output_layer_values
