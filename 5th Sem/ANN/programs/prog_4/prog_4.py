import os
import numpy as np

def read_matrix_from_file(filename):
    matrix = []
    with open(filename, 'r') as file:
        # Read each line in the file
        for line in file:
            # Remove any whitespace from the beginning and end of the line
            line = line.strip()
            row = []            
            # Process each character in the line
            for char in line:
                # Convert the character to an integer and add it to the row
                num = int(char)
                row.append(num)
            
            # Add the completed row to our matrix
            matrix.append(row)
    # Convert the list of lists to a NumPy array
    numpy_array = np.array(matrix)
    
    return numpy_array

filename = os.getcwd() + '/prog_4/matrix.txt'
matrix_array = read_matrix_from_file(filename)

# find size of the matrix
print("Matrix size:", matrix_array.size)
num_row, num_col = matrix_array.shape
print("Matrix shape:", num_row, "x", num_col)

#print Length of a particullar COlumn
print("Matrix Column 1st Length:", len(matrix_array[:,0]))

# print lenfth of a particular row
print("Matrix Row 1st Length:", len(matrix_array[0,:]))

print("NumPy array:")
print(matrix_array)

#save a matix to a file 
mat2 = np.array([[1,5,8],[76,34,2],[45,23,7]])
np.savetxt('./prog_4/matix2.txt', mat2)

# find out variables & Features in CUrrent Scope
print(locals())