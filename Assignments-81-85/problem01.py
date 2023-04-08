def reverse_string(my_string):
    yield my_string[5]
    yield my_string[4]
    yield my_string[3]
    yield my_string[2]
    yield my_string[1]
    yield my_string[0]

# Your Code Here

# Reverse The String
for c in reverse_string("Elzero"):
    print(c)