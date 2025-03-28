# Biploar AND Perceptron (Biploar I\O) with training process
import numpy as np
import random as rd
# Traning / Testing Data for perceptron
data = (
  ((1,1), 1),
  ((1,0), -1),
  ((0,1), -1),
  ((0,0), -1)
)
import numpy as np

def randFloat(low, high, size):
  random_numbers = np.random.uniform(low, high, size)
  bipolar_numbers = random_numbers - (low + high) / 2
  return bipolar_numbers

class Perceptron:
  def __init__(self, weights, bias, lRate):
    self.weights = weights
    self.bias = bias
    self.lRate = lRate
  def feedforward(self, Vinput):
    total = np.dot(Vinput, self.weights) + self.bias
    return self.activation(total)
  def activation(self, x):
    if x >= 2:
      return 1
    else:
      return -1
  def train(self, data, epoch):
    for _ in range(epoch):
      for inputs, expected_output in data:
        prediction = self.feedforward(inputs)
        error = expected_output - prediction
        # Update the weights and bias using the perceptron learning rule
        for i in range(len(self.weights)):
          self.weights[i] += self.lRate * error * inputs[i]
        # Update the bias
        self.bias[0] += self.lRate * error
      print(f"Epoch {_+1}: Accuracy: {self.calculateAccuracy(data)}%")  # Print the accuracy after each epoch self.calculateAccuracy(data)

  def showParameters(self):
    print("Parameters:")
    for i,weight in enumerate(self.weights):
      print(f"weight_{i} : {round(weight,2)}")
    for i, bias in enumerate(self.bias):
      print(f"bias_{i} : {round(bias,2)}")
  def calculateAccuracy(self, data):
    # Calculate accuracy as a percentage of correct predictions
    correct_predictions = 0
    for inputs, target in data:
        prediction = self.feedforward(inputs)
        if prediction == target:
            correct_predictions += 1
    accuracy = (correct_predictions / len(data)) * 100
    return accuracy

randRange = 1
p1 = Perceptron(randFloat(-randRange,randRange,2), randFloat(-randRange,randRange,1), 0.1)
print("\n---------Before Traning---------")
p1.showParameters()
print("\nFeedForward Output:")
for row in data:
  print("In:",row[0],"Out:", p1.feedforward(row[0]))
print(f"Accuracy: {p1.calculateAccuracy(data)}%")

print("\n---------After Traning---------")
p1.train(data, 10)
p1.showParameters()

print("\nFeedForward Output:")
for row in data:
  print("In:",row[0],"Out:", p1.feedforward(row[0]))

print(f"Accuracy: {p1.calculateAccuracy(data)}%")
