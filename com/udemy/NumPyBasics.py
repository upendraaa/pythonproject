import numpy as np

# This is show basics function available in Numpy
list = [1, 2, 3, 4, 5, 6]
print(np.array(list))

# Two dimension array
list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(list)
print(np.array(list))

# arange method to create array
print(np.arange(1, 10))
# Jump two step
print(np.arange(0, 10, 2))

# For zero matrix
print(np.zeros(7))
# First tuple is row and second is column
print(np.zeros((2, 3)))
