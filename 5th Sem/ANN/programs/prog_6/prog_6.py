# Biploar AND Perceptron (Biploar I\O)
import numpy as np

# Traning / Testing Data for perceptron

data = (
  ((1,1), 1),
  ((1,-1), -1),
  ((-1,1), -1),
  ((-1,-1), -1)
)

def NN(inputsArr):
  weights = np.array([1,1])
  bias = np.array([0])
  sum = np.dot(inputsArr, weights) + bias[0]
  return ActivFunc(sum)

def ActivFunc(n):
  if n >=2:
    return 1
  else:
    return -1

for row in data:
  print("In:",row[0],"Out:", NN(row[0]))