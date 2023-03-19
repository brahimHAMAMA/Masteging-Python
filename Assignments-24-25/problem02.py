friends = ("Osama", "Ahmed", "Sayed")
friends = list(friends)
friends[0]= "Elzero"
print(friends)
print(type(friends))


friends = tuple(friends)
print(friends)
print(type(friends))

print(len(friends))
# Needed Output

# ("Elzero", "Ahmed", "Sayed")
# <class 'tuple'>
# 3 Elements