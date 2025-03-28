print("")
import numpy as np

# Create/Define single dimension / multi-dimension arrays, and arrays with specific values like array of all ones, all zeros, array with random values within a range, or a diagonal matrix.

# Single Dimensional
arr_1d = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print("1D Array\n", arr_1d, "\n")

# Multi Dimensional
arr_4d = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print("ND Array\n", arr_4d, "\n")

#Array of ones
arr_ones = np.ones((3, 3))
print("Array of ones\n", arr_ones, "\n")
# Arrays of zeoes
arr_zeros = np.zeros((3, 3))
print("Array of zeros\n", arr_zeros, "\n")
# Array with random values
arr_rand = np.random.rand(3, 3)
print("Array with random values\n", arr_rand, "\n")
# Diagonal Matrix
arr_diag = np.diag([1, 2, 3, 4])
print("Diagonal Matrix\n", arr_diag, "\n")

