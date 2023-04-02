name = "osama elzero"


theName = name.split(" ")

print(theName)
newList = []
for n in theName:
    newList.append(n.capitalize())

print(newList)
newName = " ".join(newList)
print(newName)

print("="*20)
print(name.title())

print("="*20)

joined = " ".join(word.capitalize() for word in theName)
print(joined)

print("="*20)
