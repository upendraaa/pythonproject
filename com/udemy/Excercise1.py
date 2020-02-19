print("** What is 7 to the power of 4?**")

ans = 7 ** 4

print("Answer is {}".format(ans))

print("** Split this string:** s = Hi there Sam! *into a list. *")

s = "Hi there Sam!"
ans = s.split()
print(ans)

print("** Use .format() to print the following string: **The diameter of Earth is 12742 kilometers.")

planet = "Earth"
diameter = 12742

print("The diameter of {} is {} kilometers.".format(planet, diameter))

print("lst = [1,2,[3,4],[5,[100,200,['hello']],23,11],1,7], print hello")
lst = [1, 2, [3, 4], [5, [100, 200, ['hello']], 23, 11], 1, 7]
print(lst[3][1][2][0])

print("** Given this nested dictionary grab the word 'hello'. Be prepared, this will be annoying/tricky ** "
      "d = {'k1':[1,2,3,{'tricky':['oh','man','inception',{'target':[1,2,3,'hello']}]}]}")
d = {'k1': [1, 2, 3, {'tricky': ['oh', 'man', 'inception', {'target': [1, 2, 3, 'hello']}]}]}

ans = d.get("k1")[3].get("tricky")[3].get("target")[3]
print(ans)

print("** What is the main difference between a tuple and a list? **")
print("List initialize in [] and tuple in (), list is mutable and tuple in immutable, "
      "list is collection of items, and tuple is in pairs")

print("** Create a function that grabs the email website domain from a string in the form: ** "
      "user@domain.com  So for example, passing 'user@domain.com' would return: domain.com")


def getDomain(input):
    return input.split('@')[1]


ans = getDomain("user@domain.com")
print(ans)

print("** Create a basic function that returns True if the word 'dog' is contained in the input string. "
      "Don't worry about edge cases like a punctuation being attached to the word dog, but do account for capitalization. **")


def findDog(input):
    for word in input.split():
        if (word == 'dog'):
            return 'True'


ans = findDog("Is there a dog here?")
print(ans)

print("** Create a function that counts the number of times the word "
      'dog' " occurs in a string. Again ignore edge cases. **")


def countDog(data):
    count = 0
    for word in data.split():
        if (word == 'dog'):
            count = count + 1

    return count


count = countDog("This dog runs faster than the other dog dude!")
print(count)

print(
    "** Use lambda expressions and the filter() function to filter out words from a list that don't start with the letter 's'."
    " For example:**seq = ['soup','dog','salad','cat','great'] should be filtered down to:['soup','salad']")
seq = ['soup', 'dog', 'salad', 'cat', 'great']
fun = lambda item: item.startswith('s')
list = list(filter(fun, seq))
print(list)

print(
    "*You are driving a little too fast, and a police officer stops you. Write a function to return one of 3 possible results:"
    " 'No ticket', 'Small ticket', or 'Big Ticket'. If your speed is 60 or less, the result is "
    "'No Ticket'. If speed is between 61 and 80 inclusive, the result is 'Small Ticket'. "  "If speed is 81 or more, "
    "the result is 'Big Ticket'. Unless it is your birthday (encoded as a boolean value in the parameters of the function) "
    "-- on your birthday, your speed can be 5 higher in all cases. *")


def caught_speeding(speed, is_birthday):
    if ((not is_birthday and (speed in range(60, 81))) or (is_birthday and (speed in range(60, 81 + 5)))):
        print("Small ticket")
    elif ((not is_birthday and (speed >= 81)) or (is_birthday and (speed > 80 + 5))):
        print("Big ticket")
    else:
        print("No ticket")


caught_speeding(81, True)
caught_speeding(81, False)
