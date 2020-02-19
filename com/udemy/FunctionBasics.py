# Basic introduction of functions
print("Basic function")


def cube(x): {
    print("Cube of number {} is {}".format(x, x ** 3))
}


# Invoking method
cube(10)


# Writing the method docs

def cube(x=9):
    """
    this is python doc
    Take number x as input and return cube of x
    """

    return x ** 3


# If no number pass function will take default 9
cubeNumber = cube()
print(cubeNumber)

cubeNumber = cube(11)
print(cubeNumber)
