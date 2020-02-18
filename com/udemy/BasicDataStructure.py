
# Initialize the list, this is mutable
print("List example: ")
list = [1,2,3,4,5]
print(list)

# change first element
list[0] = 'change'
print(list)

# Append element
list.append('Element')
print(list)

# Dictionary data structure, this is like hash table
print("Dictionary example: ")

dictionary = {'key1':'Value1','key2':'value2','key3':[1,2,3,4,5]}
print(dictionary)
print(dictionary['key1'])
print(dictionary['key3'][2])
print(dictionary['key3'][1:])

# Tuple this is the Immutable data structure
print("Tuple example: ")
tuple = (1,2,3,4)
print(tuple)
print(tuple[2])
# This will throw exception tuple[1]= 'change'

# Set is data structure, this contain unique element
print("Set example: ")
exampleSet = {1,1,1,2,3,4,5,}
print(exampleSet)
exampleSet.add(6)
print(exampleSet)