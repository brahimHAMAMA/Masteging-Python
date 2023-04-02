def checkNumber(num):
    return num>10
num = [11, 1, 20, 50,100,2,3]

dataFormat = filter(checkNumber, num)

print(type(dataFormat))
# print(list(dataFormat))
for name in list(dataFormat):
    print(name)


print("="*20)
checkNumber = lambda num: num>10
num = [11, 1, 20, 5]

dataFormat = filter(checkNumber, num)

print(type(dataFormat))
print(dataFormat)
for name in dataFormat:
    print(name)