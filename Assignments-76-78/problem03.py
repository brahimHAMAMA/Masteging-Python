from functools import reduce


def product(num1, num2):
    return num1 * num2
nums = [2, 4, 6, 2]

result = reduce(product, nums)
print(result)

print("="* 20)
product = lambda num1, num2: num1 * num2

result = reduce(product, nums)
print(result)

# Output
96