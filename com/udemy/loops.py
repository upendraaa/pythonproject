# For loops
numbers = [1, 2, 3, 4, 5]
print("For loop: ")
for number in numbers:
    print(number)

# While loop
n = 1
print("While loop")
while n < 5:
    print(n)
    n = n + 1

# Number in range
print("Number in range")
# This will print 0 to 10
r = range(10)
for n in r:
    print(n)

# Print number in range 3 to 6
print("Number in range 3 to 6")
r = range(3, 6)
for n in r:
    print(n)

# Sample loop
out = []
for number in numbers:
    out.append(number ** 3)

print(out)

# extension
print("Extension")
out = [number ** 3 for number in numbers]
print(out)
