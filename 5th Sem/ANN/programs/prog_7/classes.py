import numpy as np

class Perceptron:
  def __init__(self, inLayer_size, hiddenLayer_sizes, outLayerSize, lRate):
    """
    Construct a new Perceptron with the specified number of layers.
    
    Parameters
    ----------
    inLayer_size : int
      The number of neurons in the input layer
    hiddenLayer_sizes : list of int
      The number of neurons in each of the hidden layers
    outLayerSize : int
      The number of neurons in the output layer
    lRate : float
      The learning rate for the network
    
    Notes
    -----
    The weights for the layers are initialized to small random values.
    """
    self.inputLayer_Values = np.zeros(inLayer_size)
    
    # Contains neuron values in Vector for each hidden layer
    self.hiddenLayers_values = []
    for size in hiddenLayer_sizes:
      self.hiddenLayers_values.append(np.zeros(size))
    
    # Stores the Weights matrix for each neurons in a 3d Matix much like input layer and Output layer above and below
    self.hiddenLayers_weights = []
    prevLayer_size = inLayer_size
    for size in hiddenLayer_sizes:
      # This just give me a "n x m" matrix with random values
      weightMatrix_forThisLayer = np.random.randn(size, prevLayer_size) * 1
      self.hiddenLayers_weights.append(weightMatrix_forThisLayer)
      prevLayer_size = size

    self.outputLayer_values = np.zeros(outLayerSize)
    # this give a matrix for weight with random values
    self.outputLayer_weights = np.random.randn(outLayerSize, prevLayer_size)

    self.lRate = lRate
  def softmax(self, x):
      e_x = np.exp(x - np.max(x))  # subtracting max(x) for numerical stability
      return e_x / e_x.sum(axis=0)
  def printPredictions(self):
    finalOut = []
    for i, prediction in enumerate(self.outputLayer_values):
      finalOut.append([i, prediction])
    finalOut = np.array(finalOut)
    finalOut = self.softmax(finalOut)
    finalOut= finalOut[finalOut[:, 1].argsort()[::-1]]
    for i in finalOut:
      print(f"Digit {round(i[0])} : {round(i[1],2)}")
  def printHighestPredictedValue(self):
    softmaxed = self.softmax(self.outputLayer_values)
    print(f"{np.argmax(softmaxed)} ({round(np.max(softmaxed)*100,1)}%) ")
  def printHighestPredictedValues(self):
    # print top 3 predictions
    softmaxed = self.softmax(self.outputLayer_values)
    print(f"{np.argmax(softmaxed)}: ({round(np.max(softmaxed)*100,2)}%)")
    print(f"{np.argmax(softmaxed[1:])}: ({round(softmaxed[1:][np.argmax(softmaxed[1:])]*100,2)}%)")
    print(f"{np.argmax(softmaxed[2:])}: ({round(softmaxed[2:][np.argmax(softmaxed[2:])]*100,2)}%)")

  def sigmoid(self, x):
    return 1 / (1+np.exp(-x))
  def feedForward(self, input):
    self.inputLayer_Values = input
    activation = input
    for i, weight_matrix in enumerate(self.hiddenLayers_weights):
      # z is a vector that stores the value for netxt layers's neurons
      z = np.dot(weight_matrix, activation)
      activation = self.sigmoid(z)
      self.hiddenLayers_values[i] = activation
    z_out = np.dot(self.outputLayer_weights, activation)
    output = self.sigmoid(z_out)
    self.outputLayer_values = output
    return output
  def train(self, data, epochs):
    targets = np.eye(10, dtype=np.int8)
    for epoch in range(epochs):
      for i in range(len(data)):
        self.feedForward(data[i])
        self.backPropagation(targets[i])
  def backPropagation(self, target):
    # Calculate error at output layer
    output_errors = self.outputLayer_values - target
    output_deltas = output_errors * self.outputLayer_values * (1 - self.outputLayer_values)

    # Adjust weights for the output layer
    last_hidden_output = self.hiddenLayers_values[-1]
    self.outputLayer_weights -= self.lRate * np.outer(output_deltas, last_hidden_output)

    # Start backpropagating the error through each hidden layer
    deltas = output_deltas
    for i in range(len(self.hiddenLayers_weights) - 1, -1, -1):
      # Calculate error for current hidden layer
      layer_output = self.hiddenLayers_values[i]
      hidden_errors = np.dot(self.outputLayer_weights.T, deltas) if i == len(self.hiddenLayers_weights) - 1 else np.dot(self.hiddenLayers_weights[i + 1].T, deltas)
      hidden_deltas = hidden_errors * layer_output * (1 - layer_output)

      # Update weights for the hidden layer
      prev_layer_output = self.inputLayer_Values if i == 0 else self.hiddenLayers_values[i - 1]
      self.hiddenLayers_weights[i] -= self.lRate * np.outer(hidden_deltas, prev_layer_output)

      # Update delta for the next layer in backpropagation
      deltas = hidden_deltas
  
