'''
Write a Python program to transpose a matrix using a nested loop
'''

# Original matrix (3 rows × 2 columns)
x = [[1, 2],   # Row 1
     [3, 4],   # Row 2
     [5, 6]]   # Row 3

# Create an empty result matrix (2 rows × 3 columns)
# Because transpose of 3x2 becomes 2x3
result = [[0, 0, 0],
          [0, 0, 0]]

# -----------------------------------
# Method 1: Using NumPy (built-in function)
# -----------------------------------

import numpy as np   # Import numpy library

# np.transpose() automatically transposes the matrix
c = np.transpose(x)

print("Transpose using NumPy:")
print(c)


# -----------------------------------
# Method 2: Using Nested Loops
# -----------------------------------

# Outer loop → runs through rows of original matrix
for i in range(len(x)):
    
    # Inner loop → runs through columns of original matrix
    for j in range(len(x[0])):
        
        # Swap rows and columns
        # Put element at position [i][j] into [j][i]
        result[j][i] = x[i][j]

print("Transpose using nested loops:")

# Print the transposed matrix row by row
for r in result:
    print(r)