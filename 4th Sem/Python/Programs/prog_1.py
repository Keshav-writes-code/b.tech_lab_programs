import numpy as np

# Creating a NumPy array
arr = np.array([1, 2, 3, 4, 5])
print("Original Array:", arr)

# Calculating the sum of elements
sum_arr = np.sum(arr)
print("Sum of Array Elements:", sum_arr)

# Finding the mean of the array
mean_arr = np.mean(arr)
print("Mean of Array Elements:", mean_arr)

# Finding the maximum and minimum values in the Array
max_val = np.max(arr)
min_val = np.min(arr)
print("Maximum Value:", max_val)
print("Minimum Value:", min_val)

# Sorting the array
sorted_arr = np.sort(arr)
print("Sorted Array:", sorted_arr)

# Creating a 2D array
matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("2D Array (Matrix):\n", matrix)

# Calculating the transpose of the matrix
transposed = np.transpose(matrix)
print("Transposed Matrix:\n", transposed)

# Calculating the square root of array elements
sqrt_arr = np.sqrt(arr)
print("Square Roots of Array Elements:", sqrt_arr)
