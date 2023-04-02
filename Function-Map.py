def formatName(name):
    return f"- {name.capitalize().strip()} -"

myFrinds = [" BRaHim ", "   aLi   ", "   AmINa   ", "   sAmi "]

dataFormat = map(formatName, myFrinds)

print(type(dataFormat))
# print(list(dataFormat))
for name in list(dataFormat):
    print(name)


print("="*20)
formatName = lambda name: f"- {name.capitalize().strip()} -"

myFrinds = [" BRaHim ", "   aLi   ", "   AmINa   ", "   sAmi "]

dataFormat = map(formatName, myFrinds)

print(type(dataFormat))
print(dataFormat)
for name in dataFormat:
    print(name)