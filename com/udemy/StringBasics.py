name = "Upendra Singh"
firstName = 'Upendra'

print(name)
print(firstName)

print("First character of name {}".format(name[0]))
print("Substring after index 2 onwards {}".format(name[2:]))
# Index 2 is inclusive and 6 is exclusive
print("Substring between index 2 to 6 {}".format(name[2:6]))

# One dimension character array
charArray = ['a','b','c','d']
print(charArray)

# Two dimension character array
twoDimCharArray = ['a','b','c','d',['e','f','g','h']]
print(twoDimCharArray)

print(twoDimCharArray[4][2:])