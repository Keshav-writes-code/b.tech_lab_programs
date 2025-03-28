import numpy as np
from classes import Perceptron as P

def create_digit_dataset():
  digits = np.zeros((10,15), dtype=np.int8)
  patterns = [
    [0, [[1,1,1], [1,0,1], [1,0,1], [1,0,1], [1,1,1]]],
    [1, [[1,0,0], [0,1,0], [0,1,0], [0,1,0], [0,1,0]]],
    [2, [[1,1,1], [0,0,1], [1,1,1], [1,0,0], [1,1,1]]],
    [3, [[1,1,1], [0,0,1], [1,1,1], [0,0,1], [1,1,1]]],
    [4, [[1,0,1], [1,0,1], [1,1,1], [0,0,1], [0,0,1]]],
    [5, [[1,1,1], [1,0,0], [1,1,1], [0,0,1], [1,1,1]]],
    [6, [[1,1,1], [1,0,0], [1,1,1], [1,0,1], [1,1,1]]],
    [7, [[1,1,1], [0,0,1], [0,1,0], [0,1,0], [0,1,0]]],
    [8, [[1,1,1], [1,0,1], [1,1,1], [1,0,1], [1,1,1]]],
    [9, [[1,1,1], [1,0,1], [1,1,1], [0,0,1], [0,1,1]]]
  ]
  
  # Fill the array with the patterns
  for digit, pattern in patterns:
    pattern = np.array(pattern)
    digits[digit] = pattern.flatten()
  return digits

digits = create_digit_dataset()
perceptron = P(15, [100], 10, 1)

for i, digit in enumerate(digits):
  print(f"{i}: ", end="")
  perceptron.feedForward(digit)
  perceptron.printHighestPredictedValue()

perceptron.train(digits, 100000)
22
print("\nAfter Traning: ")

for i, digit in enumerate(digits):
  print(f"----{i}-----")
  perceptron.feedForward(digit)
  perceptron.printHighestPredictedValues()
