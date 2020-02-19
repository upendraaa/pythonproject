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

# For ones matrix
print(np.ones(5))

print(np.ones((3, 4)))

# evenly devide
print(np.linspace(2, 10, 20))

# Identity matrix, this is 0,1 matrix, all the digonal values will 1 and others as 0

I2 = np.eye(2)
I3 = np.eye(3)
print(I2)
print(I3)
print(np.eye(4, 3))

# Random array limit from 0 to 1
print(np.random.rand(19))

# Random distribution can be any negative and positive number
print(np.random.randn(9))

# Random array low to high number, 2 is low inclusive, 100 is high exclusive, 5 is size
print(np.random.randint(2, 100, 5))

# Array reshape method

arr = np.arange(15)
print(arr)

# This will create the matrix of 3*5
print(arr.reshape(3, 5))

# To get the shape
print(arr.shape)
# To get the max and it's position
print(arr.max())
print(arr.argmax())

# To find the min and it's position
print(arr.min())
print(arr.argmin())

# Get the datatype in array
print(arr.dtype)
