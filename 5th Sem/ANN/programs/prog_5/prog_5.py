# XOR Logic

import numpy as np

inputs = np.array([
    [0,0],
    [1,0],
    [0,1],
    [1,1]
])

def NN(input):
    weights = np.array([ 1, 1])
    bias = 0
    val = (input[0] * weights[0]) + (input[1] * weights[1]) + bias
    if val <= 0:
        return 0
    elif val > 0 and val <= 1:
        return 1
    elif val >= 2:
        return 0 

NNin = inputs[3]
print("")
print("XOR Logic\n")
print("Input : Output")

for i in inputs:
    print(i, " : ", NN(i))
print("")




