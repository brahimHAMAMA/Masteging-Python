from functools import reduce

def sumAll(num1, num2):
    return num1 + num2
num = [10, 10, 20, 50,10,2,3]

dataFormat = reduce(sumAll, num, 5)

print(type(dataFormat))
print(dataFormat)



print("="*20)
